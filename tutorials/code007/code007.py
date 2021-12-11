import cv2 as cv
import sys

'''
# HSV ( Hue, Saturation, Value )
색상, 채도, 명도
H(0~180), S(0~255), V(0~255)
inRange = 낮은 범위(lowerb)에서 높은 범위(upperb) 사이의 요소를 추출
'''
img = cv.imread('code007\\color_image.jpg')
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) # HSV 
(h, s, v) = cv.split(img_hsv) # cv.split

'''
# HSV = 특정 색만 검출 할 수 있다
1. imread
2. cvtcolor = BGR2HSV
3. inRange
4. bitwise_and
5. cvtcolor = HSV2BGR
'''
# hsv 이미지 참조(0~360인데 opencv 에서 2로 나눠서 색 구별)
orange_h = cv.inRange(h, 8, 20) # == 주황색 부분 흰색
orange = cv.bitwise_and(img_hsv, img_hsv, mask=orange_h)
orange = cv.cvtColor(orange, cv.COLOR_HSV2BGR)

'''
cv2.inRange
lowerb: 하한 값 행렬 또는 스칼라
upperb: 상한 값 행렬 또는 스칼라
'''

cv.imshow('image', img)
cv.imshow('img_hsv', img_hsv)
cv.imshow('h', h)
cv.imshow('s', s)
cv.imshow('v', v)
cv.imshow('orange_h', orange_h)
cv.imshow('orange', orange)
cv.waitKey()