import sys
import numpy as np
import cv2

src = cv2.imread('ch03\\images\\candies.png')

if src is None:
    print('Image load failed!')
    sys.exit()

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# 특정 색 추출
# 이미지를 보면 RGB가 더 깨끗하게 나오고 HSV는 지저분한 픽셀이 나옴
# RGB가 더 좋다고 볼 수 없는것이 이미지가 어두워지면 성능이 떨어짐
# HSV를 주로 사용하게된다.(V = 0 ~ 255를 할당하면 어두운 영상도 반환해줌)
dst1 = cv2.inRange(src, (0,128,0), (100,255,100))
dst2 = cv2.inRange(hsv, (50,150,0), (80,255,255))
'''
50 <= H <= 80
150 <= S <= 255
0 <= V <= 255
'''

cv2.imshow('hsv', hsv)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

##############################################################

# cv2.createTrackbar(trackbarName, windowName, value, count, onChange)
# cv2.namedWindow 설정해줘야해 = windowName

def onChange(pos):
    # pos 지정
    hmin = cv2.getTrackbarPos('H_min', 'dst')
    hmax = cv2.getTrackbarPos('H_max', 'dst')

    # H만 설정 값으로 지정
    dst = cv2.inRange(hsv, (hmin, 150, 0), (hmax, 255, 255))
    cv2.imshow('dst', dst)

cv2.imshow('src', src)
cv2.namedWindow('dst')
# 두개를 지정했기 때문에 onChange함수에서 getTrackbarPos를 사용해서
# 최소 최대 값을 지정해줌
cv2.createTrackbar('H_min', 'dst', 50, 170, onChange)
cv2.createTrackbar('H_max', 'dst', 80, 170, onChange)
# onChange(0) ==> 생략가능??
cv2.waitKey()