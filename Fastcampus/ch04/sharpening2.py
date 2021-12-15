import sys
import numpy as np
import cv2

# color 영상

src = cv2.imread('ch04\\images\\rose.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)


# 밝기정보만 가우시안블러
src_f = src_ycrcb[:,:,0].astype(np.float32) 
# float32 why?
# 중간 연산의 과정을 float로 해줘야하는 이유
# GaussianBlur의 출력영상 type은 입력영상의 tpye과 같게 설정됨
# if uint8의 경우 GaussianBlur의해서 나타나는 출력영상은 소수점 아래가 다짤림
# == 정수형태로 변환되기 때문에 미세한 변화가 사라져
blr = cv2.GaussianBlur(src_f, (0,0), 2.0) # 흰색??

# 최종적으로 화면에 보여지기 위한 영상을 만들때 다시 uint8로 변환
src_ycrcb[:,:,0] = np.clip(2.0*src_f - blr, 0, 255).astype(np.uint8)
dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('src_ycrcb', src_ycrcb)
cv2.imshow('src_f', src_f)
cv2.imshow('blr', blr)
cv2.imshow('dst', dst)
cv2.waitKey()