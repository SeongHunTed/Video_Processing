import numpy as np, cv2
from Common.interpolation import scaling

def scaling_nearest(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    i = np.arange(0, size[1], 1)
    j = np.arange(0, size[0], 1)
    i, j = np.meshgrid(i, j)

    # 역방향 사상
    y, x = np.int32(i / ratioY), np.int32(j / ratioX)
    dst[i, j] = img[y, x]

    return dst

image = cv2.imread("images/interpolation.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("Open Image Error")

dst1 = scaling(image, (350, 400))
dst2 = scaling_nearest(image, (350, 400))

cv2.imshow("images", image)
cv2.imshow("dst1 - forward mapping", dst1)
cv2.imshow("dst2 - NN interpolation", dst2)
cv2.waitKey(0)