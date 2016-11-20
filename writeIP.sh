#!/bin/bash

ip=$(lynx --dump http://ipecho.net/plain)
date=$(date)
#echo  "$date - $ip" >> ~/IP_Update/IPlogchange.txt

#open temp compare ips if same quit if false sendIP.py
# how the fuck do you do this in bash maybe just do it in python way easier
# did it in python :/

cd ~/updateIP
python updateIP.py $ip "$date"
