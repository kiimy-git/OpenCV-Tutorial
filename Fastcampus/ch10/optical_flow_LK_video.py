import sys
import numpy as np
import cv2

# 특징점을 따라감
# LK = 사용자가 정의한 몇 개의 점에서만 이동방향을 찾는다.

# 카메라 장치 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed!')
    sys.exit()

# 설정 변수 정의
MAX_COUNT = 50
needToInit = False
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
          (0, 255, 255), (255, 0, 255), (128, 255, 0), (0, 128, 128)]

ptSrc = None
ptDst = None

while True:
    ret, frame = cap.read()

    if not ret:
        break

    img = frame.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 특징점 검출 활성화를 위함
    if needToInit:
        ptSrc = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
        needToInit= False

    if ptSrc is not None:
        if prev is None:
            prev = gray.copy()

        ptDst, status, _ = cv2.calcOpticalFlowPyrLK(prev, gray, ptSrc, None)

        for i in range(ptDst.shape[0]):
            if status[i,0] == 0:
                continue

            cv2.circle(img, (ptDst[i,0]).astype(int), 3, colors[i % 8], cv2.LINE_AA)
            # cv2.arrowedLine(img, (ptSrc[i,0]).astype(int), (ptDst[i,0]).astype(int), (0,0,255), 3)

    cv2.imshow('img', img)
    cv2.imshow('frame', frame)

    key = cv2.waitKey(20)

    if key == ord('q'):
        break
    elif key == ord('r'):
        needToInit = ~needToInit
    elif key == ord('c'): # 좌표초기화
        ptSrc = None
        ptDst = None

    ptDst, ptSrc = ptSrc, ptDst
    prev = gray

