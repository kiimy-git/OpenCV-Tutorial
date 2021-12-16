import sys
import numpy as np
import cv2

'''
Perspective Transform 투시변환(= Projective Trans, 호모그래피?)
어파인변환(2*3 matrix = 총 6개의 미지수(DOF)) 점 3개
투시변환(3*3 matrix = 총 8개의 미지수(DOF)) 점 4개
==> 자유도가 더 높다 = 평행사변형보다는 임의의 사각형, 사다리꼴 형성가능
== 점(좌표)를 조절하여 원하는 맵핑이 가능
'''

src = cv2.imread('ch05\\images\\namecard.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

# 명함의 비율이 9:5
# 비율에 맞게 출력할 이미지 사이즈 정함
w, h = 810, 450

# 이미지의 각 모서리 좌표
# 좌측상단, 우측상단, 우측하단, 우측하단
srcQuad = np.float32([[325, 307], [760, 369], [718, 611], [231, 515]])

# mapping할 좌표(그래프 확인)
dstQuad = np.float32([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]])

# cv2.getPerspectiveTransform(src, m)
# cv2.warpPerspective(src, M, dsize, dst=None, flags=보간법(interpolation), 
# borderMode=None, borderValue=None
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (w,h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()