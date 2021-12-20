import math
import cv2

src = cv2.imread('ch07\\images\\polygon.bmp')

if src is None:
    print('Image load failed')
    
def setLabel(img, pts, label):
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x,y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (0,0,255), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))
    
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 도형색이 배경보다 높기 때문에 INV 진행
_, src_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for pts in contours:
    # 너무 면적이 작은값(noise)? 제거
    if cv2.contourArea(pts) < 1000:
        continue
    # print(pts) 각 좌표값

    # 근사화
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)

    # 각 모서리 개수
    vtc = len(approx)
    
    # 삼각형, 사각형
    if vtc == 3:
        setLabel(src, pts, 'TRI')
    elif vtc == 4:
        setLabel(src, pts, 'RECT')

    # 정해진 외곽선 길이에 대한 넓이 비율이 가장 큰 형태가 원
    else:
        length = cv2.arcLength(pts, True)
        area = cv2.contourArea(pts)
        ratio = 4. * math.pi * area / (length**2)

    # 1에 가까울수록 원으로 판단
        if ratio > 0.85:
            setLabel(src, pts, 'CIR')

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('src', src)
cv2.imshow('gray', gray)
cv2.imshow('src_bin', src_bin)
cv2.waitKey()

