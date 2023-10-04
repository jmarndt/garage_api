# Garage API
This API control lights and doors for the garage. It runs on a Raspbeery Pi (zero W in my case), connected to an 8-relay module and a modified Lutron Pico remote.

## Dependencies
Create a virtual environment with
```
python3 -m venv .env && source .env/bin/activate
```

Install depndencies with
```
python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt
```

## Authentication
The API is secured with a key that is contained in `.env/api_key`.
To set or change this key run
```
echo "MySecretKey" > .env/api_key
```

## Running
For local development and testing, run `python3 run.py`.
In prodcution add the `--prod` flag: `python3 run.py --prod`.
For best results, create a system service to run this on startup. This can be done with `create_systemd_service.py`.
