import numpy as np, cv2
from Common.interpolation import bilinear_value
from Common.utils import contain

def rotate(img, degree):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree / 180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    for yd in range(img.shape[0]):
        for xd in range(img.shape[1]):
            y = int(yd * cos - xd * sin)
            x = int(xd * cos + yd * sin)
            if contain((y, x), img.shape):
                dst[yd, xd] = img[y, x]
    return dst

def rotate_bilinear(img, degree):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree / 180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    for yd in range(img.shape[0]):
        for xd in range(img.shape[1]):
            y = yd * cos - xd * sin
            x = xd * cos + yd * sin
            if contain((y, x), img.shape):
                dst[yd, xd] = bilinear_value(img, [x, y])
    return dst


image = cv2.imread("images/rotate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("Open Image Error")

center = np.divmod(image.shape[::-1], 2)[0]
dst1 = rotate(image, 20)
dst2 = rotate_bilinear(image, 20)

cv2.imshow("image", image)
cv2.imshow("dst1-rotated on org", dst1)
cv2.imshow("dst2-rotated on org with bilinear", dst2)
cv2.waitKey(0)