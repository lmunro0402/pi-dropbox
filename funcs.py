import smtplib, time
#functions for raspberry pi server/dropbox/email reminder system

# do not remove this. It starts the server to send mail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("EMAIL@gmail.com", "PASSWORD")
# can't login to both will use the first one

def get_line(file):
	count = 0
	with open(file) as f:
        	for line in f:
        		count += 1
        return count

def remove_line(file, num):
	with open(file, 'r') as f:
		d = f.readlines()
	with open(file, 'w') as f:
		for i, line in enumerate(d):
			if i != num:
				f.write(line)
			else:
				rline = line
		f.close()
	with open("removed", 'a') as rem:
		rem.write(rline)
	return None


#def sendMail(pNum, msg, carrier):
#	if carrier == "verizon":	
#		limit = 150
#	    	while len(msg) > limit:
#			if len(msg) < 201:
#				limit = 100
#			tEnd = limit - msg[limit:0:-1].find(" ")
#			if tEnd == limit+1: # didn't find a space
#				server.sendmail("tifmrp1324ip@gmail.com", pNum, msg[0:limit])
#				msg = msg[limit:] # leave nothing out there is no space
#			else: 
#            			server.sendmail("tifmrp1324ip@gmail.com", pNum, msg[0:tEnd])
# 	      	    		msg = msg[tEnd+1:] # + 1 eliminates space from new string
#			limit = 150
#			time.sleep(9)
#		server.sendmail("tifmrp1324ip@gmail.com", pNum, msg)
#        else:
#		server.sendmail("tifmrp1324ip@gmail.com", pNum, msg)
#	return None

def sendMail(pNum, msg, carrier):
	if carrier == "verizon":
   		limit = 150
    		time.sleep(10)
		if len(msg) < limit:
    			server.sendmail("EMAIL@gmail.com", pNum, msg)
		        return None
		if len(msg) < 201: #for aesthetics 
			limit = 100
    		tEnd = limit - msg[limit:0:-1].find(" ")
    		if tEnd == limit+1:
	        	server.sendmail("EMAILp@gmail.com", pNum, msg[0:limit])
       		        return sendMail(pNum, msg[limit:], carrier)
   	        else:
			server.sendmail("EMAIL@gmail.com", pNum, msg[0:tEnd])
       		        return sendMail(pNum, msg[tEnd+1:], carrier)
	return None
