import cv2
import numpy as np

image = cv2.imread("images/minMax.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("error")

(min_val, max_val, _, _) = cv2.minMaxLoc(image)

ratio = 255/(max_val - min_val)
dst = np.round((image- min_val)*ratio).astype('uint8')
