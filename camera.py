#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This scrtipt script..

import cv2
from imutils.video.pivideostream import PiVideoStream
import imutils
import numpy as np
import time

class VideoCamera:
    def __init__(self, flip = False):
        self.vs = PiVideoStream().start()
        self.flip = flip
        time.sleep(2)
    def __del__(self):
        self.vs.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        frame = self.flip_if_needed(self.vs.read())
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
