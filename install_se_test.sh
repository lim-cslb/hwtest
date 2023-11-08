#!/bin/bash

mkdir /usr/local/bin/se_test
cp se_test.* /usr/local/bin/se_test/
crontab -l|sed "\$a@reboot /usr/local/bin/se_test/se_test.sh"|crontab -
