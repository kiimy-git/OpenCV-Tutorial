import sys
import numpy as np
import cv2


src = cv2.imread('ch04\\images\\rose.bmp', cv2.IMREAD_GRAYSCALE)

# ksize = (8시그마 +1) or (6시그마 + 1)
'''
(0, 0)을 지정하면 sigma 값에 의해 자동 결정됨
'''
# (8시그마 +1) = float type, +-4 sigma
# (6시그마 + 1) = uint8, +-3 sigma
# sigmax= 1, ksize가 자동으로 설정됨= 값이 커지면 더 blur처리됨

# cv2.GaussianBlur(src, ksize, sigmaX)
# sigmax= 1, ksize가 자동으로 설정됨= 값이 커지면 더 blurring 됨
dst = cv2.GaussianBlur(src, (0,0), sigmaX= 3)

# blur( mean filter)의 경우 line(edge?)이 부드럽게 blur처리가 되지 않아
dst2 = cv2.blur(src, (7,7))

for sigma in range(1,6):
    dst_sigma= cv2.GaussianBlur(src, (0,0), sigma)
    text = f'sigma = {sigma}'
    cv2.putText(dst_sigma, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, 255, 1, cv2.LINE_AA)

    cv2.imshow('dst_sigma', dst_sigma)
    cv2.waitKey()

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.imshow('dst2', dst2)
# cv2.waitKey()