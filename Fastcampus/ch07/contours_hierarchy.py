import sys
import random
import numpy as np
import cv2


src = cv2.imread('ch07\\images\\contours.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

contours, hier = cv2.findContours(src, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
'''
cv2.findContours(image, mode, method, contours=None, hierarchy=None, 
                offset=None) -> contours, hierarchy
mode = cv2.RETR_EXTERNAL(바깥 외곽선만 검출)

contours = shape=(k,1,2), len(contours)=전체 외곽선 개수(N)
hierarchy = shape=(1,N,4) hierarchy[0, i, 0] ~ hierarchy[0, i, 3]
          = next, prev, child, parent
'''
# bbox 색으로 보여주기위함
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# 내부 구조를 개별적으로 파악하기 위함
idx = 0
while idx >=0:
    # color 각각의 색 random
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 외곽에 있는 것만 그림
    # idx = 특정 윤관석만 그리고 싶다면 정수로 지정
    cv2.drawContours(dst, contours, idx, c, 2, cv2.LINE_8)
    # 다 그림(mode = cv2.RETR_LIST의 경우는 설정 안해도 다 그림)
    # cv2.drawContours(dst, contours, idx, c, 2, cv2.LINE_AA, hier)

    # idx 업데이트 next
    idx = hier[0, idx, 0]


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()