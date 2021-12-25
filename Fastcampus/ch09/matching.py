import sys
import numpy as np
import cv2


# 영상 불러오기
src1 = cv2.imread('ch09\\images\\graf1.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('ch09\\images\\graf3.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

feature = cv2.KAZE_create()
# feature = cv2.AKAZE_create()
# feature = cv2.ORB_create()

# 특징점 검출 및 기술자 계산
kp1, desc1 = feature.detectAndCompute(src1, None)
kp2, desc2 = feature.detectAndCompute(src2, None)

# 특징점 매칭
matcher = cv2.BFMatcher_create()
'''
+ BFMatcher_create :  Brute-force (전수 조사)
+ cv2.FlannBasedMatcher : 특징점이 너무 많을 시 사용(근사화)
 ==> 완전히 최소값 매칭이 어려워(속도는 빠름) but 특징점이 몇천개 정도면 별차이 없음
 ==> 영상 사이즈가 너무 커져서 너무느리다 싶으면 사용
# 실수 기술자 KAZE(default = cv2.NORM_L2)
# 이진 기술자 AKAZE, ORB(=cv2.NORM_HAMMING)

*멤버*
+ match()
+ knnMatch()
+ radiusMatch()
'''
matches = matcher.match(desc1, desc2)
'''
cv2.DescriptorMatcher.match(queryDescriptors, trainDescriptors, mask=None)
                            -> matches

• queryDescriptors: (기준 영상 특징점) 질의 기술자 행렬
• trainDescriptors: (대상 영상 특징점) 학습 기술자 행렬
• mask: 매칭 진행 여부를 지정하는 행렬 마스크.
• matches: 매칭 결과. cv2.DMatch 객체의 리스트.

*멤버함수*
+ queryIdx : 기준 영상 특징점(src1)
+ trainIdx : 대상 영상 특징점(src2)
+ imgIdx : 매칭할 영상(src2)를 여러장 줄 수 있는데 그중 가장 비슷한 것을 찾는 형태로 동작
+ distance
'''

print('# of kp1:', len(kp1))
print('# of kp2:', len(kp2))
print('# of matches:', len(matches)) # matching 개수는 kp1

# 특징점 매칭 결과 영상 생성
dst = cv2.drawMatches(src1, kp1, src2, kp2, matches, None)

cv2.imshow('dst', dst)
cv2.waitKey()