import numpy as np, cv2
from Common.utils import contain

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


def bilinear_value(img, pt):
    x, y = np.int32(pt)
    if x >= img.shape[1] - 1: x = x - 1
    if y >= img.shape[0] - 1: y = y - 1

    A, B, C, D = np.float32(img[y:y + 2, x:x + 2].flatten())

    alpha, beta = pt[0] - x, pt[1] - y
    E = A + alpha * (B - A)
    F = C + alpha * (D - C)
    X = E + beta * (F - E)

    return np.clip(X, 0, 255)