from urllib3.response import HTTPResponse

from amcrest import AmcrestCamera


USERNAME = 'admin'
PASSWORD = 'Testing123'
HOSTNAME = 'amcresteth'
CAMERA = AmcrestCamera(HOSTNAME, 80, USERNAME, PASSWORD).camera


def camera_snapshot() -> bytes:
    response = CAMERA.snapshot()
    return response.read()


if __name__ == "__main__":
    pass