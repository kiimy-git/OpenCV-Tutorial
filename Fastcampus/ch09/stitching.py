import cv2
import numpy as np
import sys

images = ['img1.jpg', 'img2.jpg', 'img3.jpg']

imgs= []
for name in images:
    img = cv2.imread(f'ch09\\images\\{name}')

    if img is None:
        print('Images load failed')
        sys.exit()
    imgs.append(img)

# class 객체 불러오기
stitcher = cv2.Stitcher_create()
'''
cv2.Stitcher_create(, mode=None) -> retval

mode: 스티칭 모드. cv2.PANORAMA 또는 cv2.SCANS 중 하나 선택
# mode = cv2.SCANS(영상의 밝기가 균일할때, Affine의 형태만 가능)
'''

ret, dst = stitcher.stitch(imgs)
'''
cv2.Stitcher.stitch(images, pano=None) -> retval, pano

retval: 성공하면 cv2.Stitcher_OK. 
pano: 파노라마 영상
'''
if ret != cv2.Stitcher_OK:
    print('Stitch failed')
    sys.exit()

# 스트칭 파일 저장
# cv2.imwrite('PANO', dst) == 확장자 설정해줘야해(.jpg)
cv2.imwrite('ch09\\images\\PANO.jpg', dst)

cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
cv2.imshow('dst', dst)
cv2.waitKey()