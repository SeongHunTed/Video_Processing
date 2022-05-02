import numpy as np
import cv2

title = "Blending"
bar_name1 = "image1"
bar_name2 = "image2"

def onChange(value):

    th[0] = cv2.getTrackbarPos(bar_name1, title)
    alpha = th[0]/100
    th[1] = cv2.getTrackbarPos(bar_name2, title)
    beta = th[1]/100
    dst = cv2.addWeighted(image1, alpha, image2, beta, 0)
    dst1 = cv2.hconcat([image1, dst])
    dst2 = cv2.hconcat([dst1, image2])
    cv2.imshow(title, dst2)


th = [0, 0]
image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)

dst1 = cv2.hconcat([image1, image2])
dst2 = cv2.hconcat([dst1, image2])


cv2.imshow(title, dst2)
cv2.createTrackbar(bar_name1, title, th[0], 100, onChange)
cv2.createTrackbar(bar_name2, title, th[1], 100, onChange)
cv2.waitKey(0)