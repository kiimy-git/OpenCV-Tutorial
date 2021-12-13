import sys
import numpy as np
import cv2 
import matplotlib.pyplot as plt

src = cv2.imread('ch03\\images\\candies.png')
# HSV, YCrCb를 더 유용하게 사용함
# YCrCb(Y: 밝기 정보(luma), Cr,Cb: 색차(chroma))

if src is None:
    print('Image load failed!')
    sys.exit()

print('src.shape:', src.shape) # 세로 * 가로 (480, 640, 3)
print('src.dtype:', src.dtype)  # src.dtype: uint8
plt.imshow(src)
plt.show()

# RGB 색 평면 분할
b_plane, g_plane, r_plane = cv2.split(src)
# planes = cv2.split(src)
# planes[0], planes[1], planes[2] 이렇게 불러올 수도 있음
# B, G, R
'''
#b_plane = src[:, :, 0]
#g_plane = src[:, :, 1] 
#r_plane = src[:, :, 2]
G, R 
==> 노란색도 선명(흰색)하게 나오는 이유는 유난히 밝기 때문
G = 녹색과 빨간색을 합치면 노란색이 됨
R = 마찬가지
'''

cv2.imshow('src', src)
cv2.imshow('b_plane', b_plane)
cv2.imshow('g_plane', g_plane)
cv2.imshow('r_plane', r_plane)
cv2.waitKey()