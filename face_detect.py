from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
import imutils
 
# Get user supplied values
cascPath = sys.argv[1]
 
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath) # initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (160, 120)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(160, 120))



image = frame.array
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
 
 
for (x, y, w, h) in faces:
        cv2.circle(image, (x+w/2, y+h/2), int((w+h)/3), (255, 255, 255), 1)