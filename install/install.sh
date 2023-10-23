#!/bin/sh

if [ "$(id -u)" -ne "0" ] ; then
    echo "This script must be executed with root privileges."
    exit 1
fi

LOG_FILE=/opt/garage_api.log
INSTALL_DIR=/opt/garage_api
APP_DIR=../app
RUN_FILE=run.py
ENV_FILE=$INSTALL_DIR/.env
SERVICE_NAME=garage_api.service
SERVICE_FILE_CONTENTS=garage_api_service
SERVICE_FILE=/etc/systemd/system/$SERVICE_NAME

write_log() {
    echo "[$(date -u --iso-8601=ns | sed s/+00:00/Z/ | sed s/,/./)] INSTALL: $1" >> $LOG_FILE
}

install_deps() {
    write_log "Installing dependencies...."
    apt install -yq python3 python3-pip python3.11-venv
}

install_api_files() {
    write_log "Installing API to $INSTALL_DIR...."
    if [ -d $INSTALL_DIR ]; then
        rm -rf $INSTALL_DIR
    fi
    mkdir $INSTALL_DIR

    cp -r $APP_DIR $INSTALL_DIR
    cp $RUN_FILE $INSTALL_DIR
    touch $INSTALL_DIR/.env

    python3 -m venv $INSTALL_DIR/venv
    $INSTALL_DIR/venv/bin/pip install -r ../requirements.txt
}

create_service() {
    write_log "Creating $SERVICE_FILE...."
    cat $SERVICE_FILE_CONTENTS > $SERVICE_FILE
}

enable_service() {
    write_log "Enabling $SERVICE_NAME...."
    systemctl daemon-reload
    systemctl enable $SERVICE_NAME
    systemctl start $SERVICE_NAME
}

do_install() {
    write_log "Beginning Garage API install...."
    install_deps
    install_api_files
    create_service
    enable_service
    write_log "Garage API install complete!"
}

do_install