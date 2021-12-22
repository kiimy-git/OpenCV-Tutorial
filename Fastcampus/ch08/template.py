import sys
import numpy as np
import cv2


# 입력 영상 & 템플릿 영상 불러오기
# templ 위치 찾기
src = cv2.imread('ch08\\images\\circuit.bmp', cv2.IMREAD_GRAYSCALE)
templ = cv2.imread('ch08\\images\\crystal.bmp', cv2.IMREAD_GRAYSCALE)

if src is None or templ is None:
    print('Image load failed!')
    sys.exit()

# noise 추가
# 입력 영상 밝기 50증가, 가우시안 잡음(sigma=10) 추가
# np.random.normal(loc=0.0, scale=1.0, size=None)
# 평균, 표준편차
noise = np.zeros(src.shape, np.int32)
cv2.randn(noise, 50, 10)
src_noise = cv2.add(src, noise, dtype=cv2.CV_8UC3)

# 템플릿 매칭 & 결과 분석
'''
cv2.matchTemplate(image, templ, method, result=None, mask=None) -> result
image와 templ는 8비트 or 32비트
result=  (W - w + 1) * (H - h +1) = 32비트의 단일 채널 이미지로 반환
W, H = 입력 영상의 이미지
w, h = template 이미지
method = SQDIFF(완전히 같으면 0, 다르면 값이 커짐)
         CCORR(같으면 큰값, 다르면 작은 값)
         CCOEFF_NORMED(완전히 일치하면 1, 역일치 -1, 연관성 없으면 0)

** 회전, 크기변환이 클 때는 찾기 어려움 ==> keypoint(Local Feature Matching)
'''

res = cv2.matchTemplate(src_noise, templ, cv2.TM_CCOEFF_NORMED)
# 영상을 보기 위함(normalize) = 유난히 밝은 흰색 부분을 찾을 수 있음
res_norm = cv2.normalize(res, None, 0,255, cv2.NORM_MINMAX, cv2.CV_8U)

# minv, maxv, minloc, maxloc(위치)
_, maxv, _, maxloc = cv2.minMaxLoc(res)
'''
Tip : cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED는 최소 지점(minLoc)이 검출된 위치
Tip : cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED는 
      최대 지점(maxLoc)이 검출된 위치

      # 유사도 - 최댓값, 비슷한 부분이 밝게
      # 비유사도 - 최솟값, 비슷한 부분이 어둡게

만약 내가 찾고자하는 이미지가 없는 이미지에서 실행을 한다?
어느 위치든 박스를 그려 찾아낼 것이다
즉, 있으면 maxv가 큰 값을 가질테고 없다면 고만고만한것으로 return 하게 될것인데
이를 Threshold(임계값)을 부여해서 임계값보다 클 경우에만 있다고 판단 
'''
print('maxv:', maxv)
print('maxloc:', maxloc) # x, y

# 매칭 결과를 빨간색 사각형으로 표시
th, tw = templ.shape[:2]
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
cv2.rectangle(dst, maxloc, (maxloc[0] + tw, maxloc[1] + th), (0,0,255), 2)

cv2.imshow('src', src)
cv2.imshow('templ', templ)
cv2.imshow('src_noise', src_noise)
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()