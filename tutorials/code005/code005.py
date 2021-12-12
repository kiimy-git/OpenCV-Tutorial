import cv2 as cv
import sys

# Erosions(침식) and Dilations(팽창)

img = cv.imread('code005\\tetris_blocks.png')

# 예외처리
if img is None:
    print('image load failed')
    sys.exit()

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, dst = cv.threshold(img_gray, 225, 255, cv.THRESH_BINARY_INV)
mask = dst.copy()
# cv.erode = iterations이 클 수록 작아짐
# (img, kernel, iterations=1)
erode = cv.erode(mask, None, iterations=5)

# cv.dilate = iterations이 클 수록 커짐
# (img, kernel, iterations=1)
dilate = cv.dilate(mask, None, iterations=5)

cv.imshow('image', img)
cv.imshow('thresh', dst)
cv.imshow('erosion', erode)
cv.imshow('dilate', dilate)
cv.waitKey()

