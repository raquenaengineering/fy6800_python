



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
    success = func_gen.set_wave(channel,triangle)
    print("Succesful write? " + str(success))
    time.sleep(t)

    channel = 1
    func_gen.set_wave(channel,square)
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

# set/get frequency -------------------------------------------------- #

def set_get_freq_test():
    print("set/get frequency")

    channel = 0
    success = func_gen.set_freq(channel,100)
    print("Succesful write? " + str(success))
    time.sleep(t)

    channel = 1
    func_gen.set_freq(channel,0.5)
    time.sleep(t)

# -------------------------------------------------------------------- #

if __name__ == "__main__":
    
    #set_get_wave_test()        ## wave changing test
    set_get_freq_test()
    

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




