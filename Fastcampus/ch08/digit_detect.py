import sys
import numpy as np
import cv2

src = cv2.imread('ch08\\images\\digits_print.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# load_images 폴더 이미지 불러오기
def load_digits():
    img_digits = []
    for i in range(10):
        filename = f'ch08\\digits\\digit{i}.bmp'
        img_digits.append(cv2.imread(filename, cv2.IMREAD_GRAYSCALE))

        if img_digits[i] is None:
            print(('Image load failed'))
            return None
    
    return img_digits

def find_digit(img, img_digits):
    max_idx = -1
    max_ccoeff = -1
    for i in range(10):
        # img_digits.shape (150, 100)
        img = cv2.resize(img, (100, 150))
        res = cv2.matchTemplate(img, img_digits[i], cv2.TM_CCOEFF_NORMED)

        # res = img 영상과, img_digits 영상의 크기가 같으면 (1*1)행렬로 나옴
        # -1 ~ 1 의 값이 나옴
        if res[0,0] > max_ccoeff:
            max_idx = i
            max_ccoeff = res[0,0]

    return max_idx

# load_digits 함수, 폴더에 있는 이미지 다 불러오기
img_digits = load_digits() # list
print(img_digits[0].shape)

# 입력 영상 이진화 & 레이블링
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cnt, _, stats, _ = cv2.connectedComponentsWithStats(src_bin)

# 숫자 인식 결과 영상 생성
dst = src.copy()
for i in range(1, cnt):
    (x, y, w, h, area) = stats[i]

    if area < 1000:
        continue

    # 가장 유사한 숫자 이미지를 선택
    # find_digit
    digit = find_digit(src_gray[y:y+h, x:x+w], img_digits)
    cv2.rectangle(dst, (x,y,w,h), (0,255,255))
    cv2.putText(dst, str(digit), (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX,\
                0.7, (0,0,255), 1, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('dst', dst) # 비스듬하거나 
cv2.waitKey()

