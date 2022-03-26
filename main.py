from flask import Flask, render_template, Response, request
from Raspi_PWM_Servo_Driver import PWM
from camera import VideoCamera
from hatmotor import hatmotor
import json
import subprocess
import time
import sys
pi_camera = VideoCamera(flip=False)
servoMin = 192  # Min pulse length out of 4096
servo45 = 225
servoMid = 400
servo135 = 535
servoMax = 641
servoHorizontalAngle = 400
servoVerticalAngle = 400
robby = hatmotor(0x6f, 1, 2)
pwm = PWM(0x6F)
pwm.setPWMFreq(60)
pwm.setPWM(0, 0, servoMid)
pwm.setPWM(1, 0, servoMid)
pwm.setPWM(14, 0, servoMid)
pwm.setPWM(15, 0, servoMid)
ma = 400
moving=None
def motorforward():
    if moving!="forward":
        robby.forward(200)
def motorbackward():
    if moving !="backward":
        robby.backward(200)
def motorleft():
    global ma
    
    if ma==400:
        pwm.setPWM(0, 0, servo135)
        pwm.setPWM(1, 0, servo135)
        ma=535
def motorright():
    global ma
    if ma==400:
        pwm.setPWM(0, 0, servo45)
        pwm.setPWM(1, 0, servo45)
        ma = 225
def motorreset():
    global ma
    pwm.setPWM(0, 0, servoMid)
    pwm.setPWM(1, 0, servoMid)
    ma=400
def dcmotorreset():
    robby.stop()
    moving=None
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/Index.js')
def Index():
    return render_template("Index.js")
@app.route('/button', methods=["POST"])
def button():
    global data
    global servoHorizontalAngle
    global result
    data=json.loads(request.get_data())
    if "direction" in data.keys():
        if data['direction']=='forward':
            motorforward()
        elif data['direction']=='backward':
            motorbackward()
        elif data['direction']=='stopped':
            dcmotorreset()
    if "steering" in data.keys():
        if data['steering']=='left':
            motorleft()
        elif data['steering']=='right':
            motorright()
        elif data['steering']=='straight':
            motorreset()
    
    return " "
@app.route('/cameraHorizontal', methods=["POST"])
def cameraHorizontal():
    global data
    global servoHorizontalAngle
    global result
    data=json.loads(request.get_data())
    while data['CameraHorizontal']=='Left':
        servoHorizontalAngle+=1
        if servoHorizontalAngle>servoMax:
            servoHorizontalAngle=servoMax+1
        pwm.setPWM(14, 0, servoHorizontalAngle)
        time.sleep(0.0001)
    while data['CameraHorizontal']=='Right':
        servoHorizontalAngle-=1
        if servoHorizontalAngle<servoMin:
            servoHorizontalAngle=servoMin+1
        pwm.setPWM(14, 0, servoHorizontalAngle)
        time.sleep(0.0001)
    return" "
@app.route('/cameraVertical', methods=["POST"])
def cameraVertical():
    global data
    global servoVerticalAngle
    global result
    data=json.loads(request.get_data())
    while data['CameraVertical']=='Up':
        servoVerticalAngle+=1
        if servoVerticalAngle>servoMax-108:
            servoVerticalAngle=servoMax-108
        pwm.setPWM(15, 0, servoVerticalAngle)
        time.sleep(0.0001)
    while data['CameraVertical']=='Down':
        servoVerticalAngle-=1
        if servoVerticalAngle<servoMin:
            servoVerticalAngle=servoMin+1
        pwm.setPWM(15, 0, servoVerticalAngle)
        time.sleep(0.0001)
    return" "
@app.route("/cameraReset", methods=["POST"])
def cameraReset():
    global data
    global servoHorizontalAngle
    global servoVerticalAngle
    global result
    servoHorizontalAngle=servoMid
    servoVerticalAngle=servoMid
    pwm.setPWM(14, 0, servoMid)
    pwm.setPWM(15, 0, servoMid)
    return " "
def gen(camera):
    """generate camera frame"""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route("/datentime")
def datentime():
    return render_template("datentime.html")
@app.errorhandler(404)
def page_not_found(a):
    return render_template('404.html')
@app.errorhandler(500)
def server_error(a):
    return render_template("500.html")
@app.errorhandler(405)
def not_allowed(a):
    return render_template("405.html")
if __name__=="__main__":
    app.run(host="10.0.0.78")
