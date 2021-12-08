# Rotating an image
import cv2 as cv

img = cv.imread('.\\ch01\\cat.bmp')

(h,w,d) = img.shape

center = (w //2, h//2)

# cv.getRotationMatrix2D(중심점, 각도, 비율= 확대 및 축소 비율)
M = cv.getRotationMatrix2D(center, -45, 1)
rotated = cv.warpAffine(img, M, (w,h))


# image flip
flip = cv.flip(img, 0)
'''
flipCode < 0은 XY 축 대칭(상하좌우 대칭)

flipCode = 0은 X 축 대칭(상하 대칭)

flipCode > 0은 Y 축 대칭(좌우 대칭)
'''
cv.imshow('rotated', rotated)
cv.imshow('flip', flip)
cv.waitKey()