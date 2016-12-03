{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf600
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue117;\red242\green242\blue242;\red38\green38\blue38;
\red0\green0\blue0;\red83\green85\blue2;\red82\green0\blue83;\red11\green84\blue83;\red115\green0\blue2;
\red16\green121\blue2;}
{\*\expandedcolortbl;\csgray\c100000;\cssrgb\c0\c0\c53333;\cssrgb\c96078\c96078\c96078;\cssrgb\c20000\c20000\c20000;
\cssrgb\c0\c0\c0;\cssrgb\c40000\c40000\c0;\cssrgb\c40000\c0\c40000;\cssrgb\c0\c40000\c40000;\cssrgb\c53333\c0\c0;
\cssrgb\c0\c53333\c0;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
import\cf4  numpy \cf2 as\cf4  np\
\cf2 import\cf4  cv2\
\
cap \cf6 =\cf4  cv2\cf6 .\cf7 VideoCapture\cf6 (\cf8 0\cf6 )\cf4 \
\
\cf2 while\cf6 (\cf4 cap\cf6 .\cf4 isOpened\cf6 ()):\cf4   \cf9 # check !\cf4 \
    \cf9 # capture frame-by-frame\cf4 \
    ret\cf6 ,\cf4  frame \cf6 =\cf4  cap\cf6 .\cf4 read\cf6 ()\cf4 \
\
    \cf2 if\cf4  ret\cf6 :\cf4  \cf9 # check ! (some webcam's need a "warmup")\cf4 \
        \cf9 # our operation on frame come here\cf4 \
        gray \cf6 =\cf4  cv2\cf6 .\cf4 cvtColor\cf6 (\cf4 frame\cf6 ,\cf4  cv2\cf6 .\cf4 COLOR_BGR2GRAY\cf6 )\cf4 \
\
        \cf9 # Display the resulting frame\cf4 \
        cv2\cf6 .\cf4 imshow\cf6 (\cf10 'frame'\cf6 ,\cf4  gray\cf6 )\cf4 \
\
    \cf2 if\cf4  cv2\cf6 .\cf4 waitKey\cf6 (\cf8 1\cf6 )\cf4  \cf6 &\cf4  \cf8 0xFF\cf4  \cf6 ==\cf4  ord\cf6 (\cf10 'q'\cf6 ):\cf4 \
        \cf2 break\cf4 \
\cf9 # When everything is done release the capture\cf4 \
cap\cf6 .\cf4 release\cf6 ()\cf4 \
cv2\cf6 .\cf4 destroyAllWindows\cf6 ()}