# Author: Dan Machen
# 12/02/2017

#This file takes an image from file and draws lines,rectangles and text into it.
# The inputs are the starting x and y coordinates on the image.
# The output wil show the image in a new window with the shapes drawn onto it.


import numpy as np
import cv2 as cv


x1 = 20
x2 = 150
y1 = 20
y2 = 150

textheight = 1
textthickness = 2

#font = cv.FONT_HERSHEY_SIMPLEX
font = cv.FONT_HERSHEY_PLAIN

img = cv.imread('text.jpg')

#draw a red line
#img = cv.line(img, (100,100), (300,300), (0,0,255),4)
# adds text in location stated
img = cv.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
img = cv.rectangle(img, (x1,y1),(x1+50,y1+25),(255,0,0),-1)
img = cv.putText (img, "Text", (x1,y1+20), font, textheight, (255,255,255),textthickness,cv.LINE_AA)

cv.imshow('Draw01',img)
cv.waitKey(0)

