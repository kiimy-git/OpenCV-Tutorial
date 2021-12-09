import sys
import time
import numpy as np
import cv2 as cv


img = cv.imread('ch02\\hongkong.jpg')

if img is None:
    print('Image load failed')
    sys.exit()

# 시간 객체화
tm = cv.TickMeter()

# 시작
tm.start()
endtime = time.time()

# edge 검출 ( 시작과 종료 중간에 함수 정의 )
edge = cv.Canny(img, 50, 150)

# 종료
tm.stop()

# time.time() / 현재 시각 - 시작한 시각(end)
# cv.TickMeter()
print('time', (time.time() - endtime) * 1000) # time 120.75662612
print(f'Elapsed(경과) time : {tm.getTimeSec()}ms') # Elapsed(경과) time : 0.1207774ms
print(f'Elapsed(경과) time : {tm.getTimeMilli()}ms') # Elapsed(경과) time : 120.7774ms
print(f'Elapsed(경과) time : {tm.getTimeMicro()}ms') # Elapsed(경과) time : 120777.4ms

'''
tm.getTimeSec() 초단위
tm.getTimeMilli() 밀리 초단위
tm.getTimeMicro() 마이크로 초단위
'''

