import sys
import numpy as np
import cv2

# grayscale
src = cv2.imread('ch06\\images\\building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# cv2.Canny(image, threshold1, threshold2, L2gradient)
# thresg1(LOW) : thresh2(HIGH)= 1 : 2 or 1 : 3
# L2gradient = False(L1norm), True(L2norm)
# gradient 크기를 계산할때 L2norm이 좋아 but 연산 시간이 오래걸림
'''
sobel의 단점
1. Edge가 두꺼움
2. Threshold를 어떻게 잡느냐에 따라 Edge가 달라짐
= Edge인데도 조명의 밝기로 인해 Edge로 판단을 못 하는 경우가 발생
'''

dst = cv2.Canny(src, 1, 3)
dst1 = cv2.Canny(src, 50, 150)

def onChange(pos):
    low = cv2.getTrackbarPos('threshold1', 'canny')
    high = cv2.getTrackbarPos('threshold2', 'canny')

    img_canny = cv2.Canny(src, low, high)
    cv2.imshow('canny', img_canny)

# Trackbar (사용할 함수 파라미터 지정)
cv2.namedWindow('canny') 
cv2.createTrackbar('threshold1', 'canny', 0, 1000, onChange)
cv2.createTrackbar('threshold2', 'canny', 0, 1000, onChange)

# 각 파라미터 초기값
cv2.setTrackbarPos('threshold1', 'canny', 50)
cv2.setTrackbarPos('threshold2', 'canny', 150)
# cv2.imshow('src', src)
cv2.waitKey()



