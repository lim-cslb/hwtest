#!/bin/bash

mkdir /usr/local/bin/connectivity_daemon
cp connectivity_daemon.* /usr/local/bin/connectivity_daemon/
crontab -l|sed "\$a@reboot /usr/local/bin/connectivity_daemon/connectivity_daemon.sh"|crontab -
