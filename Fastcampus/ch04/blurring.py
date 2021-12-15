import cv2
import sys
import numpy as np

src = cv2.imread('ch04\\images\\rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


'''
kernel = np.array([[1/9,1/9,1/9],
                   [1/9,1/9,1/9],
                   [1/9,1/9,1/9]], dtype=np.float32) # 기본적으로 float64로 만들어짐

kernel = np.ones((3, 3), dtype=np.float64) / 9.
'''
# dst = cv2.filter2D(src, -1, kernel, borderType) 
# ddepth = -1: 입력영상과 동일한 datatype로 생성(grayscale)
# borderType = BORDER_REFLECT_101 or BORDER_DEFAULT


# cv2.blur()
dst = cv2.blur(src, (3,3))

for ksize in (3, 5, 7):
    dst_ksize = cv2.blur(src, (ksize,  ksize))

    text = f'Mean:{ksize}x{ksize}'
    cv2.putText(dst_ksize, text, (10,30), cv2.FONT_HERSHEY_SIMPLEX,\
                fontScale= 1.0, color= 255, thickness= 1, lineType=cv2.LINE_AA)

    cv2.imshow('dst_ksize', dst_ksize)
    cv2.waitKey()

# cv2.imshow('image', src)
# cv2.imshow('dst', dst)
cv2.waitKey()
