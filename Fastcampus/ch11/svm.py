import sys
import cv2
import numpy as np

digits = cv2.imread('ch11\\images\\digits.png', cv2.IMREAD_GRAYSCALE)

if digits is None:
    print('Image load failed')
    sys.exit()

# MouseCallback

oldx = oldy = -1

def onMouse(event, x, y, flags, _):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        pass

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (255,255,255), 30, cv2.LINE_AA)
            oldx, oldy = x, y
            cv2.imshow('img', img)

h, w = digits.shape # (1000, 2000)

# pixel 나누기
# 세로, 가로 20으로 나눔(20*20 영상을 만들기위함)
cells = [np.hsplit(row, w//20) for row in np.vsplit(digits, h//20)]
cells = np.array(cells) # (50, 100, 20, 20)
cells = cells.reshape(-1, 20,20) # shape=(5000, 20, 20)
print(cells[0].shape) # (20,20)

# HOG + SVM
# pdf 참조
hog = cv2.HOGDescriptor((20,20), (10,10), (5,5), (5,5), 9)
# print('Descriptor Size:', hog.getDescriptorSize()) # 324차원수
'''
영상 크기 20*20 = reshape 진행
block 10*10
cell 5*5
stride 5
bin 개수(gradient 방향 9개)
3*3*(4*9)= 324

4*9 = 한 block 당 9개의 방향값
3*3 = 5*5 block 이동 수(가로 * 세로)
'''

desc = []
for img in cells:
    # 20*20 하나의 숫자를 계산
    desc.append(hog.compute(img))

train_desc = np.array(desc) # (5000, 324)
train_desc = train_desc.squeeze().astype(np.float32) # 왜?
print(train_desc.shape)
# ==> shape = 1 제거
'''
>>> x = np.array([[[0], [1], [2]]])
[[[0]
  [1]
  [2]]]
>>> x.shape
(1, 3, 1)
>>> np.squeeze(x).shape, axis=1(default)
(3,) == [0 1 2]
>>> np.squeeze(x, axis=0).shape
(3, 1) == [[0]
           [1]
           [2]]
>>> np.squeeze(x, axis=2).shape
(1, 3) [[0 1 2]]
'''
# 0= 500장, 1=500장 ...
# np.repeat(a, repeats) = a는 복사할 값, repeats 몇번 반복할지(=배열복사)
train_labels = np.repeat(np.arange(10), len(train_desc)/10) # 5000(0, 1, ... 9)
print(train_desc.shape, train_labels.shape)

# SVM 학습
svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_RBF)
svm.setC(2.5)
svm.setGamma(0.50625)
svm.train(train_desc, cv2.ml.ROW_SAMPLE, train_labels)

# 모델 저장
svm.save('svmdigits.yml')
# 모델 불러오기
svm_load = cv2.ml.SVM_load('svmdigits.yml')

# svm.trainAuto(train_desc, cv2.ml.ROW_SAMPLE, svm_train_labels)
# print(f'svmC:{svm.getC}, svmGamma;{svm.getGamma}')
# SVM 자동 학습(k-폴드 교차 검증) 오래걸림
# svm.setC, svm.setGamma 지정해주는 것이 빠름
'''
cv.ml_SVM.trainAuto(samples, layout, responses, kFold=None, ...) -> retval

svm.trainAuto(trains, cv2.ml.ROW_SAMPLE, labels)
'''

# 사용자 입력 영상에 대해 예측(= setMouseCallback)
img = np.zeros((400,400), np.uint8)

cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse)

while True:
    key = cv2.waitKey()

    if key == ord('q'):
        break
    elif key == ord(' '):
        # test_image == 내가 입력한 이미지
        test_image = cv2.resize(img, (20,20), interpolation=cv2.INTER_AREA)
        test_desc = hog.compute(test_image).reshape(-1,1).T
        # (324, 1) --> (1, 324)

        _, res = svm_load.predict(test_desc) #= SVM Model load
        # _, res = svm.predict(test_desc)
        print(res) # 예측 결과 [[]]
        print(int(res))

        img.fill(0)
        cv2.imshow('img', img)

cv2.destroyAllWindows()
