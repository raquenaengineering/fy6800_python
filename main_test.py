



from fy6800 import *
import time 

func_gen = fy6800()


# get/set_serialport #
#func_gen.set_serialport(port)
requested_port = (func_gen.get_serialport())
print("Serial port of the functon generator: " + requested_port)


#autodetect serial port #
#port = func_gen.autodetect_port()


t = 0.5


# set/get wave type -------------------------------------------------- #

def set_get_wave_test():

    print("set/get wave")

    channel = 0
    success = func_gen.set_wave(channel,sine)
    print("Succesful write? " + str(success))
    time.sleep(t)

    channel = 1
    func_gen.set_wave(channel,sine)
    time.sleep(t)

    channel = 0
    wave = func_gen.get_wave(channel)
    print("Wave number is: " + wave)
    time.sleep(t)

    channel = 1
    wave = func_gen.get_wave(channel)
    print("Wave number is: " + wave)
    time.sleep(t)


    channel = 0
    success = func_gen.set_wave(channel,triangle)
    print("Succesful write? " + str(success))
    time.sleep(t)

    channel = 1
    func_gen.set_wave(channel,triangle)
    time.sleep(t)


    channel = 0
    wave = func_gen.get_wave(channel)
    print("Wave number is: " + wave)
    time.sleep(t)

    channel = 1
    wave = func_gen.get_wave(channel)
    print("Wave number is: " + wave)
    time.sleep(t)

# set/get frequency -------------------------------------------------- #

def set_get_freq_test():
    print("set/get frequency")

    channel = 0
    success = func_gen.set_freq(channel,50.50)
    print("Succesful write? " + str(success))
    time.sleep(t)

    channel = 1
    func_gen.set_freq(channel,0.4)
    time.sleep(t)
    
    channel = 0
    freq = func_gen.get_freq(channel)
    print("Frequency channel " + str(channel) + ": " + str(freq) + "Hz")
    time.sleep(t)

    channel = 1
    freq = func_gen.get_freq(channel)
    print("Frequency channel " + str(channel) + ": " + str(freq) + "Hz")
    time.sleep(t)


# set/get Amplitude  -------------------------------------------------- #

def set_get_ampl_test():
    print("set/get Amplitude")

    channel = 0
    success = func_gen.set_ampl(channel,0.0042)
    print("Succesful write? " + str(success))
    time.sleep(t)
    
    channel = 1
    success = func_gen.set_ampl(channel,1.90)
    print("Succesful write? " + str(success))
    time.sleep(t)

    channel = 0
    ampl = func_gen.get_ampl(channel)
    print("Obtained amplitude value: " + str(ampl) + "V")
    time.sleep(t)
    
    channel = 1
    ampl = func_gen.get_ampl(channel)
    print("Obtained amplitude value: " + str(ampl) + "V")
    time.sleep(t)
    

# set/get Offset  -------------------------------------------------- #

def set_get_offset_test():
    print("set/get Offset")

    channel = 0
    success = func_gen.set_offs(channel,-5)
    print("Succesful write? " + str(success))
    time.sleep(t)
    
    channel = 1
    success = func_gen.set_offs(channel,-0.001)
    print("Succesful write? " + str(success))
    time.sleep(t)

    channel = 0
    ampl = func_gen.get_offs(channel)
    print("Obtained offset value: " + str(ampl) + "V")
    time.sleep(t)
    
    channel = 1
    ampl = func_gen.get_offs(channel)
    print("Obtained offset value: " + str(ampl) + "V")
    time.sleep(t)
# -------------------------------------------------------------------- #


if __name__ == "__main__":
    
    #set_get_wave_test()        ## wave changing test
    #set_get_freq_test()
    set_get_ampl_test()
    set_get_offset_test()
    
    
    func_gen.print_params()

## amplitude get set testing ##

# channel = 0;
# func_gen.set_ampl(channel, 0.010)
# time.sleep(t)


# channel = 1;
# func_gen.set_ampl(channel, 0.010)
# time.sleep(t)


## frequency get set testing ##

# channel = 0;
# func_gen.set_freq(channel, 100)
# time.sleep(t)


# channel = 1;
# func_gen.set_freq(channel, 100)
# time.sleep(t)


#req_wave = func_gen.get_wave(channel)

# channel = 1
# func_gen.set_wave(channel,triangle)
# req_wave = func_gen.get_wave(channel)
# print("Wave on port " + str(channel) + ": " + req_wave)

# modify get/set to return the name of the wave, instead of its number.  (tuples ???)

#set/get amplitude#

# channel = 0
# ampl = 0.01
# func_gen.set_ampl(channel,ampl)
# req_ampl = func_gen.get_ampl(channel)
# print("Amplitude on port " + str(channel) + ": " + str(req_ampl))

# channel = 1
# ampl = 1
# func_gen.set_ampl(channel,ampl)
# req_ampl = func_gen.get_ampl(channel)
# print("Amplitude on port " + str(channel) + ": " + str(req_ampl))




