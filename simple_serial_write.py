

import serial
import time 


port_name = "COM11"
ser = serial.Serial(
	port=port_name, 
	baudrate=115200, 
	#bytesize=EIGHTBITS, 
	#parity=PARITY_NONE, 
	#stopbits=STOPBITS_ONE, 
	timeout=None, 
	xonxoff=False, 
	rtscts=False, 
	write_timeout=None, 
	dsrdtr=False, 
	inter_byte_timeout=None, 
	exclusive=None)

#ser.baudrate = 115200			# it's correct, checked with the datasheet 
#ser.port = port_name
#print(ser.name)
#ser.open()
print("Is the port open?")
print(ser.is_open)
time.sleep(1)
ser.write(b"WMA1,00\n")
time.sleep(1)
ser.close
