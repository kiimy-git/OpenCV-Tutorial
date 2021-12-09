import cv2 as cv
import numpy as np
import sys

oldx = oldy = -1

def onMouse(event, x, y, flags, param):
    global oldx, oldy

    if event == cv.EVENT_LBUTTONDOWN: # 왼쪽 버튼을 누르면 활성화
        oldx, oldy = x, y # 누르면 시작 지점으로 잡음
        print(f'EVENT_LBUTTONDOWN: {x}, {y}')
    
    elif event == cv.EVENT_LBUTTONUP: # 왼쪽 버튼을 누르고 떼어지면 활성화
        print(f'EVENT_LBUTTONDOWN: {x}, {y}')

    elif event == cv.EVENT_MOUSEMOVE:
        # 마우스가 클릭되어있을때만 출력할 수 있도록 지정해준다.
        # == 안그러면 마우스가 창을 지나갈때마다 계속해서 출력
        # (==) 연산자를 쓰지않고 & and 연산자 사용(값 == 1, cv.EVENT_LBUTTONDOWN)
        if flags & cv.EVENT_FLAG_LBUTTON: # 왼쪽 버튼이 눌려져 있음

            # cv2.circle(img, (x,y), 5, (0, 0, 255), -1)
            # ==> 빨리 그리면 점형식으로 찍힘 so, line으로 설정
            # 이전 마우스 포인트부터 현재 마우스 포인트까지 직선을 그리기
            # 처음 시작점 변수 지정 oldx, oldy
            cv.line(img, (oldx, oldy), (x,y), (0,0,255), 2, cv.LINE_AA)
            cv.imshow('image', img)
            oldx, oldy = x, y

img = np.ones((480,640,3), dtype=np.uint8) * 255 # 흰색

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.setMouseCallback('image', onMouse) 
# img인자 값을 안가져도 되는 이유
# cv.setMouseCallback('image', onMouse, img)
# cv.namedWindow에서 지정 했기 때문에

cv.imshow('image', img)
cv.waitKey()