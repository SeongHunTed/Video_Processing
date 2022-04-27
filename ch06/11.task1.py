import numpy as np
import cv2

def onChange(value):
    global image3, title, image1, image2, alpha
    alpha = value/100
    image3 = cv2.addWeighted(image1, alpha, image2, 1-alpha, 0)
    dst1 = cv2.hconcat([image1, image3])
    dst2 = cv2.hconcat([dst1, image2])
    cv2.imshow(title, dst2)

def onChange2(value):
    global image3, title, image1, image2, alpha
    alpha = value/100
    image3 = cv2.addWeighted(image1, 1-alpha, image2, alpha, 0)
    dst1 = cv2.hconcat([image1, image3])
    dst2 = cv2.hconcat([dst1, image2])
    cv2.imshow(title, dst2)

alpha = 0
image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)
image3 = cv2.addWeighted(image1, 1, image2, 1, 0)
dst1 = cv2.hconcat([image1, image3])
dst2 = cv2.hconcat([dst1, image2])

title = "dst2"
bar_name = "image1"
bar_name2 = "image2"
cv2.imshow(title, dst2)
cv2.createTrackbar(bar_name, title, 1, 100, onChange)
cv2.createTrackbar(bar_name2, title, 1, 100, onChange2)

cv2.waitKey(0)