import cv2

image = cv2.imread("images/flip_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류 발생")

x_axis = cv2.flip(image, 0)
y_axis = cv2.flip(image, 1)
xy_axis = cv2.flip(image, -1)
rep_image = cv2.repeat(image, 1, 2)
trans_image = cv2.transpose(image)
trans_image_trans = cv2.transpose(trans_image)

titles = ['image', 'x_axis', 'y_axis', 'xy_axis', 'rep_image', 'trans_image', 'trans_image_trans']

for title in titles:
    cv2.imshow(title, eval(title))

cv2.waitKey(0)