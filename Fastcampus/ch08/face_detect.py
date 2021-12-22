import sys
import numpy as np
import cv2


src = cv2.imread('ch08\\images\\lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# Cascade 클래스 객체 생성
classifier = cv2.CascadeClassifier('ch08\\haarcascade_frontalface_alt2.xml')

if classifier.empty():
    print('XML load failed')
    sys.exit()

tm = cv2.TickMeter()
tm.start()

faces = classifier.detectMultiScale(src)
'''
cv2.CascadeClassifier.detectMultiScale(image, scaleFactor=None,
                    minNeighbors=None, flags=None, minSize=None, maxSize=None) -> result

scaleFactor가 클 수록 빨라짐(default = 1.1(1.2))
but 특정 크기의 객체를 놓칠 수 있다

minSize, maxSize (최소, 최대 객체크기) 
= 너무 작은 객체가 아니면 minSize 설정하는 것이 좋다
==> 파라미터를 적절히 조절하면 속도가 빨라짐

result: 검출된 객체의 사각형 정보(x, y, w, h)를 담은 numpy.ndarray
'''

tm.stop()
print(tm.getTimeMilli())
print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(src, (x,y,w,h), (0,0,255), 2, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.waitKey()