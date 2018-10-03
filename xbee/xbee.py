'''
  Sixfab_RPi_Xbee_Library 
  -
  Library for Sixfab RPi Xbee Shield.
  -
  Created by Yasin Kaya (selengalp), October 3, 2018.
'''

import time
import serial
import RPi.GPIO as GPIO

# global variables
TIMEOUT = 3 # seconds
ser = serial.Serial()

###########################################
### Private Methods #######################
###########################################

# function for printing debug message 
def debug_print(message):
	print(message)

# function for getting time as miliseconds
def millis():
	return int(time.time())

# function for delay as miliseconds
def delay(ms):
	time.sleep(float(ms/1000.0))

###########################################
### XBee Class ############################
###########################################	
class XBee:
	board = "" # shield name
	timeout = TIMEOUT # default timeout for function and methods on this library.
	
	def __init__(self, serial_port="/dev/ttyS0", serial_baudrate=9600, board="Sixfab Xbee Shield"):
		
		self.board = board
    	
		ser.port = serial_port
		ser.baudrate = serial_baudrate
		ser.parity=serial.PARITY_NONE
		ser.stopbits=serial.STOPBITS_ONE
		ser.bytesize=serial.EIGHTBITS
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
			
		debug_print(self.board + " Class initialized!")

	def sendString(self, compose):
		if (ser.isOpen() == False):
			ser.open()		
		ser.reset_input_buffer()
		ser.write(compose.encode())
		debug_print(compose)

	def receiveString(self):
		response = ""
		while(ser.inWaiting()):
			response += ser.read(ser.inWaiting()).decode('utf-8')
		return response