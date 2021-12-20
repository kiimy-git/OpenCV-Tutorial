import sys
import numpy as np
import cv2


src = cv2.imread('ch07\\images\\keyboard.bmp', cv2.IMREAD_GRAYSCALE)
print(src.shape)
if src is None:
    print('Image load failed!')
    sys.exit()

_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)

# 레이블링된 객체의 크기와 어디에 있는지 정보가 필요할때 유용하게 쓰임
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

# bbox를 color로 보여주기위함
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for i in range(1, cnt):
    (x,y,w,h,area) = stats[i]
    print(stats[i])
    # 작은 noise가 검출되니 a 값이 작은 것들은 빼주겠다.
    # threshold를 open함수를 통해서 침식 팽창을 해도됨
    if area < 20:
        continue
    
    cv2.rectangle(dst, (x,y,w,h), (0,0,255))

cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)
cv2.waitKey()