import sys
import numpy as np
import cv2

# meanshift와 거의 같음
# bbox가 객체의 가깝거나 멀어질때 맞춰나감
# 비디오 파일 열기
cap = cv2.VideoCapture('ch10\\videos\\camshift.avi')

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

# 초기 사각형 영역: (x, y, w, h)
# *참고* selectROI로 지정해서 사용할 수 있다.
x, y, w, h = 135, 220, 100, 100
rc = (x, y, w, h)

ret, frame = cap.read()

if not ret:
    print('frame read failed!')
    sys.exit()

roi = frame[y:y+h, x:x+w]
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# HS 히스토그램 계산
channels = [0, 1]
ranges = [0, 180, 0, 256]
hist = cv2.calcHist([roi_hsv], channels, None, [90, 128], ranges)

# CamShift 알고리즘 종료 기준
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

# 비디오 매 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # HS 히스토그램에 대한 역투영
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    backproj = cv2.calcBackProject([frame_hsv], channels, hist, ranges, 1)

    # Camshift
    ret, rc = cv2.CamShift(backproj, rc, term_crit)
    ''' meanshift <-> camshift
    cv2.CamShift(probImage, window, criteria) -> retval, window

    retval: 추적하는 객체의 모양을 나타내는 회전된 사각형정보 반환
    ((cx, cy), (width, height), angle)
    (사각형의 중심), (가로,세로), 사각형이 몇도 회전했는지

    window: 회전되지 않은 사각형
    '''

    # 추적 결과 화면 출력(타원)
    cv2.rectangle(frame, rc, (0,0,255), 2)
    # cv2.ellipse(frame, ret, color=(0,255,0), thickness=2)
    cv2.imshow('frame', frame)

    if cv2.waitKey(30) == ord('q'):
        break


cap.release()