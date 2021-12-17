import sys
import numpy as np
import cv2


src = cv2.imread('ch06\\images\\lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# cv2.Sobel(src, ddepth, dx, dy)
# dx, dy = (1, 0) or (0, 1)
# x방향 미분차수, y방향 미분차수
# ksize = 3 
'''
*미분 마스크 sobel*
sobel_kernel = np.float32([[-1,0,1],
                    [-2,0,2],
                    [-1,0,1]])
dx = cv2.filter2D(src, -1, sobel_kernel)
'''
# -1을 주었기 때문에 grayscale 형태로 나옴
# ddepth = -1 이면 입력 영상 type과 똑같이 나옴
# 회색부분에서 검은색 부분으로 값이 낮아지는 경우 미분값이 음수값이 됨
# 그래서 출력영상에서 그냥 검은색으로 나옴 so, delta=128 할당
# == 눈으로 잘 보이게 하기 위해?

dx = cv2.Sobel(src, -1, 1, 0, delta=128)
dy = cv2.Sobel(src, -1, 0, 1, delta=128) # 수직인 edge는 나오지 않음

# 어느 방향으로 미분하느냐에 따라 값이 바뀐부분이 다름
# so, 따로 미분을 하고 합치는 과정을 진행(Gradient = magintude, phase)

cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()