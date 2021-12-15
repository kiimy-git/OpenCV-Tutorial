import sys
import numpy as np
import cv2

# 이미지에 노이즈 추가 함수
def noisy(noisy_type, image):
    if noisy_type == 'speckle':
        row,col,ch = image.shape
        gauss = np.random.randn(row,col,ch)
        gauss = gauss.reshape(row,col,ch)        
        noisy = image + image * gauss
        return noisy

src = cv2.imread('ch04\\images\\noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# median filter = 소금-후추 잡음 제거에 효과적
# filtering 방법이 sort 알고리즘을 사용하여 가운데 값을 선택
# quailty가 좋지 않음
dst = cv2.medianBlur(src, 3)
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()