import sys
import numpy as np
import cv2

# Hough Transform
src = cv2.imread('ch06\\images\\building.jpg', cv2.IMREAD_GRAYSCALE)

# 노이즈 제거 후 진행하는 것이 더 선명한 line 검출
src = cv2.GaussianBlur(src, (0,0), 1)

if src is None:
    print('Image load failed!')
    sys.exit()

edges = cv2.Canny(src, 50, 150)
'''
파라미터 설정이 관건

cv2.HoughLinesP(image, rho, theta, threshold, lines, minLineLength, maxLineGap)
image = edge image
rho = 축적 배열에서 rho 값의 간격 -> 1pixel 간격
theta = 축적 배열에서 theta 값의 간격 -> 1 theta 간격
line= 선분의 시작과 끝 좌표(x1, y1, x2, y2) 정보를 담고 있는 numpy.ndarray.
      shape=(N, 1, 4). dtype=numpy.int32.
maxLineGap= 조명으로인해 edge가 끊어질 수 있음 해당 부분을 얼마정도의 값으로 이어줄거냐
==> 5로 설정한다면 5pixel이 떨어져 있어도 하나의 직선으로 만들어주겠다.
값이 작으면 확실한 선만 판단하게됨
'''
lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160,\
                        minLineLength=50, maxLineGap=10)    
# print(lines.shape) shape=(N, 1, 4)

dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for i in range(lines.shape[0]): # 직선의 개수
        # shape=(N, 1, 4)
        pt1 = (lines[i][0][0], lines[i][0][1]) # 시작점 좌표(x,y)
        pt2 = (lines[i][0][2], lines[i][0][3]) # 끝점 좌표(x,y)

        # dst에 line 표시
        cv2.line(dst, pt1, pt2, (0,0,255), 2, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('edges', edges)
cv2.imshow('dst', dst)
cv2.waitKey()