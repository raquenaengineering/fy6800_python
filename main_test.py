



from fy6800 import *
import time 




## get/set_serialport #
##func_gen.set_serialport(port)
#requested_port = (func_gen.get_serialport())
#print("Serial port of the functon generator: ")
#print(requested_port)

##autodetect serial port #
##port = func_gen.autodetect_port()


t = 0.5

# Basic setup to connect to the fy6800-------------------------------- #

def fy6800_setup():
    pass

# set/get wave type -------------------------------------------------- #

def set_get_wave_test():

    print("set/get wave")

    channel = 0
    success = func_gen.set_wave(channel,SINE)
    print("Succesful write? " + str(success))
    time.sleep(t)

    channel = 1
    func_gen.set_wave(channel,SINE)
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
    success = func_gen.set_wave(channel,SINE)
    print("Succesful write? " + str(success))
    time.sleep(t)

    channel = 1
    func_gen.set_wave(channel,SINE)
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
    success = func_gen.set_freq(channel,10)
    print("Succesful write? " + str(success))
    time.sleep(t)

    channel = 1
    func_gen.set_freq(channel,10)
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
    success = func_gen.set_ampl(channel,0.015)
    print("Succesful write? " + str(success))
    time.sleep(t)
    
    channel = 1
    success = func_gen.set_ampl(channel,0.015)
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
    success = func_gen.set_offs(channel,0)
    print("Succesful write? " + str(success))
    time.sleep(t)
    
    channel = 1
    success = func_gen.set_offs(channel,0)
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

# set/get Phase  -------------------------------------------------- #

def set_get_phase_test():
    print("set/get Phase")

    channel = 0
    success = func_gen.set_phas(channel,90)
    print("Succesful write? " + str(success))
    time.sleep(t)
    
    channel = 1
    success = func_gen.set_phas(channel,270)
    print("Succesful write? " + str(success))
    time.sleep(t)

    channel = 0
    phas = func_gen.get_phas(channel)
    print("Obtained Phase value: " + str(phas) + "º")
    time.sleep(t)
    
    channel = 1
    phas = func_gen.get_phas(channel)
    print("Obtained Phase value: " + str(phas) + "º")
    time.sleep(t)
    


# -------------------------------------------------------------------- #


if __name__ == "__main__":
    
    func_gen = fy6800()        ## useful to test autodetect
    #func_gen = fy6800(serial_port_name = "/dev/ttyUSB0")
    
    set_get_wave_test()        ## wave changing test
    set_get_freq_test()
    set_get_ampl_test()
    set_get_offset_test()
    
    set_get_phase_test()
    
    
    func_gen.print_params()





