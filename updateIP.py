#!/usr/bin/python

# Import smtplib for the actual sending function
import smtplib, sys, random
from funcs import *

# declare variable for reference
newIP = sys.argv[1]
date = sys.argv[2]
list = "lineList"
limit = get_line(list)

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
				sendMail("PHONENUNMBER@vext.com", line, "verizon")
			elif i > numC:
				break
	remove_line(list, numC)  
else:
	sendMail("6504006400@vtext.com", "Quotes Depleted", "verizon")


if oldIP != newIP:
        sendMail("PHONENUMBER@vtext.com", newIP, "verizon")
	with open('tempIP', 'w') as f:
		f.write(newIP)
	with open('IPlogchange.txt', 'a') as log:
		log.write(date + " - " +  newIP + "\n")

server.quit()


