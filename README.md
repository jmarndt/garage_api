# Garage API
Setting up and running this API relies on Poetry. Install it using `pip install poetry` or follow their instructions: https://python-poetry.org/docs/#installation

## Dependencies
First create a virtual env with `python3 -m venv .env && source .env/bin/activate`.
Then install depndencies with `python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt`

## Running
For local development and testing, run `python3 run.py`.
In prodcution add the `--prod` flag.
For best results, create a system service to run this on startup. This can be done with `create_systemd_service.py`.
