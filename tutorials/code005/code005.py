import cv2 as cv
import sys

# Erosions(침식) and Dilations(팽창)

img = cv.imread('tetris_blocks.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(img_gray, 225, 255, cv.THRESH_BINARY_INV)
mask = thresh.copy()
# cv.erode = iterations이 클 수록 작아짐
erode = cv.erode(mask, None, iterations=5)

# cv.erode = iterations이 클 수록 커짐
dilate = cv.dilate(mask, None, iterations=5)

cv.imshow('image', img)
cv.imshow('thresh', thresh)
cv.imshow('erosion', erode)
cv.imshow('dilate', dilate)
cv.waitKey()

