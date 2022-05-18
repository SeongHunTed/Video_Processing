import numpy as np, cv2


def symetry(img, type):
    h, w = img.shape[:2]
    dst = np.zeros(img.shape[:2], img.dtype)

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if type == 0:
                yd = h - 1 - y
                xd = x
                dst[yd, xd] = img[y, x]
            elif type == 1:
                yd = y
                xd = w - 1 - x
                dst[yd, xd] = img[y, x]
            elif type == 2:
                yd = h - 1 - y
                xd = w - 1 - x
                dst[yd, xd] = img[y, x]
    return dst


image = cv2.imread("images/lena.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("Open Image Error")

center = np.divmod(image.shape[::-1], 2)[0]
dst1 = symetry(image, 0)
dst2 = symetry(image, 1)
dst3 = symetry(image, 2)

cv2.imshow("image", image)
cv2.imshow("dst1-symetry type 1", dst1)
cv2.imshow("dst1-symetry type 2", dst2)
cv2.imshow("dst1-symetry type 3", dst3)
cv2.waitKey(0)

