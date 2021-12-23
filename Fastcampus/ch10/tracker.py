import sys
import numpy as np
import cv2

'''
opencv_version = 4.1.0.25에서 실행
'''

# 동영상 열기
cap = cv2.VideoCapture('ch10\\videos\\tracking1.mp4')

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

# 트래커 객체 생성
# ==> 배경이 비슷하면? 검은화면이 띄면 추적 못함
# ==> 추적하는 객체가 가려지면 놓치게 됨
'''
# Kernelized Correlation Filters
# 그나마 빠르게 동작함
#tracker = cv2.TrackerKCF_create()

# Minimum Output Sum of Squared Error
#tracker = cv2.TrackerMOSSE_create()
'''
# Discriminative Correlation Filter with Channel and Spatial Reliability
# 추적은 잘하는 편이지만 속도가 느려
tracker = cv2.TrackerMIL_create()

# 첫 번째 프레임에서 추적 ROI 설정
ret, frame = cap.read()

if not ret:
    print('Frame read failed!')
    sys.exit()

rc = cv2.selectROI('frame', frame)
tracker.init(frame, rc)

while True:
    ret, frame = cap.read()

    if not ret:
        print('Frame read failed!')
        sys.exit()

    # 추적 & ROI 사각형 업데이트
    ret, rc = tracker.update(frame)

    # rectangle을 위한 int 변환
    rc = tuple([int(_) for _ in rc])
    cv2.rectangle(frame, rc, (0,0,255), 2)

    cv2.imshow('frame', frame)
    if cv2.waitkey(20) == ord('q'):
        break
