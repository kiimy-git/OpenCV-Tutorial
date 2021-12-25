import sys
import numpy as np
import cv2

src = cv2.imread('ch07\\images\\rice.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# cv2.THRESH_BINARY는 생략가능 (default)
th, dst1 = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print("otsu's threshold:", th)  # 131(실수형태로 나옴)

# Local 이진화
dst2 = np.zeros(src.shape, np.uint8)

# block 설정(128, 128)
bw = src.shape[1] // 4
bh = src.shape[0] // 4
print(bw, bh)

# Local 이진화 직접구현
for y in range(4):
    for x in range(4):
        # crop
        src_ = src[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        dst_ = dst2[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        '''
        입력영상을 출력영상으로 받는다.
        why?  _, dst_ = cv2.threshold 로 진행하면 이전 dst_의 정보를 잃어버려
        dst: 출력 영상. src와 동일 크기, 동일 타입, 같은 채널 수
        dst_ = src_의 크기가 같아야함
        '''
        cv2.threshold(src_, 0,255,cv2.THRESH_OTSU, dst_)

# 결과 출력
cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()