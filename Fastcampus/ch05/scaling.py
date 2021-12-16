import sys
import numpy as np
import cv2

src = cv2.imread('ch05\\images\\rose.bmp') 

if src is None:
    print('Image load failed!')
    sys.exit()

# src.shape=(320, 480) h*w
# resize= dsize(w, h)
'''
dsize 절대크기 (0,0) 설정시 fx, fy(상대크기) 무조건 설정
dszie 설정시 fx, fy 설정 필요 없음

interpolation (default: cv2.INTER_LINEAR)
= 결과영상의 퀄리티, 자연스럽냐 부자연스럽냐를 결정짓는 파라미터
= 원래이미지의 pixel 윤곽선을 잘 표현하냐 못 하냐
'''
# dst1 -> dst2 -> dst3 -> dst4(품질이 가장 좋은, but 연산이 오래걸림)
# dst1 = 픽셀자체가 큰 사각형이 된느낌? = 계단현상, 블럭현상
dst1 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (480*4, 320*4)) # cv2.INTER_LINEAR
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1[500:900, 400:800]) # h*w
cv2.imshow('dst2', dst2[500:900, 400:800])
cv2.imshow('dst3', dst3[500:900, 400:800])
cv2.imshow('dst4', dst4[500:900, 400:800])
cv2.waitKey()
