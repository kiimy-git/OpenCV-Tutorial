import sys
import numpy as np
import cv2

# Otsu = Threshold 값을 자동으로 잡아줌
src = cv2.imread('ch07\\images\\rice.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# cv2.THRESH_BINARY는 생략가능 (default)
th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print("otsu's threshold:", th)  # 131(실수형태로 나옴)

cv2.imshow('src', src)
cv2.imshow('dst', dst) 
# 잘 안나오는 부분이 있음 = 지역이진화로 처리 가능
# 원래 이미지에서 약간 어두운 부분은 잘 안나옴(= 이미지 불균일)
# Threshold를 낮추면 잘 보이는데 원래 보이는 것들이 잘안보임 
cv2.waitKey()