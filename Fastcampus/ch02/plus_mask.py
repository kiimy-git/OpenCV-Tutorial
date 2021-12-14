import sys
import cv2 as cv

# flags = cv.IMREAD_COLOR (default)
src = cv.imread('ch02\\airplane.bmp')
mask = cv.imread('ch02\\mask_plane.bmp', cv.IMREAD_GRAYSCALE)
dst = cv.imread('ch02\\field.bmp')

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
src1 = cv.imread('ch02\\cat.bmp', cv.IMREAD_COLOR)
logo = cv.imread('ch02\\opencv-logo-white.png', cv.IMREAD_UNCHANGED)
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

# logo에서 crop으로 복사 하는데 logo_mask흰 부분만 가져오겠다.
cv.copyTo(logo, logo_mask, crop)

cv.imshow('src1', src1)
cv.imshow('logo_mask', logo_mask)
cv.imshow('logo', logo)
cv.imshow('crop', crop)

cv.waitKey()
