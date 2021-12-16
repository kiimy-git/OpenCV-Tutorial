import sys
import cv2
import numpy as np

src = cv2.imread('ch05\\images\\scanned.jpg')

if src is None:
    print('Image load failed')
    sys.exit()

# 입력 영상 크기 및 출력 영상 크기(용지 비율 구하기)
h, w = src.shape[:2]

# A4 용지 크기 : 210x297cm
# 투시변환한 최종 이미지 사이즈 설정
dw = 500
dh = round(dw * (297 / 210))

# 모서리 점들의 좌표(드래그할 bbox 초기 상태)
# 좌측상단, 좌측하단, 우측하단, 우측상단
srcQuad = np.float32([[30, 30], [30, h-30], [w-30, h-30], [w-30, 30]])

# 드래그해서 업데이트 된 좌표 투시변환으로 mapping할 사이즈(최종출력물)
dstQuad = np.float32([[0,0], [0, dh], [dw,dh], [dw, 0]])

# 드래그 여부
dragSrc = [False, False, False, False]

# 모서리점, 사각형(bbox) 그리기
def drawROI(img, corners):
    cpy = img.copy()

    # 사각형 color, 모서리 color
    c1 = (192, 192, 255)
    c2 = (128, 128, 255)

    # 모서리 circle 형성
    # corners = 튜플로 변환해서 진행해야함(srcQaud = ndarray로 되있기 때문에)
    # and int로
    corners = tuple(corners.astype(int))
    for pt in corners:
        print(pt)
        cv2.circle(cpy, pt, 25, c1, -1, cv2.LINE_AA)

    # bbox
    cv2.line(cpy, (corners[0]), (corners[1]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, (corners[1]), (corners[2]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, (corners[2]), (corners[3]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, (corners[3]), (corners[0]), c2, 2, cv2.LINE_AA)

    # addweight로 원래이미지가 잘보이게 bbox 흐리게 형성
    roi = cv2.addWeighted(img, 0.5, cpy, 0.5, 0)

    return roi

# mouse event
def onMouse(event, x, y, flags, param):
    global srcQuad, dragSrc, src, ptOld

    # mouse button
    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            # 25= 반지름, 분홍색 원안에 들어가면 
            # drag 활성화
            if cv2.norm(srcQuad[i] - (x, y)) < 25:
                dragSrc[i] = True

        # 마우스를 움직일때마다 같이 원이 이동해줘야하는데 이동변이를 알기위해
                ptOld = (x, y)
                break
    
    # Mouse move
    if event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]: # dragSrc가 True일 때
                # x, y가 처음 마우스 위치에서 얼만큼 이동했다
                dx = x - ptOld[0]
                dy = y - ptOld[1]

                # 이동한 만큼 bbox 좌표 업데이트
                srcQuad[i] += (dx, dy)

                # 해당 bbox 출력
                roi = drawROI(src, srcQuad)
                cv2.imshow('img', roi)

                # ptOld = 현재점으로 셋팅
                ptOld = (x, y)
                break
    
    # mouse up
    if event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i] = False # drag 종료


roi = drawROI(src, srcQuad)
cv2.imshow('img', roi) # 출력할 img 이름과 mouseevent할 img이름 동일해야해
cv2.setMouseCallback('img', onMouse)

# event 종료 방법 설정
while True:
    key = cv2.waitKey()
    if key == 13: # enter
        break
    elif key == 27:
        cv2.destroyWindow('img')
        sys.exit()

# event 종료 후 업데이트 된 좌표 값으로 투시변환 적용
rot = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, rot, (dw,dh), flags=cv2.INTER_CUBIC)
cv2.imshow('dst', dst)
cv2.waitKey()