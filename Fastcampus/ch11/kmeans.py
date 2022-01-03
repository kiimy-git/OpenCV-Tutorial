import sys
import numpy as np
import cv2


# 입력 영상 불러오기
src = cv2.imread('ch11\\images\\flowers.jpg')

if src is None:
    print('Image load failed')
    sys.exit()

print(src.shape) # (640, 480, 3), dtype=uint8
# 차원 변환 & np.float32 변환
data = src.reshape((-1,3)).astype(np.float32)
print(data.shape) # (307200, 3)

# K-means 알고리즘

criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

for K in range(2,9):
    print('K:', K)

    ret, label, center = cv2.kmeans(data, K, None, criteria, 10, \
                                    flags=cv2.KMEANS_RANDOM_CENTERS)

    # 군집화 결과를 이용하여 출력 영상 생성
    center = np.uint8(center)

     # 각 픽셀을 K개 군집 중심 색상으로 치환
    dst = center[label.flatten()]
    dst = dst.reshape((src.shape))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
