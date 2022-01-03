import sys
import numpy as np
import cv2

# 가로 100, 세로 50 (5000개 숫자 데이터)
# 20 * 20 크기의 숫자 영상
digits = cv2.imread('ch11\\images\\digits.png', cv2.IMREAD_GRAYSCALE)

if digits is None:
    print('Image load failed!')
    sys.exit()

oldx, oldy = -1, -1
# setMouseCallback(= 그리기 함수)
def onMouse(event, x, y, flags, _):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        pass

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x,y), (255,255,255), cv2.LINE_AA)

            oldx, oldy = x, y
            cv2.imshow('img', img)

h, w = digits.shape[:2] # (1000, 2000)

# pixel 나누기
# 세로, 가로 20으로 나눔(20*20 영상을 만들기위함)
cells = [np.hsplit(row, w//20) for row in np.vsplit(digits, h//20)]
cells = np.array(cells) # (50, 100, 20, 20)

# knn 학습
train_images = cells.reshape(-1, 400).astype(np.float32) # (50 * 100, 400)
train_labels = np.repeat(np.arange(10), len(train_images)/10) # 5000(0, 1, ... 9)
knn = cv2.ml.KNearest_create()
knn.train(train_images, cv2.ml.ROW_SAMPLE, train_labels)

# 사용자 입력 영상에 대해 예측
img = np.zeros((400,400), np.uint8)
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse)

while True:
    key = cv2.waitKey()

    if key == ord('q'):
        break

    elif key == ord(' '):
        test_image = cv2.resize(img, (20,20), interpolation= cv2.INTER_AREA)
        test_image = test_image.reshape(-1, 400).astype(np.float32)

        ret, _, _, _ = knn.findNearest(test_image, 5)
        print(int(ret))

        img.fill(0) # 숫자를 그리고 spacebar 활성화 시 다시 그림 reset
        cv2.imshow('img', img)

cv2.destroyAllWindows()
