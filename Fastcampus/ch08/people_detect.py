import sys
import random
import numpy as np
import cv2

# 동영상 불러오기
cap = cv2.VideoCapture('ch08\\video\\vtest.avi')

if not cap.isOpened():
    print(('video open failed'))
    sys.exit()

# 보행자 검출을 위한 HOG 기술자 설정
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
'''
cv2.HOGDescriptor_getDefaultPeopleDetector()
# retval : 미리 훈련된 특징 벡터. numpy.ndarray. shape=(3781, 1)
'''

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # 매 프레임마다 보행자 검출
    detected, _ = hog.detectMultiScale(frame)
    # -> foundLocations, foundWeights
    # 영역, 신뢰도

    # 검출 결과 bbox 생성
    for (x,y,w,h) in detected:
        c = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        cv2.rectangle(frame, (x,y,w,h), c, 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('q'):
        break

