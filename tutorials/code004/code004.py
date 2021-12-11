import cv2 as cv

img = cv.imread('.\\tetris_blocks.png')
img = cv.resize(img, (500,500))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Edge Dectection(가장자리 검출)
'''
가장자리는 픽셀의 밝기가 급격하게 변하는 부분으로 간주할 수 있다.
가장자리를 찾기 위해 미분(Derivative)과 기울기(Gradient) 연산을 수행하며, 이미지 상에서 픽셀의 밝기 변화율이 높은 경계선 찾는다.
'''
# cv.Canny 가장 흔히 사용됨
canny = cv.Canny(gray, 80, 100)

# cv.Sobel(src, '출력 이미지 정밀도(ddepth)', dx, dy, 커널 크기(ksize))
# X 방향 미분 차수와 Y 방향 미분 차수는 합이 1 이상이여야 하며, 0의 값은 해당 방향으로 미분하지 않음을 의미
sobel = cv.Sobel(gray, cv.CV_8U, 0, 1, 3)

# Thresholding(이진화) 
# 설정 임곗값(retval)과 결과 이미지(dst)를 반환
# 도형 검출 시 object가 흰색성질을 띄도록 변환(INV)
res, dst = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)


# Counting Objects(contours 윤곽선, hierarchy 계층구조)
# cv2.findContours(이진화 이미지, 검색 방법, 근사화 방법)
contours, hierarchy = cv.findContours(dst.copy(), cv.RETR_EXTERNAL, \
    cv.CHAIN_APPROX_SIMPLE)

# [contours[i]] = 윤곽선 표시
# cv.CHAIN_APPROX_SIMPLE 윤곽점들 단순화 수평, 수직 및 대각선 요소를 압축하고 끝점만 남김
print(contours) # 각 점으로 표시됨
print(hierarchy[0][1])
'''
# 계층 구조는 윤곽선을 포함 관계의 여부를 나타낸다
외곽 윤곽선, 내곽 윤곽선, 같은 계층 구조를 구별할 수 있다.
* hierarchy.shape = (1, 6, 4)

[[[ 1 -1 -1 -1]
  [ 2  0 -1 -1] => hierarchy[0][1]
  [ 3  1 -1 -1]
  [ 4  2 -1 -1]
  [ 5  3 -1 -1]
  [-1  4 -1 -1]]]
  
[다음 윤곽선, 이전 윤곽선, 내곽 윤곽선, 외곽 윤곽선]
* 다음 윤곽, 이전 윤곽 = -1이 아니면 동등한 계층에 있다 <=> -1이면 동등한 계층 없다
* 내곽 윤곽 = 1은 도형 내부에 윤곽선이 있다(내부 도형이 있음)
* 외곽 윤곽 = 0은 내부 도형에서 외곽 윤곽이 있을 때
'''

# cv2.drawContours(이미지, [윤곽선], 윤곽선 인덱스, (B, G, R), 두께, 선형 타입)
# 윤곽선 인덱스 -1 = 윤곽선 배열 모두를 의미
for i in range(len(contours)):
    cv.drawContours(img, [contours[i]], -1, (0,0,255), 3)
    # cv.imshow('img', img)
    # cv.waitKey() == ord('q')

text = f'i found {len(contours)}' 
# cv.putText(img, text, '좌측 상단 모서리(org)', fontFace, fontScale, color, 굵기)
cv.putText(img, text, (20,25), cv.FONT_HERSHEY_SIMPLEX, 0.7,(240, 0, 159), 2)
cv.imshow('contours', img)
cv.waitKey()
'''
# 검색 방법Permalink
cv2.RETR_EXTERNAL : 외곽 윤곽선만 검출하며, 계층 구조를 구성하지 않습니다.
cv2.RETR_LIST : 모든 윤곽선을 검출하며, 계층 구조를 구성하지 않습니다.
cv2.RETR_CCOMP : 모든 윤곽선을 검출하며, 계층 구조는 2단계로 구성합니다.
cv2.RETR_TREE : 모든 윤곽선을 검출하며, 계층 구조를 모두 형성합니다. (Tree 구조)

# 근사화 방법Permalink
cv2.CHAIN_APPROX_NONE : 윤곽점들의 모든 점을 반환합니다.
cv2.CHAIN_APPROX_SIMPLE : 윤곽점들 단순화 수평, 수직 및 대각선 요소를 압축하고 끝점만 남겨 둡니다.
cv2.CHAIN_APPROX_TC89_L1 : 프리먼 체인 코드에서의 윤곽선으로 적용합니다.
cv2.CHAIN_APPROX_TC89_KCOS : 프리먼 체인 코드에서의 윤곽선으로 적용합니다.
'''

# cv.imshow('image', img)
# cv.imshow('gray', gray)
cv.imshow('canny', canny)
cv.imshow('sobel', sobel)
cv.imshow('thres', dst)
cv.waitKey()
