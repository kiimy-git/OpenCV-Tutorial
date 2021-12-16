import sys
import numpy as np
import cv2


src = cv2.imread('ch05\\images\\tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0, 200],
                [0, 1, 100]], dtype=np.float32)

aff1 = np.float32([[1, 0, 200],
                   [0, 1, 100]])

# cv2.warpAffine(src, M, dsize)
# 가로로 200pixel, 세로로 100pixel 이동했다.
dst = cv2.warpAffine(src, aff, (0,0))
dst1 = cv2.warpAffine(src, aff1, (0,0))

# Shear(전단 변환)
# array 변경
# m = 0.5, 값이 커질수록 더 x축으로 더 길게 늘어남(공식)
aff_shear = np.float32([[1, 0.5, 0],
                        [0, 1, 0]])
(h,w) = src.shape[:2]
# *크기 지정은 정수형태로*
# dst_shear1은 불러온 영상 크기와 같기 때문에 짤림
# ==> h(세로)는 고정 w(가로) 늘리기
dst_shear = cv2.warpAffine(src, aff_shear, (w + int(h*0.5), h))
dst_shear1 = cv2.warpAffine(src, aff_shear, (0,0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst1', dst1)
cv2.imshow('dst_shear', dst_shear)
cv2.imshow('dst_shear1', dst_shear1)
cv2.waitKey()