import cv2
import sys
import matplotlib.pyplot as plt


src1 = cv2.imread('ch03\\images\\kids1.png')
src2 = cv2.imread('ch03\\images\\kids2.png')
mask = cv2.imread('ch03\\images\\kids1_mask.bmp', cv2.IMREAD_GRAYSCALE)
print(mask.shape) # grayscale로 안불러오면 d= 3

if src1 is None or src2 is None or mask is None:
    print('Image load failed')
    sys.exit()

# 임의의 색을 추출하기위한 변환
src1_ycrcb = cv2.cvtColor(src1, cv2.cv2.COLOR_BGR2YCrCb)
src2_ycrcb = cv2.cvtColor(src2, cv2.cv2.COLOR_BGR2YCrCb)

channels = [1,2]
histSize = [128, 128]
ranges = [0,256,0,256] # Cr, Cb 범위 지정

# *mask = 특정영역(mask)에서만 Histogram을 계산하고 싶다면*
# histsize = 픽셀의 범위는 0 ~ 255
# ranges = 픽셀 범위의 값들을 계산하기위함
hist = cv2.calcHist([src1_ycrcb], channels, mask, histSize, ranges)

# cv2.normalize(hist)
# cv2.normalize(cv2.log(hist + 1)) 
# = Histogram이 큰 애들은 너무 큰 값이 나오기 때문에 큰 몇개의 픽셀만 밝게 나옴
# = 나머지는 0에 가까운 검정색이 나옴. so, log값이 0이 나올수 있으니 +1을 해줌
# hist = plot / 이걸 영상으로 보고 싶으면 normalize를 진행
# dst 입력으로 X = None
hist_norm = cv2.normalize(cv2.log(hist+1), None, 0, 255, \
                            cv2.NORM_MINMAX, cv2.CV_8U)# cv2.CV_8U default

backproj = cv2.calcBackProject([src1_ycrcb], channels, hist, ranges, 1)
backproj2 = cv2.calcBackProject([src2_ycrcb], channels, hist, ranges, 1)

# cv2.imshow('src1', src1)
# cv2.imshow('src2', src2)
cv2.imshow('mask', mask)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('backproj', backproj)
cv2.imshow('backproj', backproj2)
plt.imshow(hist_norm)
plt.show()
cv2.waitKey()