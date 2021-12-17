import sys
import numpy as np
import cv2


src = cv2.imread('ch06\\images\\lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()
# Gradient = 따로 미분을 하고 합치는 과정
# Gradient를 사용하기위해 float로 변환하는 것이 좋음
# delta 제거 (연산을 위함)
dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

# 2D 벡터의 크기 계산
# 후에 이 크기가 내가 정한 Threshold보다 큰 부분을 엣지라고 판단
mag = cv2.magnitude(dx, dy) # --> float 형태 so, imshow하면 흰부분으로 나옴
mag = np.clip(mag, 0, 255).astype(np.uint8)
print(mag)
'''
# 2D 벡터의 방향계산 = Canny에서 사용됨
pha = cv2.phase(dx, dy, angle=, angleInDegrees=)
angleInDegrees= True이면 angle 단위, False이면 radian 단위
'''

# Threshold 설정
dst = np.zeros(src.shape[:2], np.uint8)
dst[mag > 120] = 255 # edge 부분만 흰색으로 나머진 검은색
#_, dst = cv2.threshold(mag, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('src', src)
cv2.imshow('mag', mag) # 밝은 회색, 어두운 색 다 나옴

# 120보다 큰 값은 255를 줬기 때문에 원하는 부분만 흰색edge 부여가능
# edge가 두껍게 나오는데 == canny를 사용함
cv2.imshow('dst', dst)
cv2.waitKey()