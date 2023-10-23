import uvicorn


API = 'app.main:app'
HOST = '0.0.0.0'
PORT = 8001


if __name__ == '__main__':
    uvicorn.run(API, host=HOST, port=PORT)