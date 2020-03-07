import cv2 as cv
import numpy as np


print('---------------Hello Python!-----------------')
src = cv.imread('demo')
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
cv.waitKey(0)
cv.destroyAllWindows()