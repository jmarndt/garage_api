import os
import venv


API_NAME = "garage"


RUN_PATH = os.path.dirname(__file__)
API_SERVICE_NAME = f'{API_NAME.lower()}.api'
PY_ENV_PATH = f'{RUN_PATH}/env'
SERVICE_FILE_PATH = f'/etc/systemd/system/{API_SERVICE_NAME}.service'
SERVICE_FILE_CONTENTS = f"""[Unit]
Description = {API_NAME} api service
After = network.target

[Service]
Type = simple
Restart = always
SyslogIdentifier = {API_NAME}
ExecStart = {PY_ENV_PATH}/bin/python {RUN_PATH}/run.py --prod

[Install]
WantedBy = multi-user.target"""


def build_python_env():
    venv.create(PY_ENV_PATH, with_pip=True)
    os.system(f'{PY_ENV_PATH}/bin/pip install -r {RUN_PATH}/requirements.txt')


def create_service_file():
    with open(SERVICE_FILE_PATH, 'w') as service_file:
            service_file.write(SERVICE_FILE_CONTENTS)


def enable_service():
    os.system(f'systemctl enable {API_SERVICE_NAME}')
    os.system('systemctl daemon-reload')
    os.system(f'systemctl start {API_SERVICE_NAME}')


if __name__ == '__main__':
    build_python_env()
    create_service_file()
    enable_service()