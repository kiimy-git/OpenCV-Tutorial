import cv2 as cv
import sys
import numpy as np


img = cv.imread('ch03\\images\\lenna.bmp', cv.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

# cv2.add(src1, src2)
'''
src1, src2 = 스칼라는 실수 값 하나 또는 실수 값 네 개로 구성된 튜플
grayscale = (100, 0, 0, 0) = B, G, R, D
실수값 하나 지정하면 나머진 기본값 0으로 설정됨 
'''

# 밝기 조절 (밝아짐)
# grayscale
dst = cv.add(img, 100)
dst1 = img + 100
'''
dst = src + 100(브로드캐스팅) 
==> 255값보다 커지는 경우 그 값을 0에 가까운 값으로 바뀐다.
==> (256 = 0 , 257 = 1) 반전 효과
밝은 부분이 검은색으로 변함/ so, cv2.add() 사용
'''
# numpy 사용시(반환 이미지 dst와 같음)
# 0보다 작으면 0, 255보다 크면 255
dst_dst = np.clip(img +100., 0, 255).astype(np.uint8)

# color 영상

img_color = cv.imread('ch03\\images\\lenna.bmp')

if img_color is None:
    print('Image load failed!')
    sys.exit()

# color의 경우 R, G, B 값을 지정 해줘야함
img_color1 = cv.add(img_color, (100, 100, 100, 0))
# img_color1 = np.clip(img_color + 100., 0, 255).astype(np.uint8)

cv.imshow('image', img_color)
cv.imshow('img_color1', img_color1)
cv.waitKey()