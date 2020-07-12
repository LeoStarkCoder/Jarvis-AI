import cv2
import numpy as np

face_detection = cv2.CascadeClassifier('C:\\Users\\Dell\\Desktop\\Python 3.6.8\\haarcascade_frontalface_default.xml')
img = cv2.imread('C:\\Users\\Dell\\Desktop\\my python projects\\bill gates.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_detection.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),3)
cv2.imshow('Cool', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    