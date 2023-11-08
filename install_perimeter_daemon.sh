#!/bin/bash

mkdir /usr/local/bin/perimeter_daemon
cp perimeter_daemon.* /usr/local/bin/perimeter_daemon/
crontab -l|sed "\$a@reboot /usr/local/bin/perimeter_daemon/perimeter_daemon.sh"|crontab -
