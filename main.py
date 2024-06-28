"""
This module provides functionality for retrieving weather data and logging it.

It fetches weather data for Pune, India, from the Talk Python Weather API, logs the retrieved data, 
and handles the absence of the environment variable 'SOME_SECRET'.

Author: [Swapnanil Sharmah]
"""

import logging
import logging.handlers
import os
from datetime import datetime
import pytz
import requests
import csv

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    # logger.info("Token not available!")
    # raise


if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")
    city = "Pune"
    try:
        r = requests.get(
            f"https://weather.talkpython.fm/api/weather/?city={city}&country=IN",
            timeout=10,
        )
        if r.status_code == 200:
            data = r.json()
            temperature = data["forecast"]["temp"]
            feels_like = data["forecast"]["feels_like"]
            humidity = data["forecast"]["humidity"]

            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

            # Get the current time in UTC
            utc_now = datetime.utcnow()

            # Convert UTC time to IST
            ist = pytz.timezone("Asia/Kolkata")
            ist_now = utc_now.astimezone(ist)

            # Format and print the IST time
            logger.info(f'Current IST time: {ist_now.strftime("%Y-%m-%d %H:%M:%S")}')

            logger.info(
                f"Temperature in {city}: {temperature}, it feels like: {feels_like}, with Humidity: {humidity}"
            )

            # Write data to CSV file
            with open("weather_data.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                # Check if file is empty to write the header
                if file.tell() == 0:
                    writer.writerow(
                        ["Timestamp", "Temperature", "Feels Like", "Humidity"]
                    )
                writer.writerow(
                    [
                        ist_now.strftime("%Y-%m-%d %H:%M:%S"),
                        temperature,
                        feels_like,
                        humidity,
                    ]
                )

    except requests.Timeout:
        # Handle timeout exception here
        print("Timeout occurred while fetching weather data.")

    except requests.RequestException as e:
        # Handle other request exceptions here
        print("An error occurred:", e)
