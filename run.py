
from  steppMotor.SteppMotor import SteppMotor8

a = SteppMotor8()
b = SteppMotor8(pin1=15, pin2=2, pin3=0, pin4=4, pinE=13)

while True:
    b.loop()
    a.loop()



