from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import atexit
class hatmotor:
    def __init__(self, address, m1, m2):
        self.mh = Raspi_MotorHAT(addr=address)
        self.m1=m1
        self.m2=m2
        self.myMotor = self.mh.getMotor(self.m1)
        self.myMotor2 = self.mh.getMotor(self.m2)
    def forward(self, speed):
        self.myMotor.setSpeed(speed)
        self.myMotor2.setSpeed(speed)
        self.myMotor.run(Raspi_MotorHAT.FORWARD)
        self.myMotor2.run(Raspi_MotorHAT.FORWARD)
    def backward(self, speed):
        self.myMotor.setSpeed(speed)
        self.myMotor2.setSpeed(speed)
        self.myMotor.run(Raspi_MotorHAT.BACKWARD)
        self.myMotor2.run(Raspi_MotorHAT.BACKWARD)
    def stop(self):
        self.myMotor.setSpeed(0)
        self.myMotor2.setSpeed(0)
        self.myMotor.run(Raspi_MotorHAT.RELEASE)
        self.myMotor2.run(Raspi_MotorHAT.RELEASE)