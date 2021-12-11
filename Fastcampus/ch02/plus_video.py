import sys
import numpy as np
import cv2 as cv

# 두 개 영상 변수 지정
cap1 = cv.VideoCapture('ch02\\video1.mp4')
cap2 = cv.VideoCapture('ch02\\video2.mp4')

# 예외처리
if not cap1.isOpened() or not cap2.isOpened():
    print('video load failed')
    sys.exit()

# 두 영상의 크기, FPS는 같다고 가정
# 다르면 사이즈 맞춰줘야함(How??)

# 영상의 총 프레임 수 get(cv.CAP_PROP_FRAME_COUNT) 
print(cap1.get(cv.CAP_PROP_FRAME_COUNT)) # 85.
print(cap2.get(cv.CAP_PROP_FRAME_COUNT)) # 121.

# get() = 실수형태로 가져오기 때문에 round or int 변경
frame_cnt1 = round(cap1.get(cv.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv.CAP_PROP_FPS) # 24.

# 앞 영상 끝부분 2초, 뒤 영상 앞부분 2초
effect_frames = int(fps * 2)

# 영상 재생 속도 설정(보통 30)
# 두 프레임 사이의 시간 간격
delay = 30 # int(1000/fps)

# 영상 사이즈
w = round(cap1.get(cv.CAP_PROP_FRAME_WIDTH)) # 1280
h = round(cap1.get(cv.CAP_PROP_FRAME_HEIGHT)) # 720
# 영상 저장 (Codec정보)
fourcc = cv.VideoWriter_fourcc(*'XVID')

out = cv.VideoWriter('output.avi', fourcc, fps, (w, h))


# 첫 번째 동영상
#마지막 프레임까지가 아니라 뒤에 48프레임정도 남겨줌
for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()

    if not ret1:
        print('frame read error')
        sys.exit()

    out.write(frame1)

    cv.imshow('output', frame1)
    cv.waitKey(delay)

# 1번 동영상 앞부분, 2번 동영상 뒷 부분 합성
# !!합성 하는 코드를 중간에 넣어야해!!
# ==> 두 번째 동영상 코드 뒤에 작성 하면 영상이 이어짐
for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print('frame read error')
        sys.exit()
    
    
    # w 앞 영상이 오른쪽에서 왼쪽으로 사리지고 다음 영상이 나옴
    # h 위에서 아래로 앞 영상이 사라지고 다음 영상이 나옴 
    dx = int(w / effect_frames) * i

    frame = np.zeros((h,w,3), dtype=np.uint8)
    # frame 위에서 아래로
    frame[0:dx, :] = frame2[0:dx, :]
    frame[dx:h, :] = frame1[dx:h, :]
    '''
    # frame 오른쪽에서 왼쪽으로
    frame[:, 0:dx] = frame2[:, 0:dx]
    frame[:, dx:w] = frame1[:, dx:w]
    '''

    
    # 앞 영상이 점점 흐려지면서 다음 영상 나옴
    # result = imgA * alpha + imgB * (1-alpha) + c
    # alpha = 1.0 - i / effect_frames
    # frame = cv.addWeighted(frame1, alpha, frame2, 1- alpha, 0)
    out.write(frame)

    cv.imshow('output', frame)
    cv.waitKey(delay)

# 두 번째 동영상(첫 번째영상에서 짤린 부분부터 끝까지)    
for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()

    if not ret2:
        print('frame read error')
        sys.exit()

    out.write(frame2)

    cv.imshow('output', frame2)
    # delay = 영상 속도
    cv.waitKey(delay)

print('\noutput.avi file is successfully generated!')

cap1.release()
cap2.release()
out.release()
