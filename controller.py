from pyfirmata import Arduino, SERVO,util
port='COM8'

pin=10 # servo
led_pin = 11 #led
print("check")
board=Arduino(port)
board.digital[pin].mode=SERVO

def rotateServo(pin,angle):
    board.digital[pin].write(angle)
def servocontrol(val):
    if val==1:
        rotateServo(pin, 90)
        board.digital[led_pin].write(1)  
    elif val==0:
        rotateServo(pin, 0)
        board.digital[led_pin].write(0)  