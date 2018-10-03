'''
  sender.py
  Created by Yasin Kaya (selengalp), October 3, 2018.
'''
from xbee import xbee
import time

node = xbee.XBee()
# send a message every 3 seconds
while(1):
	message = "hello " + str(counter)
	node.sendString(message)
	counter++
	time.sleep(3)

