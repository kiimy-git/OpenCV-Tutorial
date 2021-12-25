import sys
import numpy as np
import cv2


# 입력 영상 불러오기
src = cv2.imread('ch08\\images\\nemo.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

# 사각형 지정을 통한 초기분할
# x, y, w, h
rc = cv2.selectROI(src)

'''
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, iterCount, mode=None)
            -> mask, bgdModel, fgdModel
mode : 보통 cv2.GC_INIT_WITH_RECT 모드로
       초기화하고, cv2.GC_INIT_WITH_MASK 모드로 업데이트함.
'''
mask = np.zeros(src.shape[:2], np.uint8)
cv2.grabCut(src, mask, rc, None, None, 5, mode=cv2.GC_INIT_WITH_RECT)
# dst1 이미지가 이상하게 나옴
dst1 = src * mask[:, :, np.newaxis]

# mask = 0,1,2,3 네 개의 값으로 구성
# 일반 적인 copyTo에서 사용하는 mask = 0, 255 두 개의 값을 가짐
'''
*mask*
BGD = Background 0
FGD = foward 1
PR BGD = 확률 2
PR FGD = 확률 3
'''
# mask 행렬에서 값이 0 또는 2인 원소는 0으로, (background)
# 그렇지 않은 원소는 1로 설정 (foward)
mask2 = np.where((mask==0) | (mask==2), 0, 1).astype('uint8')
dst2 = src * mask2[:, :, np.newaxis] # mask2= 0,1을 가진 mask

cv2.imshow('src', src)
# mask 0,1,2,3 값을 가진 grayscale 상수를 곱해줌으로써 이미지확인
cv2.imshow('mask', mask* 32)
cv2.imshow('mask2', mask2* 32)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()