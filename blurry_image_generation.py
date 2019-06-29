import numpy
import argparse
import cv2
import os

image = cv2.imread('img.jpeg')
path1 = './image_average'
path2 = './image_gaussian'
path3 = './image_median'
path4 = './image_bilateral'

for i in range(10):
    j = i+1
    # 4 method 
    blur = cv2.blur(image, (3*j,3*j))          #  average
    #blur = cv2.GaussianBlur(image, (2*j+1,2*j+1), 0)   #  Gaussian
    #blur = cv2.medianBlur(image, 2*j+1)       #  median
    #blur = cv2.bilateralFilter(image, j*3,j*20,20+j*20)  #  bilateral
    j = str(j)
    if not os.path.exists(path1):
        os.makedirs(path1)
    
    cv2.imwrite(path1 + "/image" + j + ".jpeg",blur)
