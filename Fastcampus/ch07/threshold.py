import sys
import numpy as np
import cv2

# 검은 객체 찾기
'''
OpenCV에선 '흰색이 객체다' 라고 정의
'''
src = cv2.imread('ch07\\images\\cells.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

def onChange(pos):
    # cv2.THRESH_BINARY_INV = 검은 객체 흰색으로
    ret, dst = cv2.threshold(src, pos, 255, cv2.THRESH_BINARY)
    print(ret)
    cv2.imshow('thresh', dst)

cv2.imshow('src', src)
cv2.namedWindow('thresh')
cv2.createTrackbar('threshold', 'thresh', 0, 255, onChange)
cv2.setTrackbarPos('threshold', 'thresh', 50)
cv2.waitKey()