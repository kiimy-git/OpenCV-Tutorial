import cv2
import numpy as np
import sys

cap = cv2.VideoCapture('ch10\\videos\\PETS2000.avi')

if not cap.isOpened():
    print('Video load failed')
    sys.exit()

# 배경 영상 등록(정적(static) 배경)
ret, back = cap.read()

if not ret:
    print('Background image registration failed!')
    sys.exit()

back = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)
back = cv2.GaussianBlur(back, (0,0), 1.)
# *cv2.accumulateWeighted(gray, fback, 0.01) 연산을 위함*
fback = back.astype(np.float32) 

while True:
    ret, frame = cap.read()

    if not ret:
        brake

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (0,0), 1.)

    # fback: float32, back: uint8 정적배경
    cv2.accumulateWeighted(gray, fback, 0.01)

    # *absdiff 연산을 위한 변환*
    back = fback.astype(np.uint8)

    diff = cv2.absdiff(gray, back)
    _, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    cnt, _, stats, _ = cv2.connectedComponentsWithStats(diff)

    for i in range(1, cnt):
        x, y, w, h, area = stats[i]

        if area < 100:
            continue

        cv2.rectangle(frame, (x, y, w, h), (0,0,255), 2, cv2.LINE_AA)

    cv2.imshow('diff', diff)
    cv2.imshow('frame', frame)
    cv2.imshow('back', back)
    
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
