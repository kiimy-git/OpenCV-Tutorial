import sys
import numpy as np
import cv2
'''
이미지의 히스토그램이 특정영역에 너무 집중되어 있으면 contrast가 낮아 좋은 이미지라고 할 수 없다.
전체 영역에 골고루 분포가 되어 있을 때 좋은 이미지라고 할 수 있다.

= 앞서 설명한 정규화는 분포가 한곳에 집중되어 있는 경우에는 효과적이지만 
  그 집중된 영역에서 멀리 떨어진 값이 있을 경우에는 효과가 없다.
  평탄화는 각각의 값이 전체 분포에 차지하는 비중에 따라 분포를 재분배하므로 명암 대비를 
  개선하는 데 효과적
'''

# grayscale 영상의 히스토그램 평활화
# normailzed와 equalizeHist 차이
# normalized = contrast가 커짐
# equalizeHist = 밝은 부분과 어두운부분 명확해짐

src = cv2.imread('ch03\\images\\Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.equalizeHist(src)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

# color 영상 히스토그램 평활화
# 분할해서 각각 진행
'''
BGR 색공간에서는 밝기성분을 표현할 수 없기 때문에 평활화를 할 수 없다. 
따라서, 컬러 영상에서 히스토그램 평활화를 하기 위해서는 색공간을 변경해야한다. 
YCrCb 색공간에서 Y는 밝기성분만을 가지고 있으므로 이를 활용한다.
'''

src_color = cv2.imread('ch03\\images\\field.bmp')

# Y: 밝기 정보
# Cr,Cb : red와 blue(밝기정보Y와 대비했을 때의 차이) = 색차정보
# Green? == red, blue를 합치면 green을 만들 수 있다
src_ycrcb = cv2.cvtColor(src_color, cv2.COLOR_BGR2YCrCb)
y, cr, cb = cv2.split(src_ycrcb)
planes = cv2.split(src_ycrcb)
print(planes[0])
print(y)
print(src_ycrcb[:, :, 0])

# 밝기 성분에 대해서만 히스토그램 평활화 수행
dst_y = cv2.equalizeHist(y)
# planes[0] = cv2.equalizeHist(planes[0])

# 평활화 진행 후 merge(YCrCb ==> BGR 변경)
dst_ycrcb = cv2.merge([dst_y, cr, cb])
dst_final = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src_color', src_color)
cv2.imshow('dst_ycrcb', dst_ycrcb)
cv2.imshow('dst_final', dst_final)
cv2.imshow('planes[0]', planes[0])
cv2.waitKey()
'''
*why?*
planes = cv2.split(src_ycrcb)
planes[0] = cv2.equalizeHist(planes[0])
TypeError: 'tuple' object does not support item assignment
'''
