import sys
import cv2 as cv
'''
프레임은 비디오나 영화, TV등이 영상 매체를 전달할 때 화면에 뿌려주는 한장 한장의 그림을 말합니다. 
이러한 한장 한장의 그림들이 초당 얼마간의 속도로 빠르게 바뀌면서 움직이는 하나의 동영상을 만들어 내게 됩니다. 
영화에서 쓰이는 필름을 떠 올려보십시요. 그 필름에서 보이는 하나 하나의 그림이 바로 프레임을 뜻합니다. 
이것은 인간의 시각이 한 장의 그림을 본 후 뇌에 전달하기 까지의 과정에서 또 다른 한 장의 그림을 보여줌으로써 실제로는 한 장, 
한 장 의 그림을 본 것임에도 움직인다고 느끼게 만드는 일종의 눈 속임이라고 볼 수 있습니다.
'''

# camera
cap = cv.VideoCapture(0)

# in 예외처리
if not cap.isOpened():
    print('Camera open failed')
    sys.exit()

# camera frame size = 640, 480 
# 비디오 프레임 크기, 전체 프레임수, FPS 등 출력(get() = float / (int, round) 변환)
print('Frame width', int(cap.get(cv.CAP_PROP_FRAME_WIDTH))) 
print('Frame height', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))) 
print('Frame count:', int(cap.get(cv.CAP_PROP_FRAME_COUNT)))

'''
# 비디오 프레임 크기 수정
cap.set(cv.CAP_PROP_FRAME_WIDTH, 320) # 보통 width 320
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240) # 보통 height 240
'''
w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# 보통 30 (카메라마다 다름)
fps = cap.get(cv.CAP_PROP_FPS)
print('FPS:', fps)

# 비디오 영상 저장
# Windows는 DIVX
fourcc = cv.VideoWriter_fourcc(*'DIVX') # == 'D', 'I', 'V', 'X'
delay = round(1000 / fps) # 한 프레임과 그 다음 프레임 간격

out = cv.VideoWriter('output.avi', fourcc, fps, (w,h))

# out 예외처리
if not out.isOpened():
    print('file open failed')
    cap.release()
    # 필요한 상황에 데이터를 요청하고 다른 곳에서 이 카메라 디바이스에 정보를 요청할 수도 있으니
    # 이제부터 우리가 선언한 변수에게 데이터를 그만 요청하라는 뜻
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break
    '''
    flipCode < 0은 XY 축 대칭(상하좌우 대칭)을 적용
    flipCode = 0은 X 축 대칭(상하 대칭)을 적용
    flipCode > 0은 Y 축 대칭(좌우 대칭)을 적용
    '''
    frame = cv.flip(frame, 1) # 반전
    inversed = ~frame # 색 반전
    # canny의 경우는 grayscale이라 저장이 안됨
    # ==> edge_color = cv.cvtColor(edge, cv.COLOR_GRAY2BGR)
    # ==> out.write(edge_color)
    edge = cv.Canny(frame, 50, 150) # 윤곽선

    cv.imshow('frame', frame)
    cv.imshow('inversed', inversed)
    cv.imshow('canny', edge)

    # key = cv.waitKey() 변수로 지정하는 것이 용이
    if cv.waitKey(delay) == ord('q'):
        break

cap.release()
out.release()