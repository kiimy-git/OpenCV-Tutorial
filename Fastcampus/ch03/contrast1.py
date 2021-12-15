import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

src = cv2.imread('ch03\\images\\lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

'''
dst(x,y) = saturate(s*src(x,y))
s = scala
if s = 0.5
명암은 줄어드는데 어두워짐(pdf 그래프 참조)
if s = 2.0
전체적으로 흰 부분이 많아짐(pdf 그래프 참조)
'''
# 이 연산을 사용해야지만 적절한 contrast를 반영할 수 있다.
# dst(x,y) = saturate(src(x,y) + (src(x,y) - 128) * 알파)

alpha = 1.0 # 커질수록 contrast가 높아짐 
# np.clip(0, 255) = 0보다 작은건 0, 255보다 큰건 255
# 결과값이 실수이니 .astype(np.uint8) 변경

dst = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8)
hist = cv2.calcHist([dst], [0], None, [256], [0,256])
src_hist = cv2.calcHist([src], [0], None, [256], [0,256])


cv2.imshow('src', src)
cv2.imshow('dst', dst)
plt.subplot(211), plt.axis('off'), plt.plot(src_hist, 'gray'), plt.title('src_hist')
plt.subplot(212), plt.axis('off'), plt.plot(hist, 'gray'), plt.title('hist')
plt.show()