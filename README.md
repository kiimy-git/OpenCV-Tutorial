# ✒️ opencv 4.5.4 tutorial
[![](https://img.shields.io/badge/opencv-v4.5.4-orange.svg)](https://opencv.org/) [![](https://img.shields.io/badge/opencv-tutorial-brightgreen.svg)](https://docs.opencv.org/4.0.0/d9/df8/tutorial_root.html)

[My_Blog](https://cord-ai.tistory.com/)

## Learning
***Annotation:***
- ✔️  **: Basic**
- ✏️  **: Attention**
- 🎯  **: Functions coding**

## FastCampus
No    | Description   | Annotation
:--------: | :--------: | :--------:
-- | ##########[CH01 OpenCV-Python 시작하기](Fastcampus/ch01)########## | --
ch01 | [Image_basic](Fastcampus/ch01/ch01_basic.ipynb)   | ✔️
ch01 | [Slide](Fastcampus/ch01/slide.py)   | 🎯
-- | ##########[CH02 OpenCV-Python 기초 사용법](Fastcampus/ch02)########## | --
ch02 | [Drawing (line, rectangle, cicle, polylines, puttext + linetpye)](Fastcampus/ch02/drawing.py)   | ✔️
ch02 | [Image_info (shape, dtype)](Fastcampus/ch02/img_info.py)   | ✔️
ch02 | [Image_ops (empty, zeors, ones, full, img_slicing)](Fastcampus/ch02/img_ops.py)   | ✔️
ch02 | [Plus_mask (mask, copyTo)](Fastcampus/ch02/plus_mask.py)   | ✔️
ch02 | [Camera_in (VideoCapture, cv.get, CAP_PROP_FRAME_WIDTH)](Fastcampus/ch02/mouse_event.py)   | ✔️
ch02 | [Camera_out (VideoWriter_fourcc, VideoWriter)](Fastcampus/ch02/camera_in.py)   | ✔️
ch02 | [Mouse_event (setMouseCallback, onMouse, EVENT_LBUTTONDOWN, EVENT_FLAG_LBUTTON)](Fastcampus/ch02/mouse_event.py)   | 🎯
ch02 | [Trackbar (createTrackbar, onChange)](Fastcampus/ch02/trackbar.py)   | ✏️
ch02 | [Time_check (TickMeter, time.time, getTimeSec)](Fastcampus/ch02/time_check.py)   | ✏️
ch02 | [Plus_video (effect_frames)](Fastcampus/ch02/plus_video.py)   | 🎯
-- | ##########[CH03 기본적인 영상 처리 기법](Fastcampus/ch03)########## | --
ch03 | [Brightness (add)](Fastcampus/ch03/brightness.py)    |✔️
ch03 | [산술연산(Arithmetic) (add, addweighted, substract, absdiff)](Fastcampus/ch03/arithmetic.py)    |✔️
ch03 | [Color (split)](Fastcampus/ch03/color.py)    |✔️
ch03 | [Histogram (calcHist)](Fastcampus/ch03/histogram.py)    | ✔️
ch03 | [Constrast1 (np.clip)](Fastcampus/ch03/contrast1.py)    | ✔️
ch03 | [Constrast2 - Histogram stretching (normalized)](Fastcampus/ch03/contrast2.py)    | ✏️
ch03 | [Equalize (equalizeHist)](Fastcampus/ch03/equalize.py)    | ✔️(??)
ch03 | [InRange (inRange, createTrackbar, getTrackbarpos)](Fastcampus/ch03/inrange.py)    | ✏️
ch03 | [BackProjection (selectROI, normalize, calcBackProject, copyTo)](Fastcampus/ch03/backproject1.py)    | ✏️
ch03 | [BackProjection (mask, normalize, calcBackProject)](Fastcampus/ch03/backproj2.py)    | ✔️
ch03 | [Chroma_key](Fastcampus/ch03/chroma_key.py)    | 🎯
-- | ##########[CH04 필터링](Fastcampus/ch04)########## | --
ch04 | [Blurring (filter2D, blur)](Fastcampus/ch04/blurring.py)    | ✔️
ch04 | [Gaussianblur (GaussianBlur)](Fastcampus/ch04/gaussian.py)    | ✔️
ch04 | [Sharpening-gray (GaussianBlur, subtract, addWeighted, np.clip)](Fastcampus/ch04/sharpening1.py)    | ✏️(coding)
ch04 | [Sharpening-color (GaussianBlur, np.clip)](Fastcampus/ch04/sharpening2.py)    | ✏️(coding)
ch04 | [Median (medianBlur)](Fastcampus/ch04/median.py)    | ✔️
ch04 | [Bilateral (bilateralFilter)](Fastcampus/ch04/bilateral.py)    | ✔️
ch04 | [Cartoon_cam (Canny, bitwise_and, divide)](Fastcampus/ch04/cartoon_cam.py)    | 🎯
-- | ##########[CH05 기하학적 변환](Fastcampus/ch05)########## | --
ch05 | [Translate, Shear (wrapAffine)](Fastcampus/ch05/translate.py)    | ✔️
ch05 | [Scaling (resize)](Fastcampus/ch05/scaling.py)    | ✔️
ch05 | [Pyramid (pyrDown, pyrUp, rectangle(shift))](Fastcampus/ch05/pyramid.py)    | ✔️
ch05 | [Rotation (getRotationMatrix2D, warpAffine)](Fastcampus/ch05/rotaion.py)    | ✔️
ch05 | [Perspective (getPerspectiveTransform, warpPerspective)](Fastcampus/ch05/perspective.py)    | ✏️
ch05 | [Remapping (np.indices, remap)](Fastcampus/ch05/remapping.py)    | ✏️
ch05 | [DocuScan (EVENT_MOUSE, getPerspectiveTransform)](Fastcampus/ch05/docuscan.py)    | 🎯
-- | ##########[CH06 영상의 특징 추출](Fastcampus/ch06)########## | --
ch06 | [Sobel (Sobel)](Fastcampus/ch06/sobel.py)    | ✔️
ch06 | [Sobel_gradient (magnitude, clip, threshold, phase)](Fastcampus/ch06/sobel_gradient.py)    | ✏️
ch06 | [Canny (canny, trackbar)](Fastcampus/ch06/canny.py)    | ✏️
ch06 | [Hough_lines (GaussianBlur, HoughLinesP, canny)](Fastcampus/ch06/hough_lines.py)    | ✏️
ch06 | [Hough_circles (cvtColor, GaussianBlur, HoughCircles)](Fastcampus/ch06/hough_circles.py)    | ✔️
ch06 | [Coin_count using HUE (cvtColor, GaussianBlur, HoughCircles, Histogram, mean)](Fastcampus/ch06/coin_count.py)    | 🎯
-- | ##########[CH07 이진 영상 처리](Fastcampus/ch07)########## | --
ch07 | [Threshold (Threshold)](Fastcampus/ch07/threshold.py)    | ✔️
ch07 | [Otsu (THRESH_OTSU)](Fastcampus/ch07/otsu.py)    | ✔️
ch07 | [Local_Otsu (Coding)](Fastcampus/ch07/local_otsu.py)    | ✏️(coding)
ch07 | [Adaptive_th (adaptiveThreshold)](Fastcampus/ch07/adaptive_th.py)    | ✔️
ch07 | [Morphology (getStructuringElement, erode, dilate)](Fastcampus/ch07/morphology.py)    | ✔️
ch07 | [morphologyEx, labeling (connectedComponents, morphologyEx)](Fastcampus/ch07/morphologyEx.py)    | ✔️
ch07 | [Keyboard_labeling (connectedComponentsWithStats](Fastcampus/ch07/keyboard.py)    | ✏️
ch07 | [Contours_hierarchy (findContours, hierarchy)](Fastcampus/ch07/contours_hierarchy.py)    | ✏️
ch07 | [Contours_contours (findContours, contours)](Fastcampus/ch07/contours_contours.py)    | ✏️
ch07 | [Polygon_detection (findContours, contours, approxPolyDP, arcLength, contourArea)](Fastcampus/ch07/detection.py)    | ✔️
ch07 | [Tesseract (pytesseract.image_to_string)](Fastcampus/ch07/tesseract.py)    | 🎯
-- | ##########[CH08 영상 분할과 객체 검출](Fastcampus/ch08)########## | --
ch08 | [Grabcut1 (grabcut, np.where)](Fastcampus/ch08/grabcut1.py)    | ✔️
ch08 | [Grabcut2 (setMousecallback, grabcut, bgdModel, fgdModel, np.where)](Fastcampus/ch08/grabcut2.py)    | ✔️
ch08 | [MatchShape (Threshold, findContours, boundingRect, matchShapes)](Fastcampus/ch08/matchshape.py)    | ✔️
ch08 | [Template_match (matchTemplate, TM_CCOEFF_NORMED)](Fastcampus/ch08/template.py)    | ✏️
ch08 | [Digit_detect (connectedComponentsWithStats, matchTemplate)](Fastcampus/ch08/digit_detect.py)    | ✔️
ch08 | [Face_detect (CascadeClassifier, detectMultiScale)](Fastcampus/ch08/face_detect.py)    | ✏️
ch08 | [Eye_detect (CascadeClassifier, detectMultiScale)](Fastcampus/ch08/eye_detect.py)    | ✏️
ch08 | [People_detect (HOGDescriptor, setSVMDetector, HOGDescriptor_getDefaultPeopleDetector, detectMultiScale)](Fastcampus/ch08/people_detect.py)    | ✏️
-- | ##########[CH09 특징점 검출과 매칭](Fastcampus/ch09)########## | --
ch09 | [Corners (goodFeaturesToTrack, FastFeatureDetector_create)](Fastcampus/ch09/corners.py)    | ✔️
ch09 | [Descriptor (drawKeypoints)](Fastcampus/ch09/descriptors.py)    | ✔️
ch09 | [Matching (detectAndCompute, BFMatcher_create, match)](Fastcampus/ch09/matching.py)    | ✔️
ch09 | [Good_match (sorted(matches, key=lambda x: x.distance))](Fastcampus/ch09/good_match.py)    | ✏️
ch09 | [Good_match_KNN (knnMatch)](Fastcampus/ch09/Good_match_knn.py)    | ✏️
ch09 | [Homography (findHomography, perspectiveTransform)](Fastcampus/ch09/homography.py)    | ✏️
ch09 | [Stitching_PANORAMA (Stitcher_create, stitch)](Fastcampus/ch09/stitching.py)    | ✔️
-- | ##########[CH10 객체 추적과 모션 벡터](Fastcampus/ch10)########## | --
ch10 | [BS_static (absdiff, threshold, connectedComponentsWithStats)](Fastcampus/ch10/BS_static.py)    | ✔️
ch10 | [BS_moveavg (back.astype(np.float32), accumulateWeighted)](Fastcampus/ch10/BS_moveavg.py)    | ✏️
ch10 | [BS_MOG2 (createBackgroundSubtractorKNN, createBackgroundSubtractorMOG2, apply, getBackgroundImage)](Fastcampus/ch10/BS_MOG2.py)    | ✏️
ch10 | [MeanShift (term_crit, calcBackProject, meanShift)](Fastcampus/ch10/meanshift.py)    | ✔️
ch10 | [CamShift (term_crit, calcBackProject, CamShift)](Fastcampus/ch10/camshift.py)    | ✏️
ch10 | [Optical_flow_LK (goodFeaturesToTrack, calcOpticalFlowPyrLK)](Fastcampus/ch10/optical_flow_LK.py)    | HARD
ch10 | [Optical_flow_LK_video (calcOpticalFlowPyrLK)](Fastcampus/ch10/optical_flow_LK_video.py)    | HARD
ch10 | [Optical_flow_Farne (calcOpticalFlowFarneback, cartToPolar)](Fastcampus/ch10/optical_flow_Farne.py)    | HARD
ch10 | [Tracker (TrackerMIL_create, init, update)](Fastcampus/ch10/tracker.py)    | ✔️
-- | ##########[CH11 머신 러닝](Fastcampus/ch11)########## | --
ch11 | [KNN (cv2.ml.KNearest_create, findNearest)](Fastcampus/ch11/knn.py)    | ✔️
ch11 | [HOG & SVM (HOGDescriptor, cv2.ml.SVM_create, compute)](Fastcampus/ch11/svm.py)    | ✔️
ch11 | [K_Means (criteria, cv2.kmeans)](Fastcampus/ch11/kmeans.py)    | ✔️
ch11 | [Digits_recognition (HOGDescriptor, threshold, connectedComponentsWithStats, compute)](Fastcampus/ch11/digit_recog.py)    | 🎯




## Tutorials
No    | Description   | Annotation
:--------: | :----------------: | :--------:
code001 | [load_image](tutorials/code001/code001.py) | ✔️
code002 | [rotated, flip (getRotationMatrix2D, warpAffine)](tutorials/code002/code002.py) | ✔️
code003 | [pyramid (pyrUp, pyrDown), image draw + linetype](tutorials/code003/code003.py) | ✔️
code004 | [canny, sobel, threshold, findcontour, drawcontour, puttext](tutorials/code004/code004.py) | ✔️
code005 | [이미지 형태 전환 (Morphological Transformations) erode, dilate](tutorials/code005/code005.py) | ✔️
code006 | [bitwise_and ( img, img, mask=mask )](tutorials/code006/code006.py) | ✔️
code007 | [HSV (inRange, bitwise_and)](tutorials/code007/code007.py) | ✏️
code008 | [Image Resize](tutorials/code008/code008.py) | ✔️
code009 | [모폴로지 연산(Perspective Calculate) opening, closing, gradient](tutorials/code009/code009.py) | ✏️
code009 | [배열정합(addWeighted)](tutorials/code010/code010.py) | ✔️
