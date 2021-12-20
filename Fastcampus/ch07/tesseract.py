'''
https://github.com/UB-Mannheim/tesseract/wiki
'''
import sys
import random
import numpy as np
import cv2
import pytesseract

src = cv2.imread('ch07\\images\\namecard1.jpg')

if src is None:
    print('Image load falied')
    sys.exit()

# 출력 영상 설정
dw, dh = 720, 400
srcQuad =  np.array([[0,0], [0,0], [0,0], [0,0]], np.float32)
dstQuad =  np.array([[0,0], [0,dh], [dw,dh], [dw,0]], np.float32)
dst = np.zeros((dw,dh), np.uint8)

# print(src.shape) # (810, 1080, 3)

# 입력 영상 전처리
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_OTSU)

# 외곽선 검출 및 명함 검출
contours, hier = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 근사화
cpy = src.copy()
for pts in contours:
    if cv2.contourArea(pts) < 1000:
        continue

    # 근사화(더글라스 포이커) 각각의 좌표 (4, 1, 2)
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)
    srcQuad = approx.reshape(4,2).astype(np.float32)
    '''
    # 인덱스를 명확히 설정(def reorderPts)
    srcQuad = reorderPts(approx.reshape(4, 2).astype(np.float32))
    '''

def reorderPts(pts):
    # 칼럼0 -> 칼럼1 순으로 정렬한 인덱스를 반환
    idx = np.lexsort((pts[:, 1], pts[:, 0]))  
    pts = pts[idx]  # x좌표로 정렬

    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]] # 스와핑

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    return pts

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (dw,dh))

#설치 경로 지정 후 실행
pytesseract.pytesseract.tesseract_cmd = R'C:\\Program Files\\Tesseract-OCR\\tesseract'

dst_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
print(pytesseract.image_to_string(dst_gray, lang='eng'))

cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)
cv2.waitKey()