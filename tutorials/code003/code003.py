import cv2 as cv

# 이미지 확대( image pyramid )
img = cv.imread('.\\ch01\\cat.bmp')

'''
만약 알고리즘에서 요구하는 해상도가 있다면 입력 이미지의 크기를 변경해 영상 처리를 진행
또한, 검출하려는 객체가 너무 작거나 입력 이미지가 너무 큰 경우 입력 이미지 자체를 변환해서 영상 처리를 진행할 수도 있다.

* 원본 이미지에서 크기를 확대하는 것을 업 샘플링이라 하며 하위 단계의 이미지를 생성

* 원본 이미지에서 크기를 축소하는 것을 다운 샘플링이라 하며, 상위 단계의 이미지를 생성
'''

# 가우시안 피라미드(Gaussian Pyramid), 라플라시안 피라미드(Laplacian pyramid)
(h, w, d) = img.shape

# cv.pyrUp('이미지', '출력크기', '테두리 외삽법')
# 테두리 외삽법(borderType)은 이미지를 확대하거나 축소할 경우, 이미지 영역 밖의 픽셀은 추정해 값을 할당
dst = cv.pyrUp(img, (w*2, h*2), borderType= cv.BORDER_DEFAULT)
dst2= cv.pyrDown(img)

# draw image
output = img.copy()
# cv.rectangle(img, 시작 좌표(pt1)부터 도착 좌표(pt2), color, 두께)
# pt1, pt2 X ==> rec 좌표 설정시(x, y, w, h)
rect = cv.rectangle(output, (300,20), (420,100), (0,0,255), 1)

# cv.circle(img, '중심점', '반지름', color, 두께= -1 공간채움)
circle = cv.circle(output, (h//2, w//2), 20, (0,255,0), -1)

# cv.line(img, 시작 좌표(pt1)부터 도착 좌표(pt2), color, 두께) + linetype = cv.LINE_AA = 라인을 
line = cv.line(output, (60, 20), (400, 200), (0, 255, 255), 5)

# cv.putText(img, text, '좌측 상단 모서리(org)', fontFace, fontScale, color)
# 추가로 선형 타입(lineType), 기준 좌표(bottomLeftOrigin)를 설정가능( 한글 깨짐 )
puttext = cv.putText(output, 'draw image', (10,25) ,cv.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), 3)

# cv.namedWindow('Rectangle', cv.WINDOW_NORMAL) = 마우스로 이미지 크기 조절 가능
cv.imshow('dst', dst)
cv.imshow('dst2', dst2)
cv.imshow('Rectangle, Circle, line, puttext', puttext)
cv.waitKey()
