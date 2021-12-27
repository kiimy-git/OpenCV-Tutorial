import sys
import numpy as np
import cv2

digits = cv2.imread('ch11\\images\\digits.png', cv2.IMREAD_GRAYSCALE)

oldx = oldy = -1

def onMouse(event, x, y, flags, _):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        pass

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x,y), (255,255,255), 30, cv2.LINE_AA)

            oldx, oldy = x, y
            cv2.imshow('img', img)

# 숫자 영상의 사이즈 설정
h, w = digits.shape

# hog 객체 생성
hog = cv2.HOGDescriptor((20, 20), (10, 10), (5, 5), (5, 5), 9)
print(hog.getDescriptorSize())

cells = [np.hsplit(row, w//20) for row in np.vsplit(digits, h//20)]
cells = np.array(cells)
cells = cells.reshape(-1, 20, 20) # hog 사이즈와 맞춰야함
print(cells.shape)


# normalize
def norm_digit(img):
    m = cv2.moments(img)
    cx = m['m10'] / m['m00'] # cx, cy = img의 무게중심
    cy = m['m01'] / m['m00']
    h, w = img.shape[:2]
    aff = np.array([[1, 0, w/2 - cx], [0, 1, h/2 - cy]], dtype=np.float32)
    dst = cv2.warpAffine(img, aff, (0, 0))
    return dst

# hog 계산 * norm
desc = []
for img in cells:
    img = norm_digit(img)
    desc.append(hog.compute(img))

train_desc = np.array(desc)
# 0이 500개, 1이 500개 .....
# np.repeat 배열 반복
train_labels = np.repeat(np.arange(10), len(train_desc)/10)

# SVM 학습
# svm = cv2.ml.SVM_create()
# svm.setType(cv2.ml.SVM_C_SVC)
# svm.setKernel(cv2.ml.SVM_RBF)
# svm.setC(2.5)
# svm.setGamma(0.50625)
# svm.train(train_desc, cv2.ml.ROW_SAMPLE, train_labels)

# svm load
svm = cv2.ml.SVM_load('svmdigits.yml')

img = np.zeros((400,400), np.uint8)

cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse)

while True:
    key = cv2.waitKey()

    if key == ord('q'):
        break

    elif key == ord(' '):
        test_image = cv2.resize(img, (20,20), interpolation=cv2.INTER_AREA)
        # normalize
        test_image = norm_digit(test_image)
        test_desc = hog.compute(test_image).reshape(-1,1).T

        _, res = svm.predict(test_desc)
        print(int(res))

        img.fill(0)
        cv2.imshow('img', img)
