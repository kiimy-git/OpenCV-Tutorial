import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt


src = cv2.imread('ch03\\images\\Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# histogram stretching
# 물체가 분간이 잘 되냐 안되냐를 판단할때
# contrast를 올리는 기법은 어떤 영상을 시스템에 입력으로 주기전에 전처리 과정으로서 사용
# 영상의 히스토그램이 그레이스케일 전 구간에서 걸쳐 나타나도록 변경하는 선형 변환 기법

# gmin, gmax, _, _ = cv2.minMaxLoc(src)
# min, max를 구해서 구하기
gmin = np.min(src)
gmax = np.max(src)
# numpy사용하여 기울기, y 절편구하기( pdf 사진 참고)/ 실수형태이니 .astype
# dst = ((src - gmin) * 255. / (gmax - gmin)).astype(np.uint8)

'''
*정규화*
특정 영역에 몰려 있는 경우 화질을 개선하기도 하고, 
이미지 간의 연산 시 서로 조건이 다른 경우 같은 조건으로 만들기도 한다.
'''
# cv2.normalize(입력 배열, 결과 배열, alpha, beta, 정규화 기준)
# cv2.NORM_MINMAX을 통해, 정규화 기준을 최솟값이 alpha가 되고, 최댓값이 beta가 되게 변경
dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
hist = cv2.calcHist([dst], [0], None, [256], [0,256])

cv2.imshow('src', src)
cv2.imshow('dst', dst)
plt.plot(hist)
plt.show()
cv2.waitKey()
