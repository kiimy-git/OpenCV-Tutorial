import sys
import numpy as np
import cv2

# 특정 색 추적

# 비디오 파일 열기
cap = cv2.VideoCapture('ch10\\videos\\camshift.avi')

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

ret, frame = cap.read()

# roi = cv2.selectROI('orange', frame)
(x, y, w, h) = cv2.selectROI('orange', frame)
# print(roi) x, y, w, h
rc = (x, y, w, h)

if not ret:
    print('frame read failed!')
    sys.exit()

obj_roi = frame[y:y+h, x:x+w]
roi_hsv = cv2.cvtColor(obj_roi, cv2.COLOR_BGR2HSV)

# HS 히스토그램 계산
channels = [0,1]
ranges = [0,180, 0, 256]
hist = cv2.calcHist([roi_hsv], channels, None, [180,256], ranges)

# hist 영상화(y = H, x= S)
hist_norm = cv2.normalize(cv2.log(hist+1), None, 0, 255, cv2.NORM_MINMAX)
cv2.imshow('hist_nrom', hist_norm)
cv2.waitKey()

# Mean Shift 알고리즘 종료 기준
# 최대 10번 반복하며, 정확도가 1이하이면(즉, 이동 크기가 1pixel보다 작으면)종료
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TermCriteria_COUNT, 10, 1)

# 비디오 매 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # HS 히스토그램에 대한 역투영
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 0보다 큰 값으로 되있는 확률과 같은 개념의 이미지를 반환
    backproj = cv2.calcBackProject([frame_hsv], channels, hist, ranges, 1)

    # Mean Shift(= orange 좌표를 입력과 츌력으로 받는다)
    _, rc = cv2.meanShift(backproj, rc, term_crit)
    '''
    cv2.meanShift(probImage, window, criteria) -> retval, window

    probImage: 관심 객체에 대한 히스토그램 역투영 영상(확률 영상)
    window: 초기 검색 영역 윈도우 & 결과 영역 반환
    retval: 알고리즘 내부 반복횟수
    '''
    cv2.rectangle(frame, rc, (0, 0, 255), 2)
    cv2.imshow('frame', frame)
    cv2.imshow('backproj', backproj)

    if cv2.waitKey(20) == ord('q'):
        break

cap.release()

