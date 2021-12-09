import cv2 as cv

# 이미지 불러오기
img = cv.imread('cat.bmp')
(h,w,d) = img.shape
print(img.shape)

cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
# WINDOW_NORMAL = 영상 크기가 클때(마우스로 크기를 줄이거나 키울 수 있음)
# WINDOW_AUTOSIZE = default
cv.imshow('image', img)
cv.waitKey()
cv2.destroyAllWindows()
