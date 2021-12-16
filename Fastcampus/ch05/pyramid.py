import sys
import numpy as np
import cv2

'''
영상 축소시 디테일이 사라지는 경우 발생
= 입력 영상을 부드럽게 filtering한 후 축소(다단계축소)
= cv2.resize(interpolation=cv2.INTER_AREA) 사용
= cv2.pyrDown, pyrUp = 5*5 Gaussianblur 적용됨
'''

src = cv2.imread('ch05\\images\\cat.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# x, y, w, h
rc = (250, 120, 200, 200)  # rectangle tuple
'''
그림
x,y 기준으로 w = (x+200), y = (y+200)
'''

# 사본 영상에 그리기(객체 찾기)
src_copy = src.copy()
cv2.rectangle(src_copy, rc, (0,0,255), 1)

'''
어떤 객체를 찾고 싶을 때 객체 크기는 다양하다
*방법*
1. 객체의 크기를 다양화
2. 이미지 크기를 resize해가면서 여러번 객체를 찾는다.
ex) 고양이 얼굴 크기를 100*100으로 설정
    but 입력 이미지의 고양이 얼굴 크기가 큰 경우
    내가 설정한 100*100으로는 고양이 얼굴을 찾을 수가 없다.
'''
for i in range(1, 4):
    src = cv2.pyrDown(src)
    cpy = src.copy()
    # shift = 이미지가 downsampling되면 사각형이 같이 작아짐
    # 마지막 이미지의 잔상이 남음(cv2.destroyWindow() 설정)
    cv2.rectangle(cpy, rc, (0,0,255), 1, shift=i)
    cv2.imshow('src', cpy)
    cv2.waitKey()
    # cv2.destroyWindow('src')

cv2.imshow('src_copy', src_copy)
cv2.waitKey()