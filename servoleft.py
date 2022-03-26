from Raspi_PWM_Servo_Driver import PWM
import time
import sys
pwm = PWM(0x6F)
servoMin = 50  # Min pulse length out of 4096
servo45 = 225
servoMid = 400
servo135 = 535
servoMax = 750
for i in range(servoMin, servoMax):
        pwm.setPWM(0, 0, i)
        time.sleep(0.0001)
while True:
        i=input()
        pwm.setPWM(0, 0, int(i))
        time.sleep(0.0001)