import cv2 as cv
import sys
import numpy as np
import matplotlib.pyplot as plt

# 산술연산(Arithmetic)

img1 = cv.imread('ch03\\images\\lenna256.bmp', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('ch03\\images\\square.bmp', cv.IMREAD_GRAYSCALE)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()

# cv2.add(src1, src2, dst=None, mask=None, dtype=None)
# mask= 픽셀값이 0이 아닌 부분에 대해서만 덧셈 연산이 된다
# dtype = src1, src2가 보통 tpye이 같아야하는데 이것을 동일하게 해줌
# ==> numpy가 아니라 opencv의 flag를 써야함 cv2.CV_8U ...

# img2 검은 부분은 더해도 원래 의미가 없기 때문에 img1부분만 가져오고
# img2 흰 부분(값 = 255)를 더하면 해당 부분을 255으로 출력
dst1 = cv.add(img1, img2, dtype=cv.CV_8U)

# cv.addWeighted = img1의 가중치 , img2의 가중치
# 두 이미지의 가중치 합은 되도록 1로 설정 => 두 입력 영상의 평균 밝기를 유지
dst2 = cv.addWeighted(img1, 0.5, img2, 0.5, 0)

# cv.substract 
# 색이 있는 이미지는 보통 255에 가까운 색(특히 gray) - 가운데 검은색 이미지(0)
# 순서가 중요함
dst3 = cv.subtract(img1, img2)

# cv.absdiff = 절대값
# 뺄셈 연산과 달리 입력 영상의 순서에 영향을 받지 않음
# ==> 정상 이미지(img1), 어떤 객체가 추가된 이미지(img2)
# ==> 추가된 객체를 반환
dst4 = cv.absdiff(img1, img2)

# cv.imshow('img1', img1)
# cv.imshow('img2', img2)
# cv.imshow('dst1', dst1)
# cv.imshow('dst2', dst2)
# cv.imshow('dst3', dst3)
# cv.imshow('dst4', dst4)
plt.subplot(231), plt.axis('off'), plt.imshow(img1, 'gray'), plt.title('img1')
plt.subplot(232), plt.axis('off'), plt.imshow(img2, 'gray'), plt.title('img2')
plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('add')
plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('addweight')
plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('substract')
plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('absdiff')
plt.show()