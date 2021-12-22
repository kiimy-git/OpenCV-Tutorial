import sys
import numpy as np
import cv2


# 영상 불러오기
# obj = spade만 골라내는 것이 목적
obj = cv2.imread('ch08\\images\\spades.png', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('ch08\\images\\symbols.png', cv2.IMREAD_GRAYSCALE)

if src is None or obj is None:
    print('Image load failed!')
    sys.exit()

# 객체 영상 외곽선 검출
# 객체가 검은색이라 흰색으로 INV
_, obj_bin = cv2.threshold(obj, 128, 255, cv2.THRESH_BINARY_INV)
obj_contours, _ = cv2.findContours(obj_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
obj_pts = obj_contours[0]
print(obj_contours) # int32 
# 입력 영상 분석
_, src_bin = cv2.threshold(src, 128, 255, cv2.THRESH_BINARY_INV)
src_contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 결과 영상(bbox 색 보여주기위함)
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# 입력 영상의 모든 객체 영역에 대해서
# contours= 각 점들의 집합
# pts= 객체 하나의 외곽선
for pts in src_contours:
    # noise를 제거하기 위함(spade 밖에 없기 때문에 굳이 사용은 안해도되)
    if cv2.contourArea(pts) < 1000:
        continue

    rc = cv2.boundingRect(pts)
    print(rc[0], rc[1]) # x, y
    cv2.rectangle(dst, rc, (0,0,255), 1)

    # 모양 비교
    # dist = 두 객체 상당히 비슷하다 작은값, 차이가 크다(큰값) = distance
    dist = cv2.matchShapes(obj_pts, pts, cv2.CONTOURS_MATCH_I3, 0)
    print(dist)
    '''
    투시변환 or 찌그러진 이미지에서는 성능이 떨어진다.
    '''
    cv2.putText(dst, str(round(dist, 4)), (rc[0], rc[1]-3),\
         cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1, cv2.LINE_AA)

    if dist < 0.1:
        cv2.rectangle(dst, rc, (0,0,255), 2)

cv2.imshow('obj', obj)
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()