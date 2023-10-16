import os
import argparse
import uvicorn
from dotenv import load_dotenv


API = 'app.main:app'
HOST = '0.0.0.0'
PORT = 8001


parser = argparse.ArgumentParser(
    prog = 'run_api.py',
    description = 'Runs the Fast API',
    epilog=f'Default behavior with no options provided will run in development mode on port {PORT}'
)
parser.add_argument('--port', help='port number to use', type=int, dest='port', default=PORT)
parser.add_argument('--host', help='host address to use', type=str, dest='host', default=HOST)
parser.add_argument('--prod', help='runs api in production mode', action='store_true', dest='production')


if __name__ == '__main__':
    load_dotenv()
    args = parser.parse_args()
    if args.production:
        uvicorn.run(API, host=args.host, port=args.port)
    else:
        os.environ["GPIOZERO_PIN_FACTORY"] = "mock"
        uvicorn.run(API, host=args.host, port=args.port, reload=True, log_level='debug')