#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "Please run script as root."
  exit 1
fi

DATE=$(date +%F_%H-%M-%S)
FILENAME="log_backup_$DATE.zip"

zip -r $FILENAME ./logs

if [ ! -d "/opt/backups/" ]; then
  sudo mkdir /opt/backups
fi
sudo mv $FILENAME /opt/backups
sudo chmod 700 /opt/backups

echo "Backup logs successfully"