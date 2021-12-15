import sys
import numpy as np
import cv2

# sharpening edge 강조(Contrast 조절과 비슷)
# g(x) = 2f(x) - f1(x)
src = cv2.imread('ch04\\images\\rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

blr = cv2.GaussianBlur(src, (0, 0), 2)
# 그래프에서 양수 부분만 보임
# 그래프 음수 부분도 보이게 할려면 addweigthed
subtract = cv2.subtract(src, blr)

# gamma = 결과를 눈에 잘 보이게 하기 위함 값
# 가중치 부여
# g(x) = 2f(x) - f1(x)
addweighted = cv2.addWeighted(src, 2, blr, -1, 1)

# *np.clip의 내부 연산은 float로 해줘야함(2.0)*
# np.clip = float64 / 변환필요
dst = np.clip(2.0*src - blr, 0, 255).astype(np.uint8)

cv2.imshow('blr', blr)
cv2.imshow('subtract', subtract)
cv2.imshow('addweighted', addweighted)
cv2.imshow('dst', dst)
cv2.waitKey()