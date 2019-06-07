



from fy6800 import *




func_gen = fy6800()


# get/set_serialport #
#func_gen.set_serialport(port)
requested_port = (func_gen.get_serialport())
print("Serial port of the functon generator: " + requested_port)


#autodetect serial port #
#port = func_gen.autodetect_port()


# set/get wave type #

channel = 0
func_gen.set_wave(channel,sine)
req_wave = func_gen.get_wave(channel)
print("Wave on port " + str(channel) + ": " + req_wave)

channel = 1
func_gen.set_wave(channel,triangle)
req_wave = func_gen.get_wave(channel)
print("Wave on port " + str(channel) + ": " + req_wave)

# modify get/set to return the name of the wave, instead of its number.  (tuples ???)

#set/get amplitude#

channel = 0
ampl = 0.01
func_gen.set_ampl(channel,ampl)
req_ampl = func_gen.get_ampl(channel)
print("Amplitude on port " + str(channel) + ": " + str(req_ampl))

channel = 1
ampl = 1
func_gen.set_ampl(channel,ampl)
req_ampl = func_gen.get_ampl(channel)
print("Amplitude on port " + str(channel) + ": " + str(req_ampl))




