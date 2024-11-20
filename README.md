# Schedule a Python script with GitHub Actions

**Watch the video tutorial:**

[![Alt text](https://img.youtube.com/vi/PaGp7Vi5gfM/hqdefault.jpg)](https://youtu.be/PaGp7Vi5gfM)

This example shows how to run a Python script as cron job with GitHub Actions. It calls an API once a week (could be any schedule you want), logs the response in `status.log`, and automatically pushes the changes to this repo.

- Implement your script in `main.py`
- Inspect and configure cron job in GitHub Action `.github/workflows/actions.yml`
- It can install and use third party packages from `requirements.txt`
- Secret environment variables can be used. Set secrets in Settings/Secrets/Actions -> 'New repository secret'. Use the same secret name inside `actions.yml` and `main.py`

# Actions failing because of Node issues while running GitHub workflow or other issues

- In case a step of the workflow fails because of Node-related issue, you need to update the version of the actions you use to the most recent ones. Check out the actions repositories:

1. [actions/checkout](https://github.com/actions/checkout)
2. [actions/setup-python](https://github.com/actions/setup-python)
3. [ad-m/github-push-action](https://github.com/ad-m/github-push-action)

- Should the push action fail because of a permission error like `remote: Write access to repository not granted.`, grant the remote write access from your repository under `Settings -> Actions -> General -> Workflow permissions."
