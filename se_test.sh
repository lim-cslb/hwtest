#!/bin/bash

rm /tmp/chipinfo.txt
sleep 6
sudo /home/lim/linux-optiga-trust-m/bin/trustm_chipinfo > /tmp/chipinfo.txt
if grep -q rgbBatchNumber /tmp/chipinfo.txt; then
    echo -n "00FF00" | sudo tee /tmp/led6 >/dev/null
else
    echo -n "FF0000" | sudo tee /tmp/led6 >/dev/null
fi
