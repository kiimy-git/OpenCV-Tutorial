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

# color로 진행해도 되지만 연산 속도나 굳이 color가 필요가 없어서
back = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)

# noise 제거(가우시안 없을시 도로 라인 같은 곳에 noise 발생)
# why? 빛의 반사?로 인해 튀는 값이 나타날 수 있다.
# 정적영상 or 현재 영상 둘 중에 하나만 gaussian == noise가 뚜렷해짐
back = cv2.GaussianBlur(back, (0,0), 1.)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (0,0), 1.0)

    # 차영상 구하기 & 이진화(실시간 영상 - 정적배경)
    # 덧셈 함수나 뺄셈 함수에서는 두 배열의 요소를 서로 뺄셈했을 때 음수가 발생하면 0을 반환했지만 
    # 절댓값 차이 함수는 이 값을 절댓값으로 변경해서 양수 형태로 반환
    diff = cv2.absdiff(gray, back)
    # 차이값이 30 이하면 0, 이상이면 255(30정도의 차이값은 노이즈일 가능성이 높다라고 보면됨)
    _, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # + 레이블링을 이용한 boundingbox 표시
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(diff)

    # 0은 배경이기 때문에 배경은 제외(grayscale)
    for i in range(1, cnt):
        (x, y, w, h, area) = stats[i]

        # 작은 객체를 포함시킬려면 area를 지정해주는 것이 좋음
        if area < 100:
            continue

        cv2.rectangle(frame, (x, y, w, h), (0,0,255), 1, cv2.LINE_AA)


    cv2.imshow('frame', frame)
    cv2.imshow('diff', diff)
    cv2.imshow('back', back) # 업데이트가 되지 않음

    if cv2.waitKey(20) == ord('q'):
        break

cap.release()
