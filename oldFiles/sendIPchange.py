#!/usr/bin/python

# Import smtplib for the actual sending function
import smtplib, sys, random
from funcs import *

# declare variable for reference
newIP = sys.argv[1]
date = sys.argv[2]
list = "lineList"
limit = get_line(list)
print limit

# grab old IP
f = open('tempIP', 'r')
oldIP = f.readline().strip()
f.close()


#send msg from list or new IP

if limit != 0:
	random.seed()
	numC = random.randrange(0, limit)
	with open(list) as comp:
		for i, line in enumerate(comp):
			if i == numC:
				sendMail("6504006400@vtext.com", line, "verizon")
#				sendMail("6507991555@txt.att.net", line)
			elif i > numC:
				break
	remove_line(list, numC)  #opening sendFile.txt twice - not necessary - easier to understand + portability of functions - good for now
else:
	sendMail("6504006400@vtext.com", "Quotes Depleted", "verizon")


if oldIP != newIP:
	# want to send from different email server.login("tifmrp1324@gmail.com", "wussgood$$")
        sendMail("6504006400@vtext.com", newIP, "verizon")
	with open('tempIP', 'w') as f:
		f.write(newIP)
	with open('IPlogchange.txt', 'a') as log:
		log.write(date + " - " +  newIP + "\n")

server.quit()


