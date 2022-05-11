import numpy as np, cv2
from Common.utils import contain

def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)
    for i in range(img.shape[0]):       # 행 정보
        for j in range(img.shape[1]):
            x, y = np.subtract((j,i), pt)
            if contain((y, x), img.shape):
                dst[i, j] = img[y, x]
    return dst

image = cv2.imread('images/translate.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("Open Image Error")

dst1 = translate(image, (30, 80))
dst2 = translate(image, (-70, -50))

cv2.imshow("image", image)
cv2.imshow("dst1 : trans to (80, 30)", dst1)
cv2.imshow("dst2 : trans to (-50, -70)", dst2)
cv2.waitKey(0)