import cv2
image = cv2.imread('lena.jpg',1)
cv2.imshow("imge",image)
cv2.waitKey(5000)