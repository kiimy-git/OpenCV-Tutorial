import sys
import numpy as np
import cv2

src = cv2.imread('ch11\\images\\handwritten1.png')

if src is None:
    print('Image load failed!')
    sys.exit()

print(src.shape) # (480,640,3)


# 숫자 영상을 20x20 크기 안에 적당히 들어가도록 리사이즈
# 숫자의 바운딩 박스 부분 영상의 가로/세로 비율을 유지할 것
def norm_img(img):
    h, w = img.shape[:2]
    
    # img = src_gray(흰색 배경에 검은색글씨)
    # 반전을 시켜줘여함(검은색 배경에 흰색 글씨)
    img = ~img

    # 노이즈 제거
    blr = cv2.GaussianBlur(img, (0,0), 2)

    sf = 14. / h # scale factor. 위/아래 3픽셀씩 여백 고려.
    if w > h:
        sf = 14. / w

    img2 = cv2.resize(img, (0,0), fx=sf, fy=sf, interpolation= cv2.INTER_AREA)
    
    h2, w2 = img2.shape[:2]
    a= (20 - w2) // 2
    b= (20 - h2) // 2

    dst = np.zeros((20,20), dtype=np.uint8)
    dst[b:b+h2, a:a+w2] = img2[:, :]

    return dst


# HOG 객체 생성(img resize 함수 설정= norm_img)
hog = cv2.HOGDescriptor((20, 20), (10, 10), (5, 5), (5, 5), 9)

# 미리 학습된 SVM 데이터 불러오기
svm_load = cv2.ml.SVM_load('svmdigits.yml')

# 이진화 & 레이블링
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

cnts, _, stats, _ =cv2.connectedComponentsWithStats(thresh)

# 원래 그림에서 확인하기 위함
dst = src.copy()

# 배경은 제외
for i in range(1, cnts):
    x, y, w, h, area = stats[i]

    if area < 100:
        continue

    # 각각의 숫자 부분 영상을 정규화한 후 HOG & SVM 숫자 인식
    digits = norm_img(src_gray[y:y+h, x:x+w])
    test_desc = hog.compute(digits).reshape(-1,1)
    '''
    # 계산을 위한 축 추가해야되(np.newaxis) or .reshape(-1,1)
    test_desc = test_desc[:, np.newaxis]
    # print(test_desc.shape) # (324, 1)
    '''
    _, res = svm_load.predict(test_desc.T)

    # HOG & SVM 숫자 인식 결과 출력
    cv2.rectangle(dst, (x,y,w,h), (0,0,255))
    cv2.putText(dst, str(int(res)), (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, \
                2, (0,0,255), 2, cv2.LINE_AA)

cv2.imshow('dst', dst)
cv2.waitKey()

# cv2.imshow('src', src)
# cv2.waitKey()
