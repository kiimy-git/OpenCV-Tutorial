import sys
import numpy as np
import cv2


src = cv2.imread('ch07\\images\\rice.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst1 = np.zeros(src.shape, np.uint8)

bw = src.shape[1] // 4
bh = src.shape[0] // 4

# adaptiveThreshold 사용해도 되는데 느림
for y in range(4):
    for x in range(4):
        src_ = src[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        dst_ = dst1[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        cv2.threshold(src_, 0, 255, cv2.THRESH_OTSU, dst_)

'''
cv2.connectedComponents(image, labels=None, connectivity=None, 
                        ltype=None) -> retval, labels

흰색 덩어리의 개수를 정수 형태로 return( retval, labels)
retval 덩어리 개수 + 1 의 형태로 나옴
labels = np.ndarray 나오고 각 덩어리에 label 값부여됨

connectedComponentsWithStats 이게 더 많이 쓰임
== 레이블링된 객체의 크기와 어디에 있는지 정보가 필요할 때
'''
cnt1, _ = cv2.connectedComponents(dst1)
print('cnt1:', cnt1)

dst2 = cv2.morphologyEx(dst1, cv2.MORPH_OPEN, None)
# open = 보통 noise를 제거할 때 사용
#dst2 = cv2.erode(dst1, None)
#dst2 = cv2.dilate(dst2, None)

cnt2, _ = cv2.connectedComponents(dst2)
print('cnt2:', cnt2)

###############################################################
# cv2.connectedComponents(image) -> retval(cnt), labels
# labeling 방법 
mat = np.array([
    [0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]], np.uint8)

cnt, labels = cv2.connectedComponents(mat)

print('sep:', mat, sep='\n')
print('cnt:', cnt)
print('labels:', labels, sep='\n')

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()