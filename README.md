# PI Dropbox & Server

## Access your pi from anywhere - host a site, use it as a dropbox, have scripts running, etc.

## Configure pi to check external IP 
## Sends a custom msg if IP stays the same (mine is configured to send a random inspirational quote)
## Send new IP address if changed

## writeIP.sh - bash script runs every 3 hours using crontab. Grabs external IP passes it to updateIP.py

## updateIP.py - python script logs into server, check new IP vs old IP, logs into server, randomly selects quote to send and/or new IP
## I have it setup to text me the number, if you do this you will need to modify @carrier to your carrier.

## funcs.py - useful functions. For texting sendMail recurisvely breaks long messages into less than 150 chars so they aren't truncated
## the verizon email to text service truncates msg at 150 this is not the case for other carriers


