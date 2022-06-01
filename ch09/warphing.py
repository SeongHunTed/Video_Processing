import numpy as np
import cv2
import sys
import tkinter.messagebox
from matplotlib import pyplot as plt

def color_reset():
    global RGB, RGB_index
    RGB = [255, 0, 0]
    RGB_index = 0

def onMouse(event, x, y, flags, param):

    global ix, iy, drawing, is_First, dstP, dstQ, srcP, srcQ, RGB, RGB_index

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(param, (ix, iy), (x, y), (RGB[2], RGB[1], RGB[0]), 2)

        RGB[RGB_index] -= 30
        if(RGB[RGB_index] < 0):
            RGB[RGB_index] = 0
            RGB_index += 1
            if(RGB_index > 2):
                RGB_index = 0
            RGB[RGB_index] = 255

        if is_First:
            srcP.append([ix, iy])
            srcQ.append([x, y])
        else:
            dstP.append([ix, iy])
            dstQ.append([x, y])

def mouseBrush(img):
    drawing = img.copy()
    cv2.namedWindow('paint')
    cv2.setMouseCallback('paint', onMouse, param=drawing)

    while True:
        cv2.imshow('paint', drawing)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break
    cv2.destroyAllWindows()

    return drawing

def MsgBox1():
    tkinter.messagebox.showinfo('워핑 수행 도우미', '이미지 워핑을 성공적으로 수행하기 위해\n첫 번째 이미지와 같은 순서로 그려주세요.\n\n선을 다 그렸으면 ESC 키를 눌러주세요.')

def MsgBox2():
    tkinter.messagebox.showinfo('워핑 수행 도우미', '두 번째 이미지에서 선을 그릴 때\n두 번째 이미지와 같은 순서로 그려주세요.\n\n선을 다 그렸으면 ESC 키를 눌러주세요.')

def MsgBox3():
    tkinter.messagebox.showinfo('워핑 수행 도우미', '제어선 그리기 완료!\n순서가 안맞거나 잘 못 그리셨다면 프로그램을 재시작해주세요\n\n확인 버튼을 누르면 모핑울 시작합니다..')

def MsgBox_Fail1():
    tkinter.messagebox.showinfo('워핑 수행 도우미', '워핑 실패\n제어선의 수가 일치하지 않습니다.\n다시 시도해주세요.')

def MsgBox_Fail2():
    tkinter.messagebox.showinfo('워핑 수행 도우미', '워핑 실패\n제어선이 잘 못 그려진 것 같습니다.\n다시 시도해주세요.')

def MsgBox_Success():
    tkinter.messagebox.showinfo('워핑 수행 도우미', '워핑 완료!\n결과를 확인해주세요')


def perpendicular(a):
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b


def warphing(img1, outputs):

    height, width, channels = img1.shape

    #DeltaP and DeltaQ 계산부
    dP = (np.array(dstP) - np.array(srcP))
    dQ = (np.array(dstQ) - np.array(srcQ))

    # 제어선 좌표 미리 저장
    P1 = np.array(srcP)
    P2 = np.array(dstP)
    Q1 = np.array(srcQ)
    Q2 = np.array(dstQ)

    # 스텝마다 제어선을 다르게 하기 위해 중간 프레임에 대한 제어선 계산
    # 보간된 제어선을 저장할 interpolated lines 배열 생성
    P = np.array(srcP) + dP
    Q = np.array(srcQ) + dQ

    # Beier-Neely's multiple-line morphing algorithm
    # 각 픽셀 마다 반복
    for h_index in range(0, height):
        for w_index in range(0, width):
            # print(iFrame+1, h_index, w_index) # 현재 작업 중인 위치 출력
            # 픽셀 좌표, 누적 변위, 총 가중치 초기화
            pixel = np.array([w_index, h_index])
            DSUM1 = np.array([0.0, 0.0])
            totalweight = 0

            # 제어선 수 만큼 반복
            for i in range(int(np.array(srcP).size / 2)):
                norm_QP = np.linalg.norm(Q[i] - P[i])

                # 수직 교차점 u와 제어선으로부터의 변위 h 계산
                U = ((pixel - P[i]).dot(Q[i] - P[i])) / (norm_QP * norm_QP)
                H = ((pixel - P[i]).dot(perpendicular(Q[i] - P[i]))) / norm_QP

                xPrime1 = P1[i] + U * (Q1[i]-P1[i]) + (H * perpendicular(Q1[i] - P1[i])) / np.linalg.norm(Q1[i] - P1[i])
                xPrime2 = P2[i] + U * (Q2[i]-P2[i]) + (H * perpendicular(Q2[i] - P2[i])) / np.linalg.norm(Q2[i] - P2[i])

                if(U>1):
                    shortestDist = np.linalg.norm(Q[i] - pixel)
                elif(U<0):
                    shortestDist = np.linalg.norm(P[i] - pixel)
                else:
                    if(H>0):
                        shortestDist = H
                    else:
                        shortestDist = H * -1

                lineWeight = ((norm_QP ** p) / (a + shortestDist)) ** b

                DSUM1 = DSUM1 + (xPrime1 - pixel) * lineWeight
                totalweight += lineWeight

            xPrime1 = pixel + DSUM1 / totalweight

            srcX = int(xPrime1[0])
            srcY = int(xPrime1[1])

            if (srcX in range(0, width) and srcY in range(0, height)):
                srcRGB = img1[srcY][srcX]
            else:
                srcRGB = img1[h_index][w_index]

            # if (destX in range(0, width) and destY in range(0, height)):
            #     destRGB = outputs[destY][destX]
            # else:
            #     destRGB = outputs[h_index][w_index]

            R = srcRGB[0]
            G = srcRGB[1]
            B = srcRGB[2]

            outputs[h_index][w_index] = [int(R), int(G), int(B)]

    outputs = np.uint8(outputs)
    # cv2.imwrite('First drawing' + '.jpg', outputs)


def mouse_Input(img1, dst):
    global is_First

    is_First = True
    MsgBox1()
    cv2.imshow('example', example)
    drawing1 = mouseBrush(img1)

    is_First = False
    MsgBox2()
    cv2.imshow('First drawing', drawing1)
    drawing2 = mouseBrush(dst)

    MsgBox3()
    cv2.destroyAllWindows()

drawing = False
is_First = True
ix, iy = -1, -1
RGB = [255, 0, 0]
RGB_index = 0

srcP = list()
srcQ = list()
dstP = list()
dstQ = list()

a = 0.01
b = 1
p = 0.5

example = cv2.imread("images/example1.png")
img1 = cv2.imread("images/P1.jpg")

height, width, channels = img1.shape
outputs = np.zeros(img1.shape, np.float32)

mouse_Input(img1, outputs)

if not(len(srcP) == len(srcQ) == len(dstP) == len(dstQ)):
    MsgBox_Fail1()
    sys.exit(-2)

warphing(img1, outputs)
MsgBox_Success()

plt.imshow(np.uint8(outputs))
plt.xticks([]), plt.yticks([])
plt.title("Figure1")

plt.show()

