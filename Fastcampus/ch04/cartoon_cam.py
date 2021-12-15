import sys
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('video open failed')
    sys.exit()

cam_mode = 0

def cartoon_filter(frame):
    # 축소한 이미지에서 blur 진행시 단순화가 더 효과적으로 나타남
    (h, w) = frame.shape[:2]
    frame2 = cv2.resize(frame, (w//2, h//2)) # 영상에선 가로 * 세로

    # resize안하고 그대로 진행하면 좀 느림? resize 진행하고 적용
    blr = cv2.bilateralFilter(frame2, -1, 10, 5)

    # 내부에서 grayscale변환함
    # cv2.Canny로만 사용하면 edge가 흰색(255)가되고 배경이 검정(0)
    # so, 255 - cv2.Canny() : 반전 됨
    # 가장자리 검출 cv2.Canny()
    edge = 255 - cv2.Canny(frame2, 60, 150)

    # cv2.Canny() gray ==> BGR
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    
    # cv2.bitwise_and 연산
    dst = cv2.bitwise_and(blr, edge)

    # 축소된 이미지 다시 복원
    # 자연스러운 느낌보다는 값이 급격하게 바뀌는 느낌(cv2.INTER_NEAREST)
    dst = cv2.resize(dst, (w,h), interpolation=cv2.INTER_NEAREST)

    return dst

def pencil_sketch(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray, (0,0), 3)
    
    # edge 근방에서 어두운 영역을 검정색으로 밝은 영역은 흰색으로
    # gray % blr (영상 그래프 참조)
    # blr값이 더 큰 부분은 0보다 작은 값
    # blr값이 더 작은 부분은 1보다 큰 값
    dst = cv2.divide(gray, blr, scale=255)
    dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
    return dst

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # cartoon filter
    if cam_mode == 1:
        frame = cartoon_filter(frame)
    
    # pencile filter
    elif cam_mode == 2:
        frame = pencil_sketch(frame)
    
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    elif key == ord(' '):
        cam_mode += 1
        if cam_mode == 3:
            cam_mode = 0


cap.release()