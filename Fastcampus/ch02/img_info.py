import cv2 as cv
import sys

img_gray = cv.imread('ch02\\images\\cat.bmp', cv.IMREAD_GRAYSCALE)
img_color = cv.imread('ch02\\images\\cat.bmp') # default = cv.IMREAD_COLOR 

# 예외처리
if img_color is None or img_gray is None:
    print('Image load failed')
    sys.exit()

# 이미지 속성(shape = (h, w, d)) 
print('tpye(img_gray)', type(img_gray)) # np.ndarray
print('img_gray.shape', img_gray.shape) # (h, w)
print('img_color.shape', img_color.shape) # (h, w, d)
print('img_gray.shape', img_gray.dtype) # uint8

# 영상 크기 참조
'''
세로 * 가로 = 행렬(np.ndarray)
가로 * 세로 = 영상 좌표계
'''
h, w = img_color.shape[:2] # 행렬
print(f'영상 좌표계 {w} * {h}') # 영상 좌표

# 영상의 픽셀 값 참조
img_gray[:,:] = 255 # 흰색
img_color[:, :] = (0, 0, 255) # 빨간색

cv.imshow('image', img_gray)
cv.imshow('img_color', img_color)
cv.waitKey()
