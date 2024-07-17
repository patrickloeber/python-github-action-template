"""
Retrieve weather data for a given city and log it.
"""

import csv
import logging
from datetime import datetime
from typing import Optional
import os

import pytz
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


def get_weather_data(city: str) -> Optional[dict]:
    """
    Get weather data for the given city from the Talk Python Weather API.

    :param city: The city for which to get the weather data.
    :return: A dictionary containing the weather data or None if the request failed.
    """
    api_url = "https://weather.talkpython.fm/api/weather/"
    params = {"city": city, "country": "IN"}
    try:
        response = requests.get(api_url, params=params, timeout=10)
        return response.json() if response.status_code == 200 else None
    except (requests.Timeout, requests.RequestException):
        return None


def log_weather_data(city: str, data: dict) -> None:
    """
    Log the weather data for a given city.

    :param city: The city for which the weather data is logged.
    :param data: The weather data to be logged.
    """
    logger.info("City: %s", city)
    logger.info("Temperature: %s", data.get("forecast", {}).get("temp"))
    logger.info("Feels Like: %s", data.get("forecast", {}).get("feels_like"))
    logger.info("Humidity: %s", data.get("forecast", {}).get("humidity"))

    utc_now = datetime.utcnow()
    ist_now = utc_now.astimezone(pytz.timezone("Asia/Kolkata"))

    logger.info("Current IST time: %s", ist_now.strftime("%Y-%m-%d %H:%M:%S"))

    with open("weather_data.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Timestamp", "Temperature", "Feels Like", "Humidity"])
        writer.writerow(
            [
                ist_now.strftime("%Y-%m-%d %H:%M:%S"),
                data.get("forecast", {}).get("temp"),
                data.get("forecast", {}).get("feels_like"),
                data.get("forecast", {}).get("humidity"),
            ]
        )


def main() -> None:
    """
    The main function for this module.
    """
    token = os.environ.get("SOME_SECRET")
    if token is None:
        logger.error("Token value is not available.")
        return

    city = "Pune"
    data = get_weather_data(city)
    if data is None:
        logger.error("Failed to get weather data for %s.", city)
        return

    log_weather_data(city, data)


if __name__ == "__main__":
    main()
