from machine import Pin
import utime

class SteppMotor4:
    __pos = 500000
    _stepps = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]]
    __run = True
    __timestamp = utime.ticks_ms()
    __speed = 100
    __direction = -1
    __min = 1
    __max = -1
    __init = True
    __angle = 0

    def __init__(self, pin1=13, pin2=12, pin3=14, pin4=27, pinE=34):
        self.__pins = [0, 1, 2, 3]
        self.__pins[0] = Pin(pin1, mode=Pin.OUT)
        self.__pins[1] = Pin(pin2, mode=Pin.OUT)
        self.__pins[2] = Pin(pin3, mode=Pin.OUT)
        self.__pins[3] = Pin(pin4, mode=Pin.OUT, pull=Pin.PULL_DOWN)
        self.pinE = Pin(pinE, mode=Pin.IN)

    def __loopInit__(self):

        if self.pinE.value() == 1:
            if self.__min == 1 and self.__max == -1:
                self.__pos = 0
                self.__min = 0
                self.__direction = 1
                print('__min=0', ' ', self.__direction)
            elif self.__min == 0 and self.__max == -1 and self.__pos > 200:
                self.__max = self.__pos
                self.__direction = -1
                print('__max=', self.__max, ' ', self.__direction)
                self.setAngle(180)
                self.__init = False
        self.__pos += self.__direction

    def __loopAngle__(self):
        if self.__pos > self.__max/(360/self.__angle):
            self.__pos += -1
        else:
            self.__pos += 1
        if int(self.__pos) == int(self.__max/(360/self.__angle))and self.__run:
            self.stop()
            print(self.getAngle())

    def setAngle(self, angle):
        self.start()
        self.__angle = angle

    def getAngle(self):
        return self.__pos/self.__max*360

    def stop(self):
        self.__run = False
        for i in range(len(self.__pins)):
            self.__pins[i].value(0)

    def start(self):
        self.__run = True

    def loop(self):
        if self.__timestamp+((1/self.__speed)*1000)/len(self._stepps) <= utime.ticks_ms():
            self.__timestamp = utime.ticks_ms()
            if self.__init:
                self.__loopInit__()
            else:
                self.__loopAngle__()

            if self.__pos < 200:
                self.__direction = 1
            if self.__pos > self.__max-200 and self.__max > 0:
                self.__direction = -1

            if self.__run:
                for i in range(len(self.__pins)):
                    self.__pins[i].value(
                        self._stepps[self.__pos % len(self._stepps)][i])


class SteppMotor8(SteppMotor4):
    _stepps = [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [
        0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1]]

