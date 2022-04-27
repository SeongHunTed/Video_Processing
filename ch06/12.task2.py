import numpy as np, cv2

image = cv2.imread("images/low.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("Open Image Error")

hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
Hue, Saturation, Intensity = cv2.split(hsv_img)

# bins, ranges = [256], [0, 256]
# hist = cv2.calcHist([image], [0], None, bins, ranges)
# accum_hist = np.zeros(hist.shape[:2], np.float32)
# accum_hist[0] = hist[0]
#
# for i in range(1, hist.shape[0]):
#     accum_hist[i] = accum_hist[i-1] + hist[i]
#
# accum_hist = (accum_hist / sum(hist)) * 255
# dst

dst = cv2.equalizeHist(Intensity)

cv2.imshow("image", dst)
cv2.waitKey(0)

