



from fy6800 import *



func_gen = fy6800()


port = "COM8"			# fixed com port for testing purposes 

func_gen.set_serialport(port)

requested_port = (func_gen.get_serialport())

print(requested_port)

#port = func_gen.autodetect_port()


