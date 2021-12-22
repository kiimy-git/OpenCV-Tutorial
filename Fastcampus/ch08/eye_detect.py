import sys
import numpy as np
import cv2


src = cv2.imread('ch08\\images\\lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

face_classifier = cv2.CascadeClassifier('ch08\\haarcascade_frontalface_alt2.xml')
eye_classifier = cv2.CascadeClassifier('ch08\\haarcascade_eye.xml')

if face_classifier.empty() or eye_classifier.empty():
    print('XML load failed!')
    sys.exit()

faces = face_classifier.detectMultiScale(src)

for (x1,y1,w1,h1) in faces:
    cv2.rectangle(src, (x1,y1,w1,h1), (0,0,255), 1, cv2.LINE_AA)

    # 얼굴에서 윗 부분만 ROI
    faceROI = src[y1:y1 + h1 //2, x1:x1 + w1]
    eyes = eye_classifier.detectMultiScale(faceROI)

    for (x2,y2,w2,h2) in eyes:
        center = (x2 + w2 // 2, y2 + h2 // 2)
        cv2.circle(faceROI, center, w2 // 2, (255,255,0), 2, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.waitKey()