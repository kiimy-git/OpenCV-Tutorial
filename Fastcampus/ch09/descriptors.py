import sys
import numpy as np
import cv2


# 영상 불러오기
# src2 = 기울어진 영상
src1 = cv2.imread('ch09\\images\\graf1.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('ch09\\images\\graf3.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

'''
sift = cv2.xfeatures2d.SIFT_create() 좋음
'''
# 특징점 알고리즘 객체 생성 (KAZE, AKAZE, ORB 등)
feature = cv2.KAZE_create() # 방향 성분 x( 0도 )
# feature = cv2.AKAZE_create() # 방향 성분 o
#feature = cv2.ORB_create() # 상당히 빠름
# cv2.ORB_create(1000) 검출할 특징점 개수, default = 500
'''
feature ==> cv2.Feature2D
            detect(), compute(), detectAndCompute()
'''

# 특징점 검출 및 기술자 계산
kp1 = feature.detect(src1)
'''
keypoints= cv2.KeyPoint객체의 리스트
pt, size, angle
pt = x좌표, y좌표 (float)
size= 특징점을 검출할 때 어느정도 주변의 크기로 검출 했냐
angle = 특징점을 검출하고나서 그 특징점 주변영상을(기술자) 계산할때
        방향에 대한 주된 방향성분을 계산해서 그 주된 방향성분만큼 보정한다.
        그리고 특징벡터를 계산, 즉 부분영상의 주된 방향
'''
# 특징점 기술자 계산 함수
_, desc1 = feature.compute(src1, kp1)
'''
-> keypoints, descriptors
'''

# 특징점 검출 및 기술자 계산(detect, compute)
# 이 두가 지가 모두 가능한 class를 사용해야해(Fastfeaturedetector?? = detection만 됨)
# kp1, desc2 = feature.detectAndCompute(src1, None)
kp2, desc2 = feature.detectAndCompute(src2, None)

print('desc1.shape:', desc1.shape) # column의 갯수는 무조건 동일()
print('desc1.dtype:', desc1.dtype)
print('desc2.shape:', desc2.shape)
print('desc2.dtype:', desc2.dtype)

# 검출된 특징점 출력 영상 생성
# for loop 굳이 안돌리고 drawKeypoints 사용
dst1 = cv2.drawKeypoints(src1, kp1, None, 
                        flags= cv2.DRAW_MATCHES_FLAGS_DEFAULT)
dst2 = cv2.drawKeypoints(src2, kp2, None, 
                        flags= cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
'''
cv2.DRAW_MATCHES_FLAGS_DEFAULT
= 특징점 위치만을 표현하는 작은 크기의 원

DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
= 특징점의 크기와 방향을 반영한 원
'''

cv2.imshow('src1', src1)
cv2.imshow('src2', src2)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
