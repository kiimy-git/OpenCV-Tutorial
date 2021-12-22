import numpy as np
import sys
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

kp1, desc1 = feature.detectAndCompute(src1, None)
kp2, desc2 = feature.detectAndCompute(src2, None)

matcher = cv2.BFMatcher_create()
# 이진 기술자의 경우
# matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING)
matches = matcher.knnMatch(desc1, desc2, 2) # 잘 매칭된 두개를 불러온다
# [[DMatch], [DMatch]] 형태

'''
가장 좋은 매칭 결과의 distance 값과 두 번째로 좋은 매칭 결과의 
distance 값의 비율을 계산
'''
good_matches = []
for m in matches:
    # [0] 값이 작고 / [1] 값이 큼
    # (<DMatch 0000025608092BF0>, <DMatch 0000025608092C10>) ....
    if m[0].distance / m[1].distance < 0.7: # 비율이 임계값(e.g. 0.7)보다 작으면 선택
        good_matches.append(m[0])

print('# of kp1:', len(kp1))
print('# of kp2:', len(kp2))
print('# of matches:', len(matches))
print('# of good_matches:', len(good_matches))

# 잘못된 매칭이 간혹 보이는데 호모그래피 사용하여 보완
dst = cv2.drawMatches(src1, kp1, src2, kp2, good_matches, None)

cv2.imshow('dst', dst)
cv2.waitKey()