# Garage API
This API control lights and doors for the garage. It runs on a Raspbeery Pi (zero W in my case), connected to an 8-relay module and a modified Lutron Pico remote.

## Development
Create a virtual environment with
```
python3 -m venv venv && source venv/bin/activate
```

Install depndencies with
```
python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt
```
### Run Locally
Run locally with `python3 run.py`

## Authentication
The API is secured with a key. On startup it is expecting to find an environment variable called `API_KEY`. This needs to be set before run, or stored in a `.env` file (see `example.env`).

## Installing
Installing will copy the `app` folder to `/opt/garage_api` install dependendies and create a systemd service. To install, `cd` into `install` and run `./install.sh`