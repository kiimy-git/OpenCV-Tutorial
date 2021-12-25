import sys
import numpy as np
import cv2


# 기준 영상 불러오기
# src1 = cv2.imread('ch09\\images\\graf1.png', cv2.IMREAD_GRAYSCALE)
# src2 = cv2.imread('ch09\\images\\graf3.png', cv2.IMREAD_GRAYSCALE)
src1 = cv2.imread('ch09\\images\\box.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('ch09\\images\\box_in_scene.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

feature = cv2.KAZE_create()
#feature = cv2.AKAZE_create()
#feature = cv2.ORB_create()

kp1, desc1 = feature.detectAndCompute(src1, None)
kp2, desc2 = feature.detectAndCompute(src2, None)

matcher = cv2.BFMatcher_create()
#matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING)
matches = matcher.match(desc1, desc2)

matches = sorted(matches, key=lambda x: x.distance)
good_matches = matches[:60]

# 호모그래피 계산
# good_matches = 80개의 특징점
# m = DMathch의 tpye
# DMathch라는 클래스에는 queryIdx와 trainIdx가 멤버가 있다.
# pt= kp1[m.queryIdx]의 좌표 (80,2) float64

# cv2.findHomography 사용 할려면 shape=(N, 1, 2) 변경
pts1 = np.array([kp1[m.queryIdx].pt for m in good_matches]
                ).reshape(-1,1,2).astype(np.float32)
pts2 = np.array([kp2[m.trainIdx].pt for m in good_matches]
                ).reshape(-1,1,2).astype(np.float32)

# H = perspective transform 정보를 가지고 있는 행렬
H, M = cv2.findHomography(pts1, pts2, cv2.RANSAC)
'''
cv2.findHomography(srcPoints, dstPoints, method=None, 
                    ransacReprojThreshold=None, mask=None, maxIters=None, 
                    confidence=None) -> retval, mask

• srcPoints: 입력 점 좌표. numpy.ndarray. shape=(N, 1, 2). dtype=numpy.float32. 
• dstPoints: 결과 점 좌표. numpy.ndarray. shape=(N, 1, 2). dtype=numpy.float32.

retval: 호모그래피 행렬. numpy.ndarray. shape=(3, 3). dtype=numpy.float32.
mask: 출력 마스크 행렬. RANSAC, RHO 방법 사용 시 Inlier로 사용된
      점들을 1로 표시한 행렬. numpy.ndarray. shape=(N, 1), dtype=uint8
      inliers = 두 특징점이 매칭된 것은 1, 아닌 것은 0으로

'''
# 호모그래피를 이용하여 기준 영상 영역 표시
# 두 이미지가 가로로 합쳐져서 나옴
# flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS(매칭되는 점이 아는 건 버림)
dst = cv2.drawMatches(src1, kp1, src2, kp2, good_matches, None,
                        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

dst2 = cv2.drawMatches(src1, kp1, src2, kp2, good_matches, None)

# Perspective
(h,w) = src1.shape[:2]
corners1 = np.array([[0,0], [0, h-1], [w-1, h-1], [w-1,0]] #(4,2)
                    ).reshape(-1,1,2).astype(np.float32) #(4,1,2)
# 점들을(H라는 행렬) 어디로 좌표가 이동하는지
# H.shape = (4, 1, 2)
perspective = cv2.perspectiveTransform(corners1, H)

# 합쳐져서 나오니까 이미지1의 가로 길이만큼 shift시킨다
perspective = perspective + np.float32([w,0])
cv2.polylines(dst, [np.int32(perspective)], True, (0,255,0), 2, cv2.LINE_AA)

cv2.imshow('src1', src1)
cv2.imshow('src2', src2)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()
