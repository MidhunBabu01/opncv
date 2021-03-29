import cv2
image = cv2.imread("lena.jpg",1)
cv2.line(image,(0,0),(400,400),(255,0,0),5)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()