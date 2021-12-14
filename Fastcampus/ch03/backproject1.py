import cv2
import sys
import matplotlib.pyplot as plt

src = cv2.imread('ch03\\images\\cropland.png')

if src is None:
    print('Image load failed')
    sys.exit()

# ROI 창 생성(드래그 할 수 있음) / spacebar 누르면 ROI 적용됨
x, y, w, h = cv2.selectROI('ROI', src)
print(x, y, w, h)

# Histogram(RGB가 아닌 YCrCb가 임의의 색추출에 용의)
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
crop = src_ycrcb[y:y+h, x:x+w] # ROI 

channels = [1,2] # Y: 밝기 정보라 필요 X(Cr, Cb)
cr_bins = 128 # 0~255, 266을 써야하지만 128( 결과는 비슷함 )
cb_bins = 128
histsize = [cr_bins, cb_bins]
cr_range = [0,256] # 256 = 255까지의 값이기 때문에 
cb_range = [0,256]
ranges = cr_range + cb_range
print(ranges)

hist = cv2.calcHist([crop], channels, None, histsize, ranges, cv2.CV_8U)
hist_norm = cv2.normalize(cv2.log(hist+1), None, 0, 255, cv2.NORM_MINMAX)

# 입력 영상 전체에 대해 히스토그램 역투영

# cv2.calcBackProject = cv2.calcHist와 인자값이 비슷하다
# 하지만 calcHist는 Histogram을 출력으로 내주는 것이고
# calcBackProject는 calcHist를 입력으로 받고 그 histogram과 부합되는 영역만
# 0보다 큰 값으로 되있는 확률과 같은 개념의 이미지를 반환
# backproj = grayscale 
backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)
dst = cv2.copyTo(src, backproj) 
# cv2.copyTo : ROI를 지정한 backproj(grayscale) = 흰 부분만 가져오기

cv2.imshow('image', src)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('backproj', backproj)
cv2.imshow('dst', dst)
cv2.waitKey()