from Raspi_PWM_Servo_Driver import PWM
from camera import VideoCamera
from hatmotor import hatmotor
import json
import subprocess
import time
servoMin = 50  # Min pulse length out of 4096
servo45 = 225
servoMid = 400
servo135 = 535
servoMax = 750