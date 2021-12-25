import sys
import numpy as np
import cv2

src1 = cv2.imread('ch10\\images\\frame1.jpg')
src2 = cv2.imread('ch10\\images\\frame2.jpg')

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

gray1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)

# cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance)
# grayscale image만 받음(corner 검출을 위함)
pt1 = cv2.goodFeaturesToTrack(gray1, 50, 0.1, 10)

'''
corners, shape=(N, 1, 2)
maxCorners:  maxCorners <=0 이면 무제한
minDistance : 두 corner가 너무 근접해서 나타나면 하나는 버리겠다.
10 pixel 금방에 있는 것들은 그 중에서 코너해리스가 높은 것만 선택 나머진 버림
'''

pt2, status, err = cv2.calcOpticalFlowPyrLK(src1, src2, pt1, None)
'''
cv2.calcOpticalFlowPyrLK(prevImg, nextImg, prevPts, nextPts, status=None,
                        err=None, winSize=None, maxLevel=None, criteria=None, flags=None, 
                        minEigThreshold=None) -> nextPts, status, err

prevPts: 이전 프레임에서 추적할 점들. shape=(N, 1, 2), dtype=np.float32
nextPts: 출력으로 받음(pt2)
status: 점들의 매칭상태. shape=(N,1)
        i번째 원소가 1이면 prevPts의 i번째 점이 nextPts의 i번째 점으로 이동
'''

dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)

for i in range(pt2.shape[0]): # corner 개수
    # 잘 된것만 표현해주기 위함
    if status[i,0] == 0: # status.shape= (34,1)
        continue

    # 도형그릴땐 int값만 받음
    # error: only size-1 arrays can be converted to Python scalars
    '''
    pt1, pt2 = [[[1,2], [2,4], ...]]
    각 좌표성분이 들어가 있는데
    *각 좌표 접근방법*
    ==> pt1[1, 0] = 첫번째 좌표 
    '''
    cv2.circle(dst, (pt1[i,0]).astype(int), 4, (0,255,255), 2, cv2.LINE_AA)
    cv2.circle(dst, (pt2[i,0]).astype(int), 4, (0,0,255), 2, cv2.LINE_AA)
    cv2.arrowedLine(dst, (pt1[i,0]).astype(int), (pt2[i,0]).astype(int), (0,255,0), 2)

cv2.imshow('dst', dst)
cv2.waitKey()