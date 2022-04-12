import numpy as np
import cv2

switch_case = {
    ord('a'): "a키 입력",
    0x41: "A키 입력"
}

image = np.ones((200, 300), np.float64)
cv2.namedWindow('Keyboard Event')
cv2.imshow('Keyboard Event', image)

while True:
    key = cv2.waitKey(100)
    if key == 27: break

    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()