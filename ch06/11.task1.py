import numpy as np, cv2

def onChange1(value):
    image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)
    alpha = value/100
    image3 = cv2.addWeighted(image1, 1-alpha, image2, alpha, 0)
    cv2.imshow("image1", image1)


# cv2.createTrackbar("image1", "dst2", 1, 100, onChange1)
# cv2.createTrackbar("image2", "dst2", 0, 100, onChange(0))

# cv2.imshow("dst2", dst2)
cv2.waitKey(0)