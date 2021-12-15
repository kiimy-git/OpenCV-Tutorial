import cv2 as cv
import sys

img1 = cv.imread('code007\\color_image.jpg')
img2 = cv.imread('tetris_blocks.png')
img_hsv = cv.cvtColor(img1, cv.COLOR_BGR2HSV)

# add를 위한 동일한 이미지 사이즈로 변경
print(img1.shape) # 640, 1920 ( h ,w )
img2 = cv.resize(img2, (1920,640))

if img1 is None and img2 is None:
    print('Image load failed')
    sys.exit()

# cv2.add(src1, src2)
img_sum = cv.add(img1, img2)

# cv2.addweighted(img1 * alpha + img2 * (1-alpha), gamma)
# gamma 정수값을 더함으로써 좀 더 눈에 잘보이게 할 수 있다.
alpha = 0.5
img_addweight = cv.addWeighted(img1, alpha, img2, 1-alpha, 0)

# 영상이나 이미지에서 색상을 검출 할 때, 배열 요소의 범위 설정 함수(cv2.inRange)의 영역이 한정되어 색상을 
# 설정하는 부분이 제한되어 있다.
# 예를 들어 빨간색 영역이 약 0 ~ 5와 약 170 ~ 179으로 범위가 두 가지로 나눠져
# ==> 배열 요소의 범위 설정 함수를 두 개의 범위로 설정하고 검출한 두 요소의 배열을 병합해서 하나의 공간으로 만들어야 
# 배열 병합 = cv2.addweighted
(h,s,v) = cv.split(img_hsv)

# red mask를 찾는다.
lower_red = cv.inRange(img_hsv, (0,100,100), (5,255,255))
upper_red = cv.inRange(img_hsv, (170,100,100), (180,255,255))
added_red = cv.addWeighted(lower_red, 1.0, upper_red, 1.0, 0) # red 부분 흰색

red = cv.bitwise_and(img_hsv, img_hsv, mask=added_red)
# HSV -> BGR
final_red = cv.cvtColor(red, cv.COLOR_HSV2BGR)



cv.imshow('image1', img1)
cv.imshow('image2', img2)
cv.imshow('sum', img_sum)
cv.imshow('weight', img_addweight)
cv.imshow('add_weighted', added_red)
cv.imshow('bitwise_and', red)
cv.imshow('final_red', final_red)
cv.waitKey()
