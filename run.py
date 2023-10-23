
import os
import uvicorn


API = 'app.main:app'
HOST = '0.0.0.0'
PORT = 8001


if __name__ == '__main__':
    os.environ["GPIOZERO_PIN_FACTORY"] = "mock"
    uvicorn.run(API, host=HOST, port=PORT, reload=True, log_level='debug')