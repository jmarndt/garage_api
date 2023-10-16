import os

from urllib3.response import HTTPResponse
from amcrest import AmcrestCamera


CAMERA_USER = os.getenv('CAMERA_USER')
CAMERA_PASS = os.getenv('CAMERA_PASS')
CAMERA_HOST = os.getenv('CAMERA_HOST')
CAMERA = AmcrestCamera(CAMERA_HOST, 80, CAMERA_USER, CAMERA_PASS).camera


def camera_snapshot() -> bytes:
    response = CAMERA.snapshot()
    return response.read()


if __name__ == "__main__":
    pass