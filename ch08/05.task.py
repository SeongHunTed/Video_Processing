import numpy as np, cv2

def bilinear_interpolation(image, size):
    height = image.shape[0] # 150
    width = image.shape[1] # 141

    scale_x = width / size[1]  #0.42857142857142855
    scale_y = height / size[0] #0.42857142857142855

    dst = np.zeros(size, image.dtype)

    for i in range(size[0]): # 329 //height
        for j in range(size[1]): # 350 // width

            rx = scale_x * j
            ry = scale_y * i

            x1 = int(rx)
            y1 = int(ry)

            x2 = x1 + 1
            y2 = y1 + 1

            if x2>=width : x2 = width -1
            if y2>=height : y2 = height -1

            alpha = rx - x1
            beta = ry - y1

            A = float(image[y1, x1])
            B = float(image[y1, x2])
            C = float(image[y2, x1])
            D = float(image[y2, x2])
            E = A + alpha*(B-A)
            F = C + alpha*(D-C)
            X = E + beta*(F-E)

            dst[i, j] = np.clip(X, 0, 255)

    return dst

image = cv2.imread('images/interpolation.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("Open Image Error")

size = (350, 329)

dst1 = bilinear_interpolation(image, size)

cv2.imshow("image", image)
cv2.imshow("User_bilinear2", dst1)
cv2.waitKey(0)