#!/bin/sh

cd /opt/garage_api
. venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8001