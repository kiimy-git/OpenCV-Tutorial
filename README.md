# ✒️ opencv 4.5.4 tutorial
[![](https://img.shields.io/badge/opencv-v4.5.4-orange.svg)](https://opencv.org/) [![](https://img.shields.io/badge/opencv-tutorial-brightgreen.svg)](https://docs.opencv.org/4.0.0/d9/df8/tutorial_root.html)

## Introduction
### Source Code of Image Process for Image Deep Learning
[Blog](https://cord-ai.tistory.com/) ~ing

## Learning
***Annotation:***
- ✔️  **: Basic**
- ✏️  **: Attention**
- 🎯  **: Functions coding**

## FastCampus
No    | Description   | Annotation
:--------: | :--------: | :--------:
-- | ㅁㄴㅇㅁㄴㅇ | --
ch01 | [Image_basic](Fastcampus/ch01/ch01_basic.ipynb)   | ✔️
ch01 | [Slide](Fastcampus/ch01/slide.py)   | 🎯
-- | ㅁㄴㅇㅁㄴㅇ | --
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
-- | ㅁㄴㅇㅁㄴㅇ | --
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
-- | ㅁㄴㅇㅁㄴㅇ | --
ch04 | [Blurring (filter2D, blur)](Fastcampus/ch04/blurring.py)    | ✔️
ch04 | [Gaussianblur (GaussianBlur)](Fastcampus/ch04/gaussian.py)    | ✔️
ch04 | [Sharpening-gray (GaussianBlur, subtract, addWeighted, np.clip)](Fastcampus/ch04/sharpening1.py)    | ✏️(coding)
ch04 | [Sharpening-color (GaussianBlur, np.clip)](Fastcampus/ch04/sharpening2.py)    | ✏️(coding)
ch04 | [Median (medianBlur)](Fastcampus/ch04/median.py)    | ✔️
ch04 | [Bilateral (bilateralFilter)](Fastcampus/ch04/bilateral.py)    | ✔️
ch04 | [Cartoon_cam (Canny, bitwise_and, divide)](Fastcampus/ch04/cartoon_cam.py)    | 🎯
-- | ㅁㄴㅇㅁㄴㅇ | --
ch05 | [Translate, Shear (wrapAffine)](Fastcampus/ch05/translate.py)    | ✔️
ch05 | [Scaling (resize)](Fastcampus/ch05/scaling.py)    | ✔️
ch05 | [Pyramid (pyrDown, pyrUp, rectangle(shift))](Fastcampus/ch05/pyramid.py)    | ✔️
ch05 | [Rotation (getRotationMatrix2D, warpAffine)](Fastcampus/ch05/rotaion.py)    | ✔️
ch05 | [Perspective (getPerspectiveTransform, warpPerspective)](Fastcampus/ch05/perspective.py)    | ✏️
ch05 | [Remapping (np.indices, remap)](Fastcampus/ch05/remapping.py)    | ✏️
ch05 | [DocuScan (EVENT_MOUSE, getPerspectiveTransform)](Fastcampus/ch05/docuscan.py)    | 🎯
-- | ㅁㄴㅇㅁㄴㅇ | --
ch06 | [Sobel (Sobel)](Fastcampus/ch06/sobel.py)    | ✔️
ch06 | [Sobel_gradient (magnitude, clip, threshold, phase)](Fastcampus/ch06/sobel_gradient.py)    | ✏️
ch06 | [Canny (canny, trackbar)](Fastcampus/ch06/canny.py)    | ✏️
ch06 | [Hough_lines (GaussianBlur, HoughLinesP, canny)](Fastcampus/ch06/hough_lines.py)    | ✏️
ch06 | [Hough_circles (cvtColor, GaussianBlur, HoughCircles)](Fastcampus/ch06/hough_circles.py)    | ✔️
ch06 | [Coin_count using HUE (cvtColor, GaussianBlur, HoughCircles, Histogram, mean)](Fastcampus/ch06/coin_count.py)    | 🎯
-- | ㅁㄴㅇㅁㄴㅇ | --
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
-- | ㅁㄴㅇㅁㄴㅇ | --






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
