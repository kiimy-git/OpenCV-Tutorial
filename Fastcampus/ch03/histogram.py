import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

src = cv2.imread('ch03\\images\\lenna.bmp', cv2.IMREAD_GRAYSCALE)

'''
이미지에서 사용하는 히스토그램은 
X 축을 픽셀의 값으로 사용하고 Y 축을 해당 픽셀의 개수로 표현

빈도 수(BINS): 히스토그램 그래프의 X 축 간격
차원 수(DIMS): 히스토그램을 분석할 이미지의 차원
범위(RANGE): 히스토그램 그래프의 X 축 범위

*히스토그램을 통해 연산된 결과는 정규화되지 않은 값*
'''
if src is None:
    print('Image load failed!')
    sys.exit()

# cv2.calcHist([여러장의 이미지list= 한장이이라도 list 묶어줘야함])
# cv2.calcHist(연산 이미지, 특정 채널, 마스크, 히스토그램 크기, 히스토그램 범위)
hist = cv2.calcHist([src], [0], None, [256], [0,256])

cv2.imshow('src', src)
# cv2.imshow('hist', hist) 안나옴
# cv2.waitKey(1) # plt.show 사용시 생략가능 

plt.plot(hist) # 분포 그래프를 보여줘야함 plot()
plt.show()

#############################################################

# color 영상의 히스토그램
src1 = cv2.imread('ch03\\images\\lenna.bmp')

colors = ['b', 'g', 'r'] # plot color
bgr_planes = cv2.split(src1)

# BGR을 각각 보여줘야하니 for, zip 
for (p, c) in zip(bgr_planes, colors):
    hist_color = cv2.calcHist([p], [0], None, [256], [0,256])
    plt.plot(hist_color, color=c)

cv2.imshow('src1', src1)
plt.show()


# numpy histogram(opencv 그리기 함수 사용)
def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)

    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist

# histImg = getGrayHistImage(hist)
# cv2.imshow('histImg', histImg)
# cv2.waitKey()