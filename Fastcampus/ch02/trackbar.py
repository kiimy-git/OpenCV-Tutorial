import cv2 as cv
import numpy as np

# opencv에서 제공하는 (유일한?) 그래픽 사용자 인터페이스
# 트랙바 위치가 변경될 때마다 호출할 콜백 함수 이름
def onChange(pos): 
    #pos = 최대값 16
    value = pos * 16

    # pos * 16 / pos 값이 16일 때 256 값을 가지기 때문에
    # trackbar가 맨 끝에 왔을 때 검은 화면이 나옴 
    # so, 255보다 크면 255 값을 가지는 code 작성

    if value >= 255:
        value = 255

    '''
    if 조건문 안쓰고
    # 0보다 작은건 0, 255보다 큰건 255 설정 해줌
    value = np.clip(value, 0 ,255)
    '''
    
    img[:] = value
    cv.imshow('image', img)

img = np.zeros((480,640), np.uint8)
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.createTrackbar('level', 'image', 0, 16, onChange)
cv.imshow('image', img)
cv.waitKey()