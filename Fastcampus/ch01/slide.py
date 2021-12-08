import cv2 as cv
import sys
import os
import glob


img_files = glob.glob('.\\images\\*.jpg')

for i in img_files:
    print(i)

if not img_files:
    print("There are no jpg files in 'images' folder")
    sys.exit()

# 전체화면으로 창 생성
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.setWindowProperty('image', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

# 무한 루프를 돌아야하기 때문에(다시 첫번째로 돌아가는)
img_count = len(img_files)
idx = 0

while True:
    img = cv.imread(img_files[idx])

    cv.imshow('image', img)

    if cv.waitKey(1000) == ord('q'):
        break
    
    # 처음 idx = 0 번째 이미지를 보니까 추가
    idx +=1
    if idx >= img_count:
        # 다시 0번째로
        idx = 0
