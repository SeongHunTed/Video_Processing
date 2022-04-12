import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            dx = abs(pt[0]-x)
            dy = abs(pt[1]-y)
            center = ((pt[0]+x)//2, (pt[1]+y)//2)
            size = int(np.linalg.norm(np.array(pt) - np.array(center)))
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
            cv2.ellipse(image, center, (size, size), 0, 45, 225, (0,255,0), 3)
            cv2.imshow(title, image)
            pt = (-1, -1)

    if event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            dx = abs(pt[0]-x)
            dy = abs(pt[1]-y)
            center = ((pt[0]+x)//2, (pt[1]+y)//2)
            size = int(np.linalg.norm(np.array(pt) - np.array(center)))
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
            cv2.ellipse(image, center, (size, size), 180, 225, 45, (0, 255, 0), 3)
            cv2.imshow(title, image)
            pt = (-1, -1)

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)