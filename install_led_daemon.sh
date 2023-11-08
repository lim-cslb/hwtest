#!/bin/bash

mkdir /usr/local/bin/led_daemon
cp led_daemon.* /usr/local/bin/led_daemon/
crontab -l|sed "\$a@reboot /usr/local/bin/led_daemon/led_daemon.sh"|crontab -
