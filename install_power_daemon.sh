#!/bin/bash

mkdir /usr/local/bin/power_daemon
cp power_daemon.* /usr/local/bin/power_daemon/
crontab -l|sed "\$a@reboot /usr/local/bin/power_daemon/power_daemon.sh"|crontab -
