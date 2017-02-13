#Author: Dan Machen
#12/02/2017

#This file draw a rectangle box upon a given image file.
# It then labels the image with text and fills the contents of the box depending on the length of the text string

import numpy as np
import cv2 as cv

#set parameters for treating decimals
from decimal import *
getcontext()
Context (
prec=28,
rounding=ROUND_HALF_EVEN,
Emin=-999999999,
Emax=999999999,
capitals=1,
flags=[],
traps=[Overflow, DivisionByZero, InvalidOperation])

getcontext().prec = 7

#input sample rectangle box dimensions.
x1 = 20
x2 = 150
y1 = 20
y2 = 150

width = x2-x1
height = y2-y1

#text to be drawn
text = "Example text long"

#make text and box dimensions parametric
#tblength = Decimal(0.45)*int((x2-x1))
#tbheight = Decimal(0.2)*int((y2-y1))
#fontscale = round(Decimal(0.01)*int((y2-y1)))
#textthickness = 2

#test updating box based on text length
font = cv.FONT_HERSHEY_SIMPLEX
baseline=0;
fontscale = 0.45
textthickness = 1

#gathers size of box required to contain given text
text_size, ymin = cv.getTextSize(text,font,fontscale,textthickness)

#gives location of bottom left location of text to be plotted
pt1 = (x1, y1 + text_size[1])

img = cv.imread('text.jpg')

#draw a red line
#img = cv.line(img, (100,100), (300,300), (0,0,255),4)
# adds text in location stated
img = cv.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
img = cv.rectangle(img, (x1,y1),(x1+text_size[0],y1+text_size[1]),(255,0,0),-1)
img = cv.putText (img, text, pt1, font, fontscale, (255,255,255),textthickness,cv.LINE_AA)

cv.imshow('Draw01',img)
cv.waitKey(0)
cv.destroyAllWindows()

