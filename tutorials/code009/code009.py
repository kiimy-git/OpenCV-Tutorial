import cv2 as cv
import numpy as np
import sys

# 모폴로지 연산(Perspective Calculate)은 
# 모폴로지 변환의 팽창(dilation)과 침식(erosion)을 기본 연산으로 사용해 고급 형태학을 적용하는 변환 연산
# 입력 이미지가 이진화된 이미지라면 팽창과 침식 연산으로도 우수한 결과를 얻을 수 있다.
# 하지만, 그레이스케일이나 다중 채널 이미지를 사용하는 경우 더 복잡한 연산을 필요

img = cv.imread('tetris_blocks.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(img_gray, 225, 255, cv.THRESH_BINARY_INV)
if img is None:
    print('Image load failed')
    sys.exit()

kernel = np.ones((5,5), np.uint8)

# cv2.morphologyEx(원본 배열, 연산 방법, 구조 요소, 고정점, 반복 횟수, 테두리 외삽법, 테두리 색상)

# 침식 연산을 적용한 다음, 팽창 연산을 적용
# 침식 연산으로 인해 밝은 영역이 줄어들고 어두운 영역이 늘어
# opening = 줄어든 영역을 다시 복구하기 위해 팽창 연산을 적용하면 반대로 어두운 영역이 줄어들고 밝은 영역이 늘어
# opening = dilate(erode(src))
## 스펙클(speckle)이 사라지면서 발생한 객체의 크기 감소를 원래대로 복구 = 노이즈를 제거하는데 유용
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=5)

# 팽창 연산을 적용한 다음, 침식 연산을 적용
# 팽창 연산으로 인해 어두운 영역이 줄어들고 밝은 영역이 늘어
# closing = 늘어난 영역을 다시 복구하기 위해 침식 연산을 적용하면 밝은 영역이 줄어들고 어두운 영역이 늘어
# closing = erode(dilate(src))
## 객체 내부의 홀(holes)이 사라지면서 발생한 크기 증가를 원래대로 복구
## 객체 내의 작은 구멍이나 검은 점을 없애는데 도움
closing = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=5)

# 팽창 연산자와 침식 연산자의 조합
# gradient = dilate(erode(src)) - erode(dilate(src))
# 입력 이미지에 객체의 가장자리가 반환 = iterations= 낮을 수록 edge 반환
gradient = cv.morphologyEx(thresh, cv.MORPH_GRADIENT, kernel, iterations=1)

cv.imshow('image', img)
cv.imshow('thresh', thresh)
cv.imshow('opening', opening)
cv.imshow('closing', closing)
cv.imshow('gradient', gradient)
cv.waitKey()