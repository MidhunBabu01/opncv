import cv2
import numpy as np
org_image = cv2.imread('lena.jpg',1)
blur_image = cv2.blur(org_image,(5,5))
Gaussian_Blur=cv2.GaussianBlur(org_image,(5,5),0)
cv2.imshow('org_image',org_image)
cv2.imshow("blur_image",blur_image)
cv2.imshow('Gaussian_Blur',Gaussian_Blur)
cv2.waitKey(0)