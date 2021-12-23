import cv2
import numpy as np
import sys

cap = cv2.VideoCapture('ch10\\videos\\PETS2000.avi')

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

# 배경 차분 알고리즘 객체 생성(MOG class 객체화)
# bs = cv2.createBackgroundSubtractorMOG2()
bs = cv2.createBackgroundSubtractorKNN()
'''
cv2.createBackgroundSubtractorMOG2(, history=None, varThreshold=None, 
                                    detectShadows=None) -> dst
* 멤버함수
+ apply()
+ getBackgroundImage()
varThreshold : 새로 들어온 영상의 pixel 값이 배경영상의 pixel 값에 부합하는지판단
detecShadows: 그림자 검출 여부, 기본값은 True
'''

# Shadow 지정 ==> mask 0, 128(회색), 255
# class default == True
# bs.setDetectShadows(False)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # fgmask = 0, 128, 255 값을 가짐
    # 그림자를 표현한다면 128값을 가지는 것이다
    fgmask = bs.apply(gray)

    # 학습된 배경 출력
    back = bs.getBackgroundImage()

    cnt, _, stats, _ = cv2.connectedComponentsWithStats(fgmask)

    for i in range(1, cnt):
        (x,y,w,h, area) = stats[i]

        if area < 100:
            continue

        cv2.rectangle(frame, (x,y,w,h), (0,0,255), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    cv2.imshow('back', back)
    cv2.imshow('fgmask', fgmask)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
