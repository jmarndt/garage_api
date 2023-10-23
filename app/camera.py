import os
from io import BytesIO

from dotenv import load_dotenv
from urllib3.response import HTTPResponse
from amcrest import AmcrestCamera
from amcrest.exceptions import CommError


load_dotenv()
CAMERA_USER = os.getenv('CAMERA_USER')
CAMERA_PASS = os.getenv('CAMERA_PASS')
CAMERA_HOST = os.getenv('CAMERA_HOST')
CAMERA = AmcrestCamera(CAMERA_HOST, 80, CAMERA_USER, CAMERA_PASS).camera


def camera_snapshot() -> bytes:
    try:
        response = CAMERA.snapshot()
        return BytesIO(response.read())
    except CommError:
        return None


if __name__ == "__main__":
    pass