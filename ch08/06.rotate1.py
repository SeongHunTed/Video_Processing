import numpy as np, cv2
from Common.utils import contain


def rotate(img, degree):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree / 180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            xd = int(x * cos - y * sin)
            yd = int(x * sin + y * sin)
            if contain((yd, xd), dst.shape):
                dst[yd, xd] = img[y, x]
    return dst


image = cv2.imread("images/roate.jph", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("Open Image Error")

center = np.divmod(image.shape[::-1], 2)[0]
dst1 = rotate(image, 20)

cv2.imshow("image", image)
cv2.imshow("dst1-rotated on org", dst1)
cv2.waitKey(0)