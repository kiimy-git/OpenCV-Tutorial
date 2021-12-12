import cv2 as cv
import sys
import matplotlib.pyplot as plt

img = cv.imread('.\\code001\\cat.bmp')
img_mat = cv.cvtColor(img, cv.COLOR_BGR2RGB) # matplotlib

if img is None:
    print('Image load failed')
    sys.exit()

print(img.shape) # 480, 640, 3 (세로 * 가로)

# cv2.resize(src, dstSize, fx, fy, interpolation) , 상대 크기(fx, fy)
img_resize = cv.resize(img, dsize=(480,640)) # (가로 * 세로)
img_resize1 = cv.resize(img, dsize=(480,640), interpolation=cv.INTER_AREA) # default
img_resize2 = cv.resize(img, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv.INTER_AREA)
# 상대크기 설정시 dsize =(0,0) 

cv.imshow('image', img)
cv.imshow('image_resize', img_resize)
cv.imshow('image_resize1', img_resize1)
cv.imshow('image_resize2', img_resize2)
cv.imshow('img_mat', img_mat)
cv.waitKey()
