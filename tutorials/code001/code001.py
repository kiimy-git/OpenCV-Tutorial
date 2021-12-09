import cv2 as cv

# 이미지 불러오기
img = cv.imread('cat.bmp')
(h,w,d) = img.shape
print(img.shape)

cv.imshow('image', img)
cv.waitKey()
