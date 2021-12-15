import sys
import numpy as np
import cv2

# image profile?? 2차원으로 pixle값의 높낮이를 표현한

src = cv2.imread('ch04\\images\\lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# 가우시안 노이즈를 제거할려면 가우시안 블러를 사용
# but 가우시안 블러를 너무 심하게 블러링하게되면(sigmaX값 크면) edge정보가 무너짐
# so, 양방향 필터를 사용하게됨(edge-preserving noise removal filter)
# 기존 pixel과 이웃 pixel과의 거리(유클리디안?) 그리고 
# pixel 값의 차이를 고려하여 블러링 정도를 조절
'''
edge가 아닌 부분에서만 blurring ==> edge 보존
= pixel이 평탄하면 blurring, edge가 포함된 부분은 가우시안 함수의 일부분만
가져와서 filtering으로 사용 = Gauusian modify

sigma가 커지면 속도가 느려짐 
* why? 
가우시안 필터는 똑같은 모양의 필터마스크를 모든 픽셀에 적용하니 속도가 빠름
but 양방향 필터는
가우시안 필터를 만들고 각각의 픽셀마다 modify를 진행해 모든 픽셀마다 다른 형태의
filter를 만들어서 filtering을 진행
'''

# cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)
'''
d: 필터링에 사용될 이웃 픽셀의 거리(지름). 
음수(-1)를 입력하면 sigmaSpace 값에 의해 자동 결정됨.
sigmaColor: 색 공간에서 필터의 표준 편차
sigmaSpace: 좌표 공간에서 필터의 표준 편차
'''
# sigmaColor = edge를 판단하는 sigma(임계값), 너무크면 가우시안과 별다를게 없음 
# 가우시안 분포에서 +-2~3 sigma 보다 크다면 다른 값, 
#                  +-2~3 sigma 사이면 비슷한 값
# sigmaSpace 값 = filter_mask = 8*sigmaSpace + 1 or 6*sigmaSpace +1
dst = cv2.bilateralFilter(src, d=-1, sigmaColor=10, sigmaSpace=5)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()