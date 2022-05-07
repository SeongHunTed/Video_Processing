import numpy as np, cv2
from Common.filters import erode, dilate

def opening(img, mask):
    tmp = erode(img, mask)
    cv2.imshow("User erode", tmp)
    dst = dilate(tmp, mask)
    cv2.imshow("User dilate", dst)
    return dst

def closing(img, mask):
    tmp = dilate(img, mask)
    dst = erode(tmp, mask)
    return dst

image = cv2.imread("images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("Open Image Error")

mask = np.array([[0, 1, 0],
               [1, 1, 1],
               [0, 1, 0]]).astype("uint8")

th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]

dst1 = opening(th_img, mask)
dst2 = closing(th_img, mask)
dst3 = cv2.morphologyEx(th_img, cv2.MORPH_OPEN, mask)
dst4 = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, 1)

cv2.imshow("User opening", dst1)
cv2.imshow("User closing", dst2)
cv2.waitKey(0)