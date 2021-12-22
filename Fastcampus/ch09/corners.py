import sys
import numpy as np
import cv2

# cv2.cornerHarris(src, blockSize, ksize, k)
'''
• blockSize: 코너 응답 함수 계산에서 고려할 이웃 픽셀 크기. 보통 2~5.
• ksize: (미분을 위한) 소벨 연산자를 위한 커널 크기. 보통 3.
• k: 해리스 코너 검출 상수 (보통 0.04~0.06)
'''
# 잘 안씀
src = cv2.imread('ch09\\images\\building.jpg', cv2.IMREAD_GRAYSCALE)

tm = cv2.TickMeter()
tm.start()

corners = cv2.goodFeaturesToTrack(src, 400, 0.01, 10)
tm.stop()
print('GFTT: {}ms.'.format(tm.getTimeMilli()))
'''
cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, 
                        corners=None, mask=None, blockSize=None, 
                        useHarrisDetector=None, k=None) -> corners

corners: 검출된 코너점 좌표. numpy.ndarray. shape=(N, 1, 2), numpy.float32
maxCorners:  maxCorners <=0 이면 무제한
minDistance : 두 corner가 너무 근접해서 나타나면 하나는 버리겠다.
10 pixel 금방에 있는 것들은 그 중에서 코너해리스가 높은 것만 선택 나머진 버림
corners = np.float32 이기 때문에 혹시라도 화면으로 출력해보고싶다면
int tpye으로 conversion해서 opencv draw 함수에 넣어주면 됨
'''
dst1 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
if corners is not None:
    for i in range(corners.shape[0]): # shape = (N, 1, 2), 2= x,y[0,1]
        pt = (int(corners[i,0,0]), int(corners[i,0,1]))
        cv2.circle(dst1, pt, 5, (0,0,255))

# reset 안하면 이전 tm 시간에 + 하게됨
tm.reset()
tm.start()

fast = cv2.FastFeatureDetector_create(60)
'''
cv2.FastFeatureDetector_create(, threshold=None, nonmaxSuppression=None, 
                                type=None) -> retval

threshold: 중심 픽셀 값과 주변 픽셀 값과의 차이 임계값. 기본값은 10.
= p점을 기준으로 해서 충분히 밝은 값 (30 ~ 60)
= ex) p값보다 50보다 더 밝은 것들이 9개 이상 나타나면 corner로 판단하겠다

nonmaxSuppression: 비최대 억제 수행 여부. 기본값은 True.
type: 코너 검출 방법. 기본값은 cv2.FAST_FEATURE_DETECTOR_TYPE_9_16.
= 주변 16개 pixel중에 9개 이상 연속적으로 더 밝고 어두운게 나타나면 corner로 검출하겠다
'''
# cv2.KeyPoint
keypoints = fast.detect(src)
'''
keypoints: (출력) 검출된 코너점 정보. cv2.KeyPoint 객체를 담은 리스트.
                  cv2.KeyPoint의 pt 멤버를 이용하여 코너 좌표 추출.
                  pt[0]은 x좌표, pt[1]은 y좌표.
'''
tm.stop()
print('FAST: {}ms.'.format(tm.getTimeMilli()))

dst2 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
for kp in keypoints:
    pt = (int(kp.pt[0]), int(kp.pt[1]))
    cv2.circle(dst2, pt, 5, (0,0,255))

cv2.imshow('src', src)
cv2.imshow('dst1', dst1) # GFTT가 성능이 더 좋음
cv2.imshow('dst2', dst2) # 빠름
'''
• FAST 방법의 반복 검출률이 대체로 높음
• 다만 FAST 방법은 노이즈에 민감함
'''
cv2.waitKey()
