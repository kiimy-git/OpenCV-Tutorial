import cv2
import sys
import matplotlib.pyplot as plt

# 녹색 배경 영상(여성만 추출)
cap1 = cv2.VideoCapture('ch03\\video\\woman.mp4')

# 예외처리
if not cap1.isOpened():
    print('video open failed')
    sys.exit()

# 비오는 배경 영상
cap2 = cv2.VideoCapture('ch03\\video\\raining.mp4')

# 두 영상 크기, FPS 같다고 가정
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

# 영상 크기 맞추기 위한 code
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

print('frame_cnt1:', frame_cnt1) # 409
print('frame_cnt2:', frame_cnt2) # 353
print(f'W X H: {w} * {h}') # 1280 * 720

fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

# 영상 저장
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, fps, (w,h))

# 합성 여부 flag
do_decomposit = False

while True: # mask를 가져올 영상 먼저
    ret1, frame1 = cap1.read() # woman

    if not ret1:
        break

    # do_composit flag가 True일 때에만 합성
    if do_decomposit:
        ret2, frame2 = cap2.read() # raining

        if not ret2:
            break
        '''
        webcam이나 다른 영상과 합칠 경우 size 맞춰주기
        frame2 = cv2.resize(frame2, (w,h))
        '''
        # HSV 색 공간에서 녹색 영역을 검출하여 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255))

        # frame2에서 frame1으로 복사를 하는데 mask의 흰 부분만 복사를 하겠다.
        cv2.copyTo(frame2, mask, frame1)

    # 영상저장
    out.write(frame1)

    # copy => frame1 
    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    if key == ord(' '):
        do_decomposit = ~do_decomposit
    elif key == ord('q'):
        break

cap1.release()
cap2.release()

