
# NOTE: \r\n are required as endline characters for the comminication to work
# NOTE: it seems a pause between change in channels is required for the changes to work properly
import serial
import serial.tools.list_ports

import time 

# WAVEFORM LIST:

sine = "0"
square = "1"
cmos = "2"
adj_pulse = "3"
dc = "4"
triangle = "5" 

# 0 : sine 
# 1: square
# 2: cmos
# 3: adj-pulse	Note: Requires second parameter WMSXX, maxval:4000000000 minval:10
# 4: dc 			Note: Requires second parameter WMP, 
# 5: triangle
# 6: ramp
# 7: neg-ramp
# 8: stair-trgl
# 9: stair-step
# 10: neg-stair
# 11: pos-exp
# 12: neg-exp
# 13: pos-fall-exp
# 14: neg-fall-exp
# 15: pos-log
# 16: neg-log
# 17: pos-fall-log
# 18: neg-fall-log
# 19: pos-full-wave
# 20: neg-full-wave
# 21: pos-half-wave
# 22: neg-half-wave
# 23: lorenz-pulse
# 24: multitone (what tones are used ???)
# 25: rand-noise (does the frequency parameter change anything here?)
# 26: ECG
# 27: trapezoid
# 28: sinc-puls
# 29: impulse
# 30: AWGN (what does this mean ???)
# 31: AM (amplitude modulated)
# 32: FM (freq-mod)
# 33: chirp (wtf is this???)
# 34: EMPTY
# 35: EMPTY

# GOES ON UNTIL 97 





class fy6800:
	
	# here all the INTERNAL VARIABLES for the classe fy6800 ############
	
	ser = serial.Serial()
	
	serial_port_name = None;	# has a variable called serial port, empty. 
	
	wave_a = None;		# current wave (only matching with device if not modified directly at the device )	
	wave_b = None;
	
	ampl_a = None;		# current wave (only matching with device if not modified directly at the device )	
	ampl_b = None;

	offs_a = None;		# current wave (only matching with device if not modified directly at the device )	
	offs_b = None;
	
	duty_a = None;		# current wave (only matching with device if not modified directly at the device )	
	duty_b = None;	



	# here all the METHODS for the classe fy6800 #######################
	
	# constructor with serial port defined manually # 
		 
	def __init__(self, serial_port_name):
			
		# if no port is given as a parameter, autodetect serial port 
		
		# if port is given as parameter, use it 
		self.serial_port = serial_port_name
		
		# open communication 
		self.serial_port = serial.Serial(self.serial_port_name) # assigns serial port
		
		
		# checks all serial ports
		# sends a message to check if there's a fy6800 connected
		# returns the first instance of a fy6800
		
		
	def __init__(self):
			
		# if no port is given as a parameter, autodetect serial port 
		
		# if port is given as parameter, use it 
		self.serial_port_name = self.autodetect_serialport()
		# open communication 
		self.serial_port = serial.Serial(self.serial_port_name) # assigns serial port
		
		
		# checks all serial ports
		# sends a message to check if there's a fy6800 connected
		# returns the first instance of a fy6800		
		
		
		
		
	def autodetect_serialport(self):			# for methods, self need to be always given as a parameter.
		
		serial_port = None
		ports = list(serial.tools.list_ports.comports())
		print(ports)
		print("---------------------------------------------------")
		for p in ports:
			print(p)
		print("---------------------------------------------------")
		port_names = []		# we store all port names in this variable
		for port in ports:
			port_names.append(port[0])	# here all names get stored
		print(port_names)
		print("---------------------------------------------------")

		for port_name in port_names:		# let's go through all ports
			try:
				ser = serial.Serial(		# serial constructor
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
					
				print (ser.name) 				# only for testing !!! 
				ser.write(b"UMO\n")
				ser.write(b"UMO\n")
				ser.write(b"UMO\n")
				ser.read_until(expected=LF, size=None)
				ser.write(b"UID\n")
				#print(ser.readln())
				# ser.write(b"WMW1\n")
				# ser.write(b"WMA1,000\n")
				# print("Channel 1 done")
				# time.sleep(1)
				# ser.write(b"WFW1\n")
				# ser.write(b"WFA1,000\n")
				# print("Channel 2 done")
				# print("String sent to function generator")
				# time.sleep(1)
				ser.close()
			except:
				print("Serial Port " + port_name + " Failed to open")
					
			ser.write(b"UMO\n")
			ser.write(b"UMO\n")
			ser.write(b"UMO\n")
			line = ser.readline()
			print("this is the line " + str(line))
			ser.write(b"UID\n")

	
		return serial_port
		
	def set_serialport(self, port):
		self.serial_port = port						# the port of this object, saves the value in port 
		
	def get_serialport(self):
		return(self.serial_port)
		
	# WAVE #
		
	def set_wave(self, channel, wave):
		if channel == 0:
			self.wave_a = wave;
			
		elif channel == 1:
			self.wave_b = wave;
			
		# add guards to be sure the wave value is between 0 and 97 ??? 
		
	def get_wave(self, channel):
		if channel == 0:
			return self.wave_a	
		elif channel == 1:
			return self.wave_b
		
		
	#AMPLITUDE#
	
	def set_ampl(self, channel, ampl):
		if channel == 0:
			self.ampl_a = ampl;
		elif channel == 1:
			self.ampl_b = ampl;
			
		# add guards to be sure the wave value is between 0 and 97 ??? 
		
	def get_ampl(self, channel):
		if channel == 0:
			return self.ampl_a	
		elif channel == 1:
			return self.ampl_b
			
	
	def set_offs(self):
		pass
		
	def set_duty(self):
		pass



	 
