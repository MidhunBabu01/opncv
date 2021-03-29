import cv2
font = cv2.FONT_HERSHEY_COMPLEX
image = cv2.imread('lena.jpg',1)
cv2.putText(image,"hello",(100,100),font,4,(255,255,255),cv2.LINE_AA)
cv2.imshow("imge",image)
cv2.waitKey(0)
