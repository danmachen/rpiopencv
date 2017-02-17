#A starter script to load the camera module and recognise a face
# puts a box around the recognised face and eyes
# prints a filled label at top left of box with text.

#Author: D Machen

#Date: 13/2/2017

import io
import picamera
import cv2 as cv
import numpy as np

#set parameters for treating decimals (use if parametric values create floats)
#from decimal import *
#getcontext()
#Context (
#prec=28,
#rounding=ROUND_HALF_EVEN,
#Emin=-999999999,
#Emax=999999999,
#capitals=1,
#flags=[],
#traps=[Overflow, DivisionByZero, InvalidOperation])

#getcontext().prec = 7

#create memory stream so image doesnt have to be saved as jpeg
stream = io.BytesIO()

with picamera.PiCamera() as camera:
        camera.resolution = (320,240)
        camera.brightness = 60
        camera.capture(stream, format='jpeg')

#convert the picture into a numpy array
buff = np.fromstring(stream.getvalue(), dtype=np.uint8)

#now creates open cv image
image = cv.imdecode(buff,1)

#load cascades
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#Draw rectangles on the faces and eyes and label
#set font parameters
font = cv.FONT_HERSHEY_SIMPLEX
baseline=0;
#fontscale could also be parametric to face box size
fontscale = 0.45
textthickness = 1

#text to be drawn
text = "Dan"

#gathers size of box required to contain given text
text_size, ymin = cv.getTextSize(text,font,fontscale,textthickness)

for (x,y,w,h) in faces:

        cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        pt1 = (x, y + text_size[1])
        cv.rectangle(image, (x,y),(x+text_size[0],y+text_size[1]),(255,0,0),-1)
        cv.putText (image, text, pt1, font, fontscale, (255,255,255),textthickness,cv.LINE_AA)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
                cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

#print text if faces ard found
print "Found "+str(len(faces))+" faces(s)"
#save captured face as image file
cv.imwrite('result.jpg',image)
cv.imshow('Draw01',image)
cv.waitKey(0)
cv.destroyAllWindows()

