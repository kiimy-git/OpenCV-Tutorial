import sys
import numpy as np
import cv2

# Dense = 특정 몇 개의 corner가 아니라 전체적으로 찾음

def draw_flow(img, flow, step=16):
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2, -1).astype(int)
    fx, fy = flow[y, x].T
    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.polylines(vis, lines, 0, (0, 255, 255), 2, lineType=cv2.LINE_AA)

    for (x1, y1), (_x2, _y2) in lines:
        cv2.circle(vis, (x1, y1), 1, (0, 128, 255), -1, lineType=cv2.LINE_AA)

    return vis

cap = cv2.VideoCapture("ch10\\videos\\vtest.avi")

if not cap.isOpened():
    print('Camera open failed!')
    sys.exit()

ret, frame1 = cap.read()

if not ret:
    print('frame read failed!')
    sys.exit()

gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

# np.zeros_like = 똑같은 크기와 타입이지만 0으로 초기화한 값
hsv = np.zeros_like(frame1)
# hsv에서 s에 해당하는건 255
hsv[..., 1] = 255

while True:
    ret, frame2 = cap.read()

    if not ret:
        print('frame read failed!')
        sys.exit()

    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(gray1, gray2, None, 0.5, 3, 13, 3, 5, 1.1, 0)
    '''
    # 파라미터 값을 잘 줘야함(사용하기가 어려움...)
    cv2.calcOpticalFlowFarneback(prev, next, flow, pyr_scale, levels, winsize,
                                iterations, poly_n, poly_sigma, flags) -> flow

    flow: 계산된 optical_flow, shape=(h, w, 2)
    '''
    # 모션벡터의 x 성분 = flow[..., 0] h, w, x
    # 모션벡터의 y 성분 = flow[..., 1] h, w, y
    # mag, ang 두 좌표 벡터의 크기와 각도(방향정보)
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])

    # hsv[..., 0] == h
    # hsv[..., 2] == v
    hsv[..., 0] = ang*180/np.pi/2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow('frame', frame2)
    cv2.imshow('flow', bgr)
    cv2.imshow('frame2', draw_flow(gray2, flow))
    if cv2.waitKey(20) == 27:
        break

    # 이렇게 안하면 특정 위치에서 값을 계속 가지고있는데..왜?
    gray1 = gray2 
