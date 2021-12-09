import sys
import cv2 as cv

# flags = cv.IMREAD_COLOR (default)
src = cv.imread('ch02\\images\\airplane.bmp')
mask = cv.imread('ch02\\images\\mask_plane.bmp', cv.IMREAD_GRAYSCALE)
dst = cv.imread('ch02\\images\\field.bmp')

'''
# HSV = 특정 색만 검출 할 수 있다
1. imread
2. cvtcolor = BGR2HSV
3. inRange
4. bitwise_and
5. cvtcolor = HSV2BGR

cv2.inRange
lowerb: 하한 값 행렬 또는 스칼라
upperb: 상한 값 행렬 또는 스칼라
'''
# Hue, Saturation, Value
# 색상, 채도, 명도
# H(0~180), S(0~255), V(0~255)
# inRange = 낮은 범위(lowerb)에서 높은 범위(upperb) 사이의 요소를 추출
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
hsv_mask = cv.inRange(hsv, (155, 100, 100), (70, 255, 255))
(h, s, v) = cv.split(hsv)

# cv.inRange(h, 8, 20) 특정색만 표현 가능(주황색 = 8~20)
'''
h = cv2.inRange(h, 8, 20)
orange = cv2.bitwise_and(hsv, hsv, mask = h) # 이미지 위에 덧씌워 해당 부분만 출력
orange = cv2.cvtColor(orange, cv2.COLOR_HSV2BGR)
'''
# cv.imshow('h', h)
# cv.imshow('s', s)
# cv.imshow('v', v)

## image 합성(원본, mask, 합성할 이미지(return))
cv.copyTo(src, mask, dst) # return dst 값으로 나옴

cv.imshow('src', src)
cv.imshow('mask', mask)
cv.imshow('dst', dst)
cv.imshow('hsv', hsv)
cv.imshow('hsv_mask', hsv_mask)
cv.waitKey()

################################################################

# 알파 채널을 마스크 영상으로 이용
# 투명도가 들어간 image = ndim = 4
src1 = cv.imread('ch02\\images\\cat.bmp', cv.IMREAD_COLOR)
logo = cv.imread('ch02\\images\\opencv-logo-white.png', cv.IMREAD_UNCHANGED)
print(logo.shape) # (222, 180, 4)
# dst = cv.imread('ch02\\field.bmp')

# 예외처리
if src1 is None or logo is None:
    print('Image load failed')
    sys.exit()

logo_mask = logo[:, :, -1] # mask
logo = logo[:, :, :3] # BGR 

# dst는 사이즈가 크기 때문에 사이즈 맞춰줘야함
h, w = logo.shape[:2]
crop = src1[:h, :w]

cv.copyTo(logo, logo_mask, crop)

cv.imshow('src1', src1)
cv.imshow('logo_mask', logo_mask)
cv.imshow('logo', logo)

cv.waitKey()
