import numpy as np, cv2
from Common.utils import time_check

def scaling(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    y = np.arange(0, img.shape[0], 1)
    x = np.arange(0, img.shape[1], 1)
    y, x = np.meshgrid(y, x)
    # print(x)
    # print(y)

    # 순방향 사상
    i, j = np.int32(y*ratioY), np.int32(x*ratioX)
    dst[i, j] = img[y, x]
    return dst

def scaling2(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            i, j = int(y*ratioY), int(x*ratioX)
            dst[i, j] =img[y, x]

    return dst

image = cv2.imread("images/scaling.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception ("Open Image Error")

dst1 = scaling(image, (150, 200))
dst2 = scaling2(image, (150, 200))
dst3 = time_check(scaling(image, (300, 400)), "[method1] 정방행렬 방식 >")
dst4 = time_check(scaling2(image, (300, 400)), "[method2] 반복문 방시 >")

cv2.imshow("image", image)
cv2.imshow("dst1 - zoom in", dst1)
cv2.imshow("dst3 - zoom out", dst3)
cv2.imshow("dst2 - zoom in", dst2)
cv2.imshow("dst4 - zoom out", dst4)
cv2.waitKey(0)
