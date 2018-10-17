'''
  receiver.py
  Created by Yasin Kaya (selengalp), October 3, 2018.
'''
from xbee import xbee
import time

# default serial_port='/dev/ttyS0'
# default serial_baudrate=9600
# if your xbee configuraiton is different, initialize like below:
# node = xbee.XBee(serial_port='[your_value]',serial_baudrate=[your_value]) 
node = xbee.XBee()

# receive if any received message via XBee
while(1):
	if(node.serialAvailable()):
		message = node.receiveString()
		if(message):
			print(message)
