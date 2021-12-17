import sys
import numpy as np
import cv2

'''
method = cv2.HOUGH_GRADIENT_ALT 사용하면
더 좋은 원을 검출 
'''

# 입력 이미지 불러오기
src = cv2.imread('ch06\\images\\dial.jpg')

if src is None:
    print('Image open failed!')
    sys.exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blr = cv2.GaussianBlur(gray, (0, 0), 2.0)

def onChange(pos):
    minr = cv2.getTrackbarPos('minRadius', 'img')
    maxr = cv2.getTrackbarPos('maxRadius', 'img')
    thresh = cv2.getTrackbarPos('threshold', 'img')
    '''
    cv2.HoughCircles(image, method, dp, minDist, circles, param1, param2)
    *image = edge영상이 아닌 일반 입력영상이 들어가야함
    *dp = 입력영상과 축적배열의 크기 비율
    *minDist = 검출된 원 중심점들의 최소 거리
    *circles =(cx, cy, r) 정보를 담은 numpy.ndarray. shape=(1, N, 3), dtype=np.float32
             ==> 중심점 좌표 두개와 반지름 np.float32
    *param1 = canny edge 검출기의 높은 임계값
    *param2 = 축적배열에서 원 검출을 위한 임계값== 높게 주냐 안주냐에 따라 원을 검출
    '''
    circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50,
                               param1=120, param2=thresh, minRadius=minr, maxRadius=maxr)
    
    # print(circles) (cx, cy, r) shape=(1, N, 3)
    dst = src.copy()
    if circles is not None:
        for i in range(circles.shape[1]):
            # numpy.float32
            cx, cy, radius = circles[0][i] # [0]: [[[]]] => [[]]각 circle 접근
            # circle ==> int(center, radius)
            cv2.circle(dst, (int(cx), int(cy)), int(radius), (0,0,255), 2, cv2.LINE_AA)

    cv2.imshow('img', dst)

# trackbar(사용할 함수 파라미터 지정)
cv2.namedWindow('img')
cv2.createTrackbar('minRadius', 'img', 0, 100, onChange)
cv2.createTrackbar('maxRadius', 'img', 0, 150, onChange)
cv2.createTrackbar('threshold', 'img', 0, 100, onChange)
cv2.setTrackbarPos('minRadius', 'img', 10)
cv2.setTrackbarPos('maxRadius', 'img', 80)
cv2.setTrackbarPos('threshold', 'img', 40)
cv2.waitKey()