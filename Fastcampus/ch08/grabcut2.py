import sys
import numpy as np
import cv2


# 입력 영상 불러오기
src = cv2.imread('ch08\\images\\messi5.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

# 사각형 지정을 통한 초기 분할
mask = np.zeros(src.shape[:2], np.uint8) 

# 분할을 좀 더 좋아지는 방향으로 업데이트 할 때
bgdModel = np.zeros((1,65), np.float64) # 배경모델, 무조건(1,65)지정
fgdModel = np.zeros((1,65), np.float64) # 전경모델, 마찬가지

rc = cv2.selectROI(src)

cv2.grabCut(src, mask, rc, bgdModel, fgdModel, 1, mode= cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
dst = src * mask2[:,:, np.newaxis]

# 초기 분할 결과 출력
cv2.imshow('dst', dst)

# 마우스 이벤트
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: # foward 전경
        cv2.circle(dst, (x,y), 3, (255,0,0), -1)
        cv2.circle(mask, (x,y), 3, cv2.GC_FGD, -1)
        cv2.imshow('dst', dst)

    elif event == cv2.EVENT_RBUTTONDOWN: # background 배경
        cv2.circle(dst, (x,y), 3, (0,0,255), -1)
        cv2.circle(mask, (x,y), 3, cv2.GC_BGD, -1)
        cv2.imshow('dst', dst)

    elif event == cv2.EVENT_MOUSEMOVE:
        # .. | .. or로 하면 그림 계속 그려짐
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(dst, (x,y), 3, (255,0,0), -1)
            cv2.circle(mask, (x,y), 3, cv2.GC_FGD, -1)
            cv2.imshow('dst', dst)

        elif flags & cv2.EVENT_FLAG_RBUTTON:
            cv2.circle(dst, (x,y), 3, (0,0,255), -1)
            cv2.circle(mask, (x,y), 3, cv2.GC_BGD, -1)
            cv2.imshow('dst', dst)

# setMouse콜백           
cv2.setMouseCallback('dst', onMouse)

# 선택 부분 적용
while True:
    key = cv2.waitKey()
    if key == 13: # Enter
        # 사용자가 지정한 전경/배경 정보를 활용하여 영상 분할
        cv2.grabCut(src, mask, rc, bgdModel, fgdModel, 1, mode= cv2.GC_INIT_WITH_MASK)
        mask2 = np.where((mask==0) | (mask==2), 0, 1).astype('uint8')
        dst = src * mask2[:,:,np.newaxis]
        cv2.imshow('dst', dst)
    elif key == ord('q'):
        break