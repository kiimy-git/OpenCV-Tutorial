import cv2 as cv
import numpy as np

# 새 영상 생성
img1 = np.empty((240, 320), dtype=np.uint8) # grayscale 
img2 = np.zeros((240,320,3), dtype=np.uint8) # ndim 3 = color 
img3 = np.ones((240,320), dtype=np.uint8)*255 # * 255(흰색) 연산가능
img4 = np.full((240,320,3), (0, 255, 255), dtype=np.uint8) # yellow 채우기

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('img3', img3)
cv.imshow('img4', img4)
cv.waitKey()

# 영상 복사
img = cv.imread('ch02\\images\\HappyFish.jpg')
# img_2 = img, 이미지 공유됨
img_copy = img.copy()

cv.imshow('img', img)
cv.imshow('img_copy', img_copy)
cv.waitKey()

# crop(부분 영상 추출)
img_crop1 = img[40:120, 30:150]
img_crop2 = img[40:120, 30:150].copy()

img_crop2.fill(255) # 0 검은색, 255 흰색

cv.namedWindow('img_crop1', cv.WINDOW_NORMAL) # 창 크기 조절
cv.imshow('img_crop1', img_crop1)
cv.imshow('img_crop2', img_crop2)
cv.waitKey()
