import cv2
import numpy as np
capture = cv2.VideoCapture(0)
while(1):
    frame = capture.read()
    converted_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_bound = np.array([110,50,50])
    upper_bound = np.array([130,252,252])
    mask = cv2.inRange(converted_image,lower_bound,upper_bound)
    cv2.imshow('mask',mask)
    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('result',result)
    k = cv2.waitKey(5)&0xFF
    if k == 27:
        break