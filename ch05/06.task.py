import numpy as np
import cv2
from Common.utils import print_matInfo

image = cv2.imread("images/ssu.jpg", cv2.IMREAD_COLOR)
src1 = cv2.imread("images/ssu_logo1.jpg", cv2.IMREAD_COLOR)
src2 = cv2.imread("images/ssu_logo2.jpg", cv2.IMREAD_COLOR)
if image is None or src1 is None or src2 is None:
    raise Exception("영상 파일 읽기 오류")

mask1 = cv2.threshold(src1, 220, 255, cv2.THRESH_BINARY)[1]
mask1 = cv2.split(mask1)

fg_pass_mask1 = cv2.bitwise_or(mask1[0], mask1[1])
fg_pass_mask1 = cv2.bitwise_or(mask1[2], fg_pass_mask1) # 전경 통과 마스크
bg_pass_mask1 = cv2.bitwise_not(fg_pass_mask1)

mask2 = cv2.threshold(src2, 220, 255, cv2.THRESH_BINARY)[1]
mask2 = cv2.split(mask2)

fg_pass_mask2 = cv2.bitwise_or(mask2[0], mask2[1])
fg_pass_mask2 = cv2.bitwise_or(mask2[2], fg_pass_mask2) # 전경 통과 마스크
bg_pass_mask2 = cv2.bitwise_not(fg_pass_mask2)

(hLogo, wLogo), (h, w) = src1.shape[:2], src2.shape[:2]
xl, yl = int((wLogo - w)/2), int((hLogo-h)/2)
roi = image[yl:yl+h, xl:xl+w]

foreground = cv2.bitwise_and(src1, src1, mask=fg_pass_mask1)
background = cv2.bitwise_and(src2, src2, mask = fg_pass_mask2)


dst = cv2.add(background, foreground)

cv2.imshow('dst', dst)


#슬라이스 연산자 사용해서 로고 두개 합치기

cv2.waitKey(0)