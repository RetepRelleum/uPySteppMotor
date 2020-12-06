
import machine 
import utime
import random
import math




class DAC:
    __timestamp = utime.ticks_ms()
    __frequenz=50
    __fs=2000
    def __init__(self,port, bits=8, *, buffering=None):
        p=machine.Pin(port)
        self.d=machine.DAC(p)

    def loop(self):
        if self.__timestamp+1/(self.__fs/1000) <= utime.ticks_ms():
            self.__timestamp = utime.ticks_ms()   
            self.d.write(30+int(25*math.sin(2*math.pi*self.__timestamp/1000*self.__frequenz)))
            print(self.__timestamp/1000,' ',30+int(25*math.sin(2*math.pi*self.__timestamp/1000*self.__frequenz)))


d=DAC(26)

while True:
    d.loop()


# %%
