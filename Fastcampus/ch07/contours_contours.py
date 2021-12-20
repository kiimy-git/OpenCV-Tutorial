import sys
import random
import numpy as np
import cv2


src = cv2.imread('ch07\\images\\milkdrop.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

ret, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)

contours, hier = cv2.findContours(src_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

h, w = src.shape[:2]

# 검은 화면의 color 이미지 생성
dst = np.zeros((h,w,3), np.uint8)

# 단지 객체 파악 하기 위함
for i in range(len(contours)):
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst, contours, i, c, 1, cv2.LINE_AA)


cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)
cv2.waitKey()