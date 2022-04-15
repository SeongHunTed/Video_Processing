import numpy as np
import cv2
from Common.utils import print_matInfo

image = cv2.imread("images/ssu.jpg", cv2.IMREAD_COLOR)
logo = cv2.imread("images/ssu_logo1.jpg", cv2.IMREAD_COLOR)
logo2 = cv2.imread("images/ssu_logo2.jpg", cv2.IMREAD_COLOR)
if image is None or logo is None or logo2 is None:
    raise Exception("영상 파일 읽기 오류")

cv2.imshow('logo origin', logo)
logo[0:87, 220:700] = logo2

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1]) #전면 마스크
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask) #배경마스크

# print(image.shape) 638, 960, 3

(H, W), (h, w) = image.shape[:2], logo.shape[:2]

x, y = (W-w)//2, (H-h)//6

roi = image[y:y+h, x:x+w]

foreground = cv2.bitwise_and(logo, logo, mask=bg_pass_mask) #흰색바탕 검은글씨
background = cv2.bitwise_and(roi, roi, mask=fg_pass_mask) #검은바탕 흰색글씨

dst = cv2.add(background, foreground)
image[y:y+h, x:x+w] = dst


cv2.imshow('logo2 origin', logo2)
cv2.imshow('logo1 merged', logo)


titles = ['foreground', 'background', 'dst', 'image']
for title in titles:
    cv2.imshow(title, eval(title))

cv2.waitKey(0)


#슬라이스 연산자 사용해서 로고 두개 합치기
