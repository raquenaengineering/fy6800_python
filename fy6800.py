

import serial




class fy6800:
	
	# here all the INTERNAL VARIABLES for the classe fy6800 ############
	
	serial_port = None;	# has a variable called serial port, empty. 
	
	wave_a = None;		# current wave (only matching with device if not modified directly at the device )	
	wave_b = None;
	
	ampl_a = None;		# current wave (only matching with device if not modified directly at the device )	
	ampl_b = None;

	offs_a = None;		# current wave (only matching with device if not modified directly at the device )	
	offs_b = None;
	
	duty_a = None;		# current wave (only matching with device if not modified directly at the device )	
	duty_b = None;	



	# here all the METHODS for the classe fy6800 #######################
	
	# constructor
		
	def __init__(self):
		pass;

	
	
	# checks all serial ports
	# sends a message to check if there's a fy6800 connected
	# returns the first instance of a fy6800
	
	def autodetect_serialport(self):			# for methods, self need to be always given asa parameter.
	
		serial_port = None;
		return serial_port;
		
	def set_serialport(self, port):
		self.serial_port = port;						# the port of this object, saves the value in port 
		
	def get_serialport(self):
		return(self.serial_port)
		
	def set_wave(self):
		pass
		
		
	def set_ampl(self):
		pass
	def set_offs(self):
		pass
		
	def set_duty(self):
		pass



	 
