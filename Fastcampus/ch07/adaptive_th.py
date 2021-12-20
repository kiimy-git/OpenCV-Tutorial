import sys
import numpy as np
import cv2

# 적응형 이진화(= 지역이진화)
src = cv2.imread('ch07\\images\\sudoku.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, 
#                   thresholdType, blockSize, C, dst=None) -> dst
'''
Local 이진화를 직접 구현한 것 보다 느림
blockSize: 블록 크기. 3 이상의 홀수(클 수록 좋게 보임)
작을 경우 window에 배경 or 객체만 있을 수 있기 때문에 약간의 noise가 발생
C: 블록 내 평균값 또는 블록 내 가중 평균값에서 뺄 값. 
    (x, y) 픽셀의 임계값으로 
'''
def onChange(pos):
    bsize = pos
    if bsize % 2 == 0:
        bsize = bsize -1
    if bsize < 3:
        bsize = 3

    dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                        cv2.THRESH_BINARY, bsize, 5)
    cv2.imshow('dst', dst)

cv2.imshow('src', src)
cv2.namedWindow('dst')
cv2.createTrackbar('block_size', 'dst', 0, 255, onChange)
cv2.setTrackbarPos('block_size', 'dst', 50)
cv2.waitKey()