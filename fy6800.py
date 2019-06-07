
# NOTE: \r\n are required as endline characters for the comminication to work
# NOTE: it seems a pause between change in channels is required for the changes to work properly
import serial
import serial.tools.list_ports

import time 
import logging 	# an attempt to make debuggin easier 
logging.basicConfig(level=logging.DEBUG)		# enable debug messages
separator = "---------------------------------------------------"	# to separate debugging messages

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
	
	serial_port = serial.Serial()		# variable storing a serial port object, used for communication 
	
	serial_port_name = None;			# stores serial port name
	
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
		self.serial_port = serial.Serial(		# serial constructor
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
							exclusive=None
							)
		
		# checks all serial ports
		# sends a message to check if there's a fy6800 connected
		# returns the first instance of a fy6800
		
		
	def __init__(self):
		logging.debug("Init")
		# if no port is given as a parameter, autodetect serial port 
		# if port is given as parameter, use it 
		self.serial_port_name = self.autodetect_serialport()
		# open communication 
		logging.debug("opening the port with the name obtained with autodetect")
		# open communication 
		self.serial_port = serial.Serial(		# serial constructor
							port=self.serial_port_name, 
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
							exclusive=None
							)		
		logging.debug("open success")
		
		# checks all serial ports
		# sends a message to check if there's a fy6800 connected
		# returns the first instance of a fy6800		
		
		
		
		
	def autodetect_serialport(self):			# for methods, self need to be always given as a parameter.
		
		logging.debug('Running autodetect_serialport')
		serial_port = None
		ports = list(serial.tools.list_ports.comports())
		for p in ports:
			logging.debug(p)
		logging.debug("---------------------------------------------------")
		port_names = []		# we store all port names in this variable
		for port in ports:
			port_names.append(port[0])	# here all names get stored
		logging.debug(port_names)
		logging.debug("---------------------------------------------------")

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
					exclusive=None
					)
				print("Serial Port " + port_name + " Open succesfuly")
			except:
				print("Serial Port " + port_name + " Failed to open")	
				ser.close()

				
			# try to get device name, if works, function generator connected	
			ser.write(b"UMO\r\n")			# asks for the device name sometimes gives problems, ask 3 times
			ser.write(b"UMO\r\n")
			ser.write(b"UMO\r\n")
			dev_name = ser.readline()
			dev_name = str(dev_name)
			logging.debug("this is the device name " + str(dev_name))
			if(dev_name.find("FY6800-40M") != -1):		## put the name of the device somewhere else
				print("device found at " + port_name + " serial port")
				ser.close()							# we will open the port creating a new serial object belinging to the class, so we close it here
				return port_name


		
	def set_serialport(self, port):
		self.serial_port = port						# the port of this object, saves the value in port 
		
	def get_serialport(self):
		return(self.serial_port_name)
		
	# WAVE #
	
	def set_wave(self, channel, wave):
		if channel == 0:
			message = "WMW"							# command to change weave channel 1
			message = message + wave				# wave number
			message = message + "\r\n"				# EOL, needed.
			logging.debug("This is the message:" + str(message))
			logging.debug("sending message to serial")
			self.serial_port.write(bytes(message,'utf-8'))
			self.wave_a = wave;
			
		elif channel == 1:
			pass
	
	
	def get_wave(self, channel):
		if channel == 0:
			logging.debug("receiving message")
			self.serial_port.write(b"RMW\r\n")
			self.wave_a = self.serial_port.readline()				
			logging.debug("returned wave: " + str(self.wave_a))
			return self.wave_a	
		elif channel == 1:
			pass

			
		# add guards to be sure the wave value is between 0 and 97 ??? 
		

		
		
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



	 
