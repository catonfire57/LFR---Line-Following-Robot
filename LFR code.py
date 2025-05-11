from machine import Pin, PWM
import time

# Motor direction pins
motorrightrev = Pin(10, Pin.OUT)
motorrightfor = Pin(11, Pin.OUT)
motorleftfor = Pin(12, Pin.OUT)
motorleftrev = Pin(13, Pin.OUT)
ledright = Pin(22, Pin.OUT)
ledleft = Pin(21, Pin.OUT)
enable1 = PWM(Pin(6))
enable2 = PWM(Pin(7))
enable1.freq(1000)
enable2.freq(1000)
enable1.duty_u16(50525)
enable2.duty_u16(50525) #Ofcourse the speed can be changed the motors and duty play an important role...

# IR sensor pins (not used yet in logic)
right_ir = Pin(2, Pin.IN)
left_ir = Pin(4, Pin.IN)

# Safe startup: Stop all motors first
motorrightfor.low()
motorrightrev.low()
motorleftfor.low()
motorleftrev.low()

time.sleep(1)

def forward():

    motorrightfor.high()
    motorrightrev.low()
    motorleftfor.high()
    motorleftrev.low()
    
def reverse():
    motorrightfor.low()
    motorrightrev.high()
    motorleftfor.low()
    motorleftrev.high()
    
def rightturn():
    motorrightfor.low()
    motorrightrev.low()
    motorleftfor.high()
    motorleftrev.low()
    
def leftturn():
    motorrightfor.high()
    motorrightrev.low()
    motorleftfor.low()
    motorleftrev.low()

def stop():
    motorrightfor.low()
    motorrightrev.low()
    motorleftfor.low()
    motorleftrev.low()


while True:
    right_val=right_ir.value() #Getting right IR value(0 or 1)
    left_val=left_ir.value() #Getting left IR value(0 or 1)
    
    # Controlling robot direction based on IR value
    if right_val==0 and left_val==0:
        forward()
        ledright.high()
        ledleft.high()
    elif right_val==1 and left_val==0:
        rightturn()
        ledright.high()
        ledleft.low()
        time.sleep(0.2)
    elif right_val==0 and left_val==1:
        leftturn()
        ledleft.high()
        ledright.low()
        time.sleep(0.2)
    else:
        forward()
        ledright.high()
        ledleft.high()
        
