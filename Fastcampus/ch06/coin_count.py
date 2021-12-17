import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt


# 입력 이미지 불러오기
src = cv2.imread('ch06\\images\\coins1.jpg')

if src is None:
    print('Image open failed!')
    sys.exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blr = cv2.GaussianBlur(gray, (0, 0), 1)

# 허프 변환 원 검출
circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50,
                            param1=150, param2=40, minRadius=20, maxRadius=80)


# 원 검출 결과 및 동전 금액 출력
sum_of_coins = 0
dst = src.copy()
if circles is not None:
    for i in range(circles.shape[1]):
        cx, cy, r = circles[0][i]
        cx = int(cx)
        cy = int(cy)
        r = int(r)
        cv2.circle(dst, (cx, cy), r, (0,0,255), 2, cv2.LINE_AA)

        # 동전 영역 부분 영상 추출
        # 사각형 모서리 좌표
        x1 = (cx - r) # 원 위
        y1 = (cy - r) # 원 왼쪽
        x2 = (cx + r) # 원 오른쪽
        y2 = (cy + r) # 원 아래

        # crop
        crop = dst[y1:y2, x1:x2, :]
        ch, cw = crop.shape[:2]
        crop_cp = crop.copy()

        # 동전 영역에 대한 ROI mask 영상 생성
        # == 동전의 histogram으로 진행할 것이기 때문에 동전이외의 색 삭제
        # np = 세로*가로, cv2 = 가로*세로
        mask = np.zeros((ch,cw), np.uint8)
        cv2.circle(mask, (cw//2, ch//2), r, 255, -1)
        mask_cp = mask.copy()

        '''
        *Histogram을 확인(mask 합성)*
        output = cv2.bitwise_and(crop_cp, crop_cp, mask=mask_cp)

        hsv_hist = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)
        h1, _, _ = cv2.split(hsv_hist)
        hist = cv2.calcHist([h1], [0], None, [181], [0, 181])
        # cv2.imshow('output', output)
        # plt.plot(hist)
        # plt.show()
        '''
        # 동전 영역 Hue 색 성분을 +40 시프트하고, Hue 평균을 계산
        # 10원의 경우 값이 앞쪽과 뒷부분(빨간색)이 포함되있기 때문에
        hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        hue_shift = (h + 40) % 180
        # cv2.mean = 채널이 1개인 배열부터 4개인 배열까지 입력받을 수 있다.
        # 요소가 4개인 스칼라 형태로 반환
        mean_of_hue = cv2.mean(hue_shift, mask)[0]
        # print(mean_of_hue)

        # Hue 평균이 90보다 작으면 10원, 90보다 크면 100원으로 간주
        won = 100
        if mean_of_hue < 90:
            won = 10

        sum_of_coins += won

        cv2.putText(crop, str(won), (20,50), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.75, (255,0,0), 2, cv2.LINE_AA)

cv2.putText(dst, str(sum_of_coins) + ' won', (40, 80),
            cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2, cv2.LINE_AA)

cv2.imshow('dst', dst)
cv2.waitKey()



