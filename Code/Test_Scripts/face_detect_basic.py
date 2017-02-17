
#A starter script to load the camera module and recognise a face

#Author: D Machen
#Date: 12/2/2017

import io
import picamera
import cv2
import numpy

#create memory stream so image doesnt have to be saved as jpeg
stream = io.BytesIO()


with picamera.PiCamera() as camera:
        camera.resolution = (320,240)
        camera.brightness = 60
        camera.capture(stream, format='jpeg')

#convert the picture into a numpy array
buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

#now creates open cv image
image = cv2.imdecode(buff,1)

#load cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#Draw rectangles on the faces and eyes
for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

#print text if faces ard found
print "Found "+str(len(faces))+" faces(s)"
#save captured face as image file
cv2.imwrite('result.jpg',image)
