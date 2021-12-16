import sys
import numpy as np
import cv2

'''
굴곡진 이미지 형성
* 어파인, 투시 변환: 변환 행렬 연산을 적용
* remap: 비선형 변환을 적용
즉, 픽셀들의 좌표를 임의의 특정 좌표로 옮겨 이미지를 변경하는 작업을 의미
'''

src = cv2.imread('ch05\\images\\tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

h, w = src.shape[:2]

# 이미지에 적용할 mapping 설정
# y좌표 index, x좌표 index = np.indices()
# 어떤 행렬의 index값( 행렬의 x좌표값, y좌표값 반환)
map2, map1 = np.indices((h,w), np.float32)
map2 = map2 + (10 * np.sin(map1 / 32))

# cv2.remap(src, map1, map2, interpolation, borderMode, borderValue)
# map1 = 결과 영상의 (x, y) 좌표가 참조할 입력 영상의 x좌표
# map2 = 결과 영상의 (x, y) 좌표가 참조할 입력 영상의 y좌표
'''
*borderMode*
cv2.BORDER_DEFAULT: 영상 바깥쪽에 가상의 픽셀이 있기 때문에 자연스러움
                    ==> 금방의 색으로 대체됨(대칭)
cv2.BORDER_CONSTANT(default): borderValue가 0(default) 영상 바깥쪽 검은색
'''
dst = cv2.remap(src, map1, map2, interpolation=cv2.INTER_CUBIC,\
                borderMode= cv2.BORDER_DEFAULT)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()