# UDP Pinger

# Must server running before you can run the UDP Pinger Client code

import random
from socket import *
import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(1)

data = "Client connected"

for i in range(10):
	Ts = time.time()
	clientSocket.sendto(data, ('127.0.0.1', 12000))
	try:
		message, addr = clientSocket.recvfrom(1024)
		Tr = time.time()
		print("Packet no. : "+str(i)+'  '+message.upper()+'	'+'RTT = '+str(Tr-Ts))
    	except timeout:
		print("Packet no. "+str(i)+" lost")	
