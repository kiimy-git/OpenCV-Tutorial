import cv2 as cv
import numpy as np

# img 생성
img = np.full((400, 400, 3), 255, np.uint8)

# line
# cv2.line(img, pt1, pt2, color, thickness, lineType)
# pt1 = 시작점 좌표 (x, y)
# pt2 = 종료점 좌표 (x, y)
cv.line(img, (50, 50), (200, 50), (0, 0, 255), 5)

# rectangle ( x, y, w, h) = x, y 꼭지점으로부터 (x+w), (y+h)
cv.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
# (70, 220), ((x + w - 20), (y + h - 20))
cv.rectangle(img, (70, 220), (180, 280), (0, 255, 0), -1) # -1 = 채움

# circle (LINE_AA = 선을 부드럽게)
cv.circle(img, (300, 100), 30, (255, 255, 0), -1, cv.LINE_AA)
cv.circle(img, (300, 100), 60, (255, 0, 0), 1, cv.LINE_AA)

# polylines(pts = 연결할 꼭지점 좌표) / np.array() = 가로, 세로
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
# isClosed = 닫흰 도형 여부 / False 끝에 선이 이어지지 않음
# pts = [pts] 
cv.polylines(img, [pts], True, (255,0,0), 2)
cv.polylines(img, [pts], False, (255,0,0), 2)

# puttext( 가로, 세로 )
text = 'Draw' + cv.__version__
cv.putText(img, text, (50,350), cv.FONT_HERSHEY_SIMPLEX, 1, \
    (0,0,255),1, cv.LINE_AA)

cv.imshow('img', img)
cv.waitKey()
