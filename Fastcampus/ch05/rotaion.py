import sys
import math
import numpy as np
import cv2

# Rotation = 문서 이미지 OCR 성능을 향상시키기 위함

src = cv2.imread('ch05\\images\\tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# 직접 구현 code
# radian = degree * (pi / 180)
# degree(양수) = 반시계방향
# degree(음수) = 시계방향
rad = 20 * (np.pi / 180)


# 보통 영상의 중심점을 잡고 회전을 시킴
# 회전 절차 확인(.pdf)
aff = np.float32([[np.cos(rad), np.sin(rad), 0],
                  [-np.sin(rad), np.cos(rad), 0]])

dst = cv2.warpAffine(src, aff, (0,0))

# cv2.getRotationMatrix2D(center, angle, scale)
# scale = 영상의 크기 조절
(h,w) = src.shape[:2]
center = (h / 2, w/2)
rot = cv2.getRotationMatrix2D(center, 20, 1)
dst1 = cv2.warpAffine(src, rot, (0,0)) #dsize = (w,h)

cv2.imshow('src', src)
cv2.imshow('dst', dst) # (0,0)기준으로 회전
cv2.imshow('dst1', dst1)
cv2.waitKey()