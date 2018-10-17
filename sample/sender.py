'''
  sender.py
  Created by Yasin Kaya (selengalp), October 3, 2018.
'''
from xbee import xbee
import time

# default serial_port='/dev/ttyS0'
# default serial_baudrate=9600
# if your xbee configuraiton is different, initialize like below:
# node = xbee.XBee(serial_port='[your_value]',serial_baudrate=[your_value]) 
node = xbee.XBee()

counter = 0

# send a message every 3 seconds
while(1):
	message = "hello " + str(counter)
	node.sendString(message)
	counter += 1
	time.sleep(3)

