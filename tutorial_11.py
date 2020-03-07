
# 直方图反向投影实现

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def video_demo(sample):
    capture = cv.VideoCapture('pan1.mp4')
    while True:
        ret,frame = capture.read()
        backProjecting_demo(sample,frame)
        cv.imshow('video',frame)
        c = cv.waitKey(50)
        if c == 27 :#按下esc停止
            break;


def backProjecting_demo(sample,target):

    roi_hsv = cv.cvtColor(sample,cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    # cv.imshow('sample',sample)
    #cv.imshow('target', target)

    roiHist = cv.calcHist([roi_hsv],[0,1],None,[36,16],[0,180,0,256])
    cv.normalize(roiHist,roiHist,0,255,cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv],[0,1],roiHist,[0,180,0,256],1)
    cv.imshow('backProjectionDemo',dst)


def hist2D_demo(image):
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image],[0,1],None,[180,256],[0,180,0,256])
    # cv.imshow('hist2D_demo',hist)
    plt.imshow(hist,interpolation='nearest')
    plt.title('2D Histogram')
    plt.show()


print('---------------------Hello Python-------------------------')
# src = cv.imread('demo5.jpg')
# cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
# cv.imshow('input image',src)
sample = cv.imread('demo9.jpg')
video_demo(sample)
cv.waitKey(0)
cv.destroyAllWindows()
