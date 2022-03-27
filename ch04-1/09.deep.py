import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            dx, dy = np.abs(pt[0] - x), np.abs(pt[1] - y)
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
            cv2.ellipse(image, (int((pt[0]+x)/2), int((pt[1]+y)/2)), (int(dx/2), int(dy/2)), 0, 225, 45, (0, 255, 0), 2)
            cv2.imshow(title, image)
            pt = (-1, -1)
        print("왼쪽 마우스 클릭")

    if event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            dx, dy = np.abs(pt[0] - x), np.abs(pt[1] - y)
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
            cv2.ellipse(image, (int((pt[0]+x)/2), int((pt[1]+y)/2)), (int(dx/2), int(dy/2)), 180, 45, 225, (0, 255, 0), 2)
            cv2.imshow(title, image)
            pt = (-1, -1)
        print("오른쪽 마우스 클릭")

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1) #시작 좌표 초기화
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)