import sys
import numpy as np
import cv2


src = cv2.imread('ch07\\images\\circuit.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 만약 세로방향으로만 침식 or 팽창 하고싶다면
# ksize(가로, 세로) 가로를 작게하고 세로를 크게
# kernel
se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
'''
cv2.MORPH_RECT 사각형 모양
cv2.MORPH_CROSS 십자가 모양
cv2.MORPH_ELLIPSE 사각형에 내접하는 타원
'''

dst1 = cv2.erode(src, se)

dst2 = cv2.dilate(src, None)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()