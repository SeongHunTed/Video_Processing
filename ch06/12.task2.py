import numpy as np, cv2
from Common.histogram import draw_histo

image = cv2.imread("images/low.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("Open Image Error")

hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

H, S, I = cv2.split(hsv_img)

I_ = cv2.equalizeHist(I)
merge_hsv = cv2.merge([H, S, I_])
dst = cv2.cvtColor(merge_hsv, cv2.COLOR_HSV2BGR)

cv2.imshow("changed", dst)
cv2.waitKey(0)

