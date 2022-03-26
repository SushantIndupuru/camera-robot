"""from Raspi_PWM_Servo_Driver import PWM
import time
pwm = PWM(0x6F)
servoMin = 50  # Min pulse length out of 4096
servo45 = 225
servoMid = 400
servo135 = 535
servoMax = 750 # Max pulse length out of 4096
pwm.setPWMFreq(60)
while True:
    print("Left")
    for i in range(servoMin, servoMax):
        pwm.setPWM(0, 0, i)
        time.sleep(0.0001)
    print("Right")
    for i in reversed(range(servoMin, servoMax)):
        pwm.setPWM(0, 0, i)
        time.sleep(0.0001)"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(17, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(7.5) # turn towards 90 degree
        time.sleep(1) # sleep 1 second
        p.ChangeDutyCycle(2.5) # turn towards 0 degree
        time.sleep(1) # sleep 1 second
        p.ChangeDutyCycle(12.5) # turn towards 180 degree
        time.sleep(1) # sleep 1 second
except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()