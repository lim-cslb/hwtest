#!/bin/bash

mkdir /usr/local/bin/fan_daemon
cp fan_daemon.* /usr/local/bin/fan_daemon/
crontab -l|sed "\$a@reboot /usr/local/bin/fan_daemon/fan_daemon.sh"|crontab -
