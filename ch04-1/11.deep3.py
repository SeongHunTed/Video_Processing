import numpy as np
import cv2

click = False

def onMouse(event, x, y, flags, param):
    global title, pt, pt_prev, click

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
            click = True

    if event == cv2.EVENT_MOUSEMOVE:
        if click == True:
            if pt_prev[0] > 0:
                pt_prev = (x, y)
                cv2.line(image, pt, (x, y), (0, 0, 255), 4, cv2.LINE_AA)
                cv2.imshow(title, image)

            cv2.line(image, pt, (x, y), (255, 255, 255), 5, cv2.LINE_AA)
            pt = pt
            pt_prev = (x, y)

    if event == cv2.EVENT_LBUTTONUP:
        click = False
        center = int((pt[0] + x) / 2), int((pt[1] + y) / 2)
        size = int(np.linalg.norm(np.array(pt) - np.array(center)))
        dx, dy = np.abs(pt[0] - x), np.abs(pt[1] - y)
        cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
        cv2.ellipse(image, center, (size, size), 0, 225, 45, (0, 255, 0), 2)
        cv2.imshow(title, image)
        pt = (-1, -1)
        pt_prev = (-1, -1)
        print("Button up")

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)
pt_prev = (-1, -1)
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)