import cv2 as cv

# 이미지 불러오기
img = cv.imread('cat.bmp')
(h,w,d) = img.shape
print(img.shape)

cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv.imshow('image', img)
cv.waitKey()
cv2.destroyAllWindows()
