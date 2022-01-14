
#Taken from -> https://answers.opencv.org/question/222388/detect-ellipses-ovals-in-images-with-opencv-pythonsolved/

#This program uses adaptioveeThreshold from OpenCV to identify ovals

import cv2
import numpy as np

t2 = cv2.imread('Test2.jpg')
thresh = cv2.cvtColor(t2, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(thresh, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 101, 0)
count, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)
for i in range(1,count):
    t2 = cv2.circle(t2, (int(centroids[i,0]), int(centroids[i,1])), 5, (0, 255, 0, 0), 5)

cv2.imshow('circles', thresh)
cv2.imshow('centers', t2)
cv2.waitKey()

