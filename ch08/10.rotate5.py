import numpy as np, cv2
from Common.interpolation import bilinear_value
from Common.utils import contain


def rotate_pt_by_math(img, degree, pt):
    radian = (degree / 180) * np.pi
    radian_90 = ((90 - degree) / 180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)
    cos_90 = np.cos(radian_90)

    h, w = img.shape[:2]
    hd = int(h * cos + w * cos_90)
    wd = int(h * cos_90 + w * cos)
    dst = np.zeros((hd, wd), img.dtype)

    Hy = img.shape[0] - 1

    w_padding = (wd - w) / 2
    h_padding = (hd - h) / 2

    for yd in range(dst.shape[0]):
        for xd in range(dst.shape[1]):
            xd_new = xd - w_padding
            yd_new = yd - h_padding

            x = ((Hy - yd_new) - pt[0]) * sin + (xd_new - pt[1]) * cos + pt[1]
            y = Hy -(((Hy - yd_new) - pt[0]) * cos - (xd_new - pt[1]) * sin + pt[1])
            if contain((y, x), img.shape):
                dst[yd, xd] = bilinear_value(img, [x, y])
    return dst


image = cv2.imread("images/rotate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("Open Image Error")

center = np.divmod(image.shape[::-1], 2)[0]
dst1 = rotate_pt_by_math(image, 20, center)

cv2.imshow("image", image)
cv2.imshow("dst1-rotated on center", dst1)
cv2.waitKey(0)