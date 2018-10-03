'''
  receiver.py
  Created by Yasin Kaya (selengalp), October 3, 2018.
'''
from xbee import xbee
import time

node = xbee.XBee()

# receive if any received message via XBee
while(1):
	message = node.receiveString()
	if(message):
		print(message)