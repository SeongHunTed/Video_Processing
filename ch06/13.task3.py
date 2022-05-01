import numpy as np
import cv2

title = "Blending"
bar_name1 = "image1"
bar_name2 = "image2"
global alpha

def onChange1(value):
    global alpha
    alpha = value/100
    dst = cv2.addWeighted(image1, alpha, image2, 1-alpha, 0)
    dst1 = cv2.hconcat([image1, dst])
    dst2 = cv2.hconcat([dst1, image2])
    cv2.imshow(title, dst2)

def onChange2(value):
    global alpha
    alpha = value/100
    dst = cv2.addWeighted(image1, 1-alpha, image2, alpha, 0)
    dst1 = cv2.hconcat([image1, dst])
    dst2 = cv2.hconcat([dst1, image2])
    cv2.imshow(title, dst2)

alpha = 0
image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)

dst1 = cv2.hconcat([image1, image2])
dst2 = cv2.hconcat([dst1, image2])


cv2.imshow(title, dst2)
cv2.createTrackbar(bar_name1, title, 0, 100, onChange1)
cv2.createTrackbar(bar_name2, title, 0, 100, onChange2)
cv2.waitKey(0)