# Rotating an image
import cv2 as cv

img = cv.imread('.\\ch01\\cat.bmp')

(h,w,d) = img.shape

center = (w //2, h//2)

# cv.getRotationMatrix2D(중심점, 각도, 비율= 확대 및 축소 비율)
M = cv.getRotationMatrix2D(center, -45, 1)
rotated = cv.warpAffine(img, M, (w,h))

cv.imshow('rotated', rotated)
cv.waitKey()