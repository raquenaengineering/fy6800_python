
# NOTE: \r\n are required as endline characters for the comminication to work
# NOTE: it seems a pause between change in channels is required for the changes to work properly
# NOTE: The fy6800 always replies with a b'/n' (EOL) character to every command, so:
	# - either flush the input before every read	--> we will start here
	# - read the input after every write, and use this as an ACK --> use this in the future
	
# NOTE: the wave adj-puls doesn't exist for channel 2, so this generates an offset in the naming of the 
		# waves, so when ch2 is > 3, wave number = wave number -1		FIX THIS !!! 	
	
import serial
import serial.tools.list_ports

import time 
import logging 	# an attempt to make debuggin easier 
logging.basicConfig(level=logging.DEBUG)		# enable debug messages
separator = "---------------------------------------------------"	# to separate debugging messages

# WAVEFORM LIST:

sine = 0
square = 1
cmos = 2
adj_pulse = 3
dc = 4
triangle = 5 

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
	
	freq_a = None;		# current wave (only matching with device if not modified directly at the device )	
	freq_b = None;
	
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
		
		
	# prints all current parameters of the function generator
		
	def print_params(self):
		
		print("Serial Port: ")
		print(self.serial_port_name)
		# waves #
		print("Wave Channel A: ")
		print(self.wave_a)
		print("Wave Channel B: ")
		print(self.wave_b)
		#frequency#
		print("Frequency Channel A: ")
		print(self.freq_a)
		print("Frequency Channel B: ")
		print(self.freq_b)			
		#Amplitude#
		print("Amplitude Channel A: ")
		print(self.ampl_a)	
		print("Amplitude Channel B: ")
		print(self.ampl_b)			
		#Offset#
		print("Offset Channel A: ")
		print(self.offs_a)	
		print("Offset Channel B: ")
		print(self.offs_b)	
		#Duty#
		print("Duty Channel A: ")
		print(self.duty_a)	
		print("Duty Channel B: ")
		print(self.duty_b)			

		
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
		
		# Note: not all the ports are valid options, so we could discard the that aren't interesting USING THE DESCRIPTION!
		port_descs = []
		for port in ports:
			port_descs.append(port[1])
		logging.debug(port_descs)
		logging.debug("---------------------------------------------------")
		
		
		port_names = [] # destroy al previously printed port names, get only the ones that match description 
		for port in ports:
			port_desc = port[1]
			if(port_desc.find("USB-SERIAL CH340") != -1):	# WINDOWS DESCRIPTION FOR CH340
				port_names.append(port[0])	# here all names get stored
			if(port_desc.find("USB2.0-Serial") != -1):		# LINUX DESCRIPTION FOR CH340
				port_names.append(port[0])	# here all names get stored
		logging.debug(port_names)
		logging.debug("---------------------------------------------------")

		# Note:	use a timeout to avoid the serial detection to get stuck !!!
			

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
		
		
	#NOTE: POSSIBLE TO WRITE AN EVEN MORE GENERIC FUNCTION FOR ALL COMMANDS
	# it will only need to replace the 'W' parameter for the 'R', so it 
	# will be useful for all commands RELATED WITH OUTPUT
	# this MIGHT NOT WORK, because read commands need to wait for the returned data.
	# PLEASE READ THE FY6800 COMMAND TABLE FOR MORE INFORMATION
	
		
	# ~ #NOTE: GENERIC FUNCTION FOR ALL SET, AND GET#
	# ~ most of the commands are doing almost the same,
	# ~ so it's possible to create a common implementation for 
	# ~ most of them together, the implementation will be similar to this:
	
	
	# channel: type - integer: 0 or 1, only channel options
	# param_name: type - UNICODE character, parameter to read/write to
	# param_value: type - UNICODE character, value to write to the choosen parameter
	
	# RETURN VALUE: WRITE SUCCESSFUL 0
	# 				WRITE FAIL -1
	
	# How to know if write success: read a '\n'
	
	def set_param(self,channel,param_name,param_value):
		if channel == 0:
			chan = "M"
		elif channel == 1:
			chan = "F"
		else:
			print("ERROR: WRONG CHANNEL INDEX")					# HANDLE SOMEWHERE ELSE ???
		message = 'W' + chan + param_name + str(param_value) 	# w indicates writing
		message = message + "\r\n"				# EOL, needed.
		logging.debug("This is the SENT message:" + str(message))
		self.serial_port.write(bytes(message,'utf-8'))
		
		response = self.serial_port.readline()
		logging.debug("This is the response of the function generator: " + str(response))
		if(response == b'\n'):	# the function generator always responses with b'\n' on succesful write
			success = True		
		else:
			success = False
			
		return(success)


	# RETURN VALUE: TYPE-UNICODE_STRING: parameter read from function generator

	def get_param(self,channel,param_name):
		logging.debug("Channel number is " + str(channel))
		if channel == 0:
			chan = "M"
		elif channel == 1:
			chan = "F"
		else:
			print("ERROR: WRONG CHANNEL INDEX")	# HANDLE SOMEWHERE ELSE ???
		message = 'R' + chan + param_name 	 	# w indicates writing
		message = message + "\r\n"				# EOL, needed.
		logging.debug("This is the SENT message:" + str(message))
		# REQUEST THE PARAMETER #
		self.serial_port.write(bytes(message,'utf-8'))
		# READ THE REQUESTED PARAMETER #
		# self.serial_port.reset_input_buffer() NOT NEEDED !!! DELETE IF WORKING FINE
		param_value = self.serial_port.readline()	# first returned character is always '\n', so we need to read two lines
		logging.debug("This is the RECEIVED message:" + str(param_value))
		logging.debug("This is its type:")
		logging.debug(type(param_value))
		param_value = param_value.decode('utf8')		# converting binary value into UNICODE STRING
		param_value = param_value.strip('\n')			# removing the END OF LINE character
		logging.debug("This is the DECODED message:" + param_value)
		logging.debug("This is its type")
		logging.debug(type(param_value))
		
		response = self.serial_port.readline()
		logging.debug(str(response))
						
		return param_value		# the return parameter is always a UNICODE string !!!
	
		
	# WAVE #
	
	
	def set_wave(self, channel, wave):
		
		#ADD GUARDS TO THE POSSIBLE VALUES, FOR EACH COMMAND#
		# EXAMPLE:
		#- Wave is between 0 and 97
		#- Amplitude is between 0.0000001 and 10
		#- duty is between 0 and 100
		
		logging.debug("set wave ----------------------------------------------")
		
		# fixing STUPID wave offset problem between channels
		
		if(wave == 3 and channel == 1):
			print("Channel B has no adjustable pulse wave available, SEE SPECS !!!")
			return(False)
			
		if(wave > 3 and channel == 1):
			wave = wave - 1
		
		success = self.set_param(channel,'W',wave)	# returns true if succesful write
		if channel == 0:
			self.wave_a = wave	# wrong !!!
		elif channel == 1:
			self.wave_b = wave
		else:
			print("Selected channel not available");
			print("Options are 0 and 1")
				
		return(success)


	
	def get_wave(self, channel):
		
		logging.debug("get wave ----------------------------------------------")

		wave = None					# wave we get back
		wave = self.get_param(channel,'W')
		if channel == 0:
			self.wave_a = wave
			logging.debug("Wave in channel 0 = " + self.wave_a)
			return self.wave_a
		elif channel == 1:
			self.wave_b = wave
			logging.debug("Wave in channel 1 = " + self.wave_b)
			return self.wave_b
		# owful implementation, improve this !!!
		# add guards to be sure the wave value is between 0 and 97 ??? 
		
		
		
	#FREQUENCY#
	
	def format_freq(self,freq):
				
		## formatting the string to meet the requirements of the func.gen
		## change this to a function ??? YES, WILL BE USED MORE THAN ONCE
		
		# "{:(zero padding)(total number of digits).(digits after comma)}"
		freq_string =("{:015.6f}".format(freq))
		freq_string = freq_string.replace('.','')
		logging.debug("The formatted freq_string is:	" + freq_string)
		return(freq_string)
    
	
	def set_freq(self, channel, freq):
		# NOTE: This is always the format for the frequency value "00000010(,)000000" the comma is NOT needed
		logging.debug("set frequency ----------------------------------------------")
		
		if (freq > 40000000) or (freq < 0):		# guards to limit the input value range	# NEEDS TO BE CHANGEABLE !!!
			print("Frequency value out of range!!! (0.0000001 -- 40.000.000)")
			return(False)						# we will not set freq if out of range, and we return fail

		freq_string = self.format_freq(freq)	# formatting the string to meet the requirements of the func.gen

		
		success = self.set_param(channel,'F',freq_string)	# returns true if succesful write
		if channel == 0:
			self.freq_a = freq
		elif channel == 1:
			self.freq_b = freq

		return(success)								# return if setting frequency was succesful
		
	def get_freq(self, channel):
		logging.debug("get frequency  ----------------------------------------------")

		freq = None					# wave we get back
		freq = self.get_param(channel,'F')
		
		# converting back string to integer number#
		freq = float(freq)
		if channel == 0:
			self.freq_a = freq
			logging.debug("Frequency in channel 0 = " + str(self.freq_a))
			return self.freq_a
		elif channel == 1:
			self.freq_b = freq
			logging.debug("Frequency in channel 1 = " + str(self.freq_b))
			return self.freq_b

		
	# #AMPLITUDE#
	
	def set_ampl(self, channel, ampl):
		logging.debug("set amplitude ----------------------------------------------")
		# NOTE: THE ORIGINAL SOFTWARE DOESN'T WORK PROPERLY !!!!
		# It only allows you to set integer amplitude values by serial
		# probably because the separator is a ',', instead of a '.' (this software uses the .)
		
		# NOTE: THE FIRMWARE MAY ALSO BE BROKEN, NOT POSSIBLE AMPLITUDES BELOW 0.001 
		# (0.0001 is selectable directly using the machine knobs)
		# using a number with not only zeroes it works !!!
		# example: 1.2405V
		# 0.0045 is a value the device doesn't like, it always gets 0.0044 instead !!!
		# (not tested if indeed working)
		

		if (ampl > 20) or (ampl < 0):			# guards to limit the input value range	# NEEDS TO BE CHANGEABLE !!!
			print("Amplitude value out of range!!! (0.001 -- 20) *1:read note in code")
			return(False)						# we will not set freq if out of range, and we return fail

		ampl_string = str(ampl)					# this is all formatting needed for the amplitude
		
		success = self.set_param(channel,'A',ampl_string)	# returns true if succesful write
		if channel == 0:
			self.ampl_a = ampl
		elif channel == 1:
			self.ampl_b = ampl

		return(success)								# return if setting frequency was succesful
		
	def get_ampl(self, channel):
		logging.debug("get amplitude ----------------------------------------------")
		if channel == 0:
			ampl = self.get_param(0, 'A')
			ampl = float(ampl) 			# convert the amplitude to a floating value
			ampl = ampl/10000				# put the decimals at the right place
			self.ampl_a = ampl
			return self.ampl_a
		elif channel == 1:
			ampl = self.get_param(1, 'A')
			ampl = float(ampl)				# convert to float
			ampl = ampl/10000				# numbers returned are always 4 decimal digits swapped
			self.ampl_b = ampl
			return self.ampl_b
	
	
	
	def set_offs(self,channel,offs):
		logging.debug("set Offset ----------------------------------------------")
		
		if (offs > 10) or (offs < -10):			# guards to limit the input value range	# NEEDS TO BE CHANGEABLE !!!
			print("Offset value out of range!!! [-10:10] (|offs|>0.001) *2:read note in code")
			return(False)						# we will not set freq if out of range, and we return fail

		offs_string = str(offs)					# this is all formatting needed for the amplitude
		
		success = self.set_param(channel,'O',offs_string)	# returns true if succesful write
		if channel == 0:
			self.offs_a = offs
		elif channel == 1:
			self.offs_b = offs

		return(success)								# return if setting frequency was succesful		
		
	def get_offs(self,channel):
		logging.debug("Get Offset ----------------------------------------------")
		if channel == 0:
			offs = self.get_param(0, 'O')
			offs = float(offs) 			# convert the OFFSET to a floating value
			offs = offs/1000				# put the decimals at the right place
			self.offs_a = offs
			return self.offs_a
		elif channel == 1:
			offs = self.get_param(1, 'O')
			offs = float(offs)				# convert to float
			offs = offs/1000				# numbers returned are always 4 decimal digits swapped
			self.offs_b = offs
			return self.offs_b		
		
		
		
		
	# def set_duty(self):
		# pass



	 
