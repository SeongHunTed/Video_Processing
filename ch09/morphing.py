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
    tkinter.messagebox.showinfo('모핑 수행 도우미', '이미지 모핑을 성공적으로 수행하기 위해\n첫 번째 이미지와 같은 순서로 그려주세요.\n\n선을 다 그렸으면 ESC 키를 눌러주세요.')

def MsgBox2():
    tkinter.messagebox.showinfo('모핑 수행 도우미', '두 번째 이미지에서 선을 그릴 때\n두 번째 이미지와 같은 순서로 그려주세요.\n\n선을 다 그렸으면 ESC 키를 눌러주세요.')

def MsgBox3():
    tkinter.messagebox.showinfo('모핑 수행 도우미', '제어선 그리기 완료!\n순서가 안맞거나 잘 못 그리셨다면 프로그램을 재시작해주세요\n\n확인 버튼을 누르면 모핑울 시작합니다..')

def MsgBox_Fail1():
    tkinter.messagebox.showinfo('모핑 수행 도우미', '모핑 실패\n제어선의 수가 일치하지 않습니다.\n다시 시도해주세요.')

def MsgBox_Fail2():
    tkinter.messagebox.showinfo('모핑 수행 도우미', '모핑 실패\n제어선이 잘 못 그려진 것 같습니다.\n다시 시도해주세요.')

def MsgBox_Success():
    tkinter.messagebox.showinfo('모핑 수행 도우미', '모핑 dhksfy!\n결과를 확인해주세요')


def doResizing(theImage1, theImage2):

    size1 = theImage1.shape
    size2 = theImage2.shape
    avg0 = (size1[0] + size2[0])//2
    avg1 = (size1[0] + size2[1])//2

    if size1[0] == size2[0] and size1[1] == size2[1]:
        return [theImage1, theImage2]

    else:
        img1 = cv2.resize(theImage1, (avg1, avg0), interpolation=cv2.INTER_AREA)
        img2 = cv2.resize(theImage2, (avg1, avg0), interpolation=cv2.INTER_AREA)
        return [img1, img2]

def perpendicular(a):
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b


def doMorphing(img1, img2, nFrame, outputs):

    height, width, channels = img1.shape

    #DeltaP and DeltaQ 계산부
    dP = (np.array(dstP) - np.array(srcP)) / (nFrame + 1)
    dQ = (np.array(dstQ) - np.array(srcQ)) / (nFrame + 1)

    # 제어선 좌표 미리 저장
    P1 = np.array(srcP)
    P2 = np.array(dstP)
    Q1 = np.array(srcQ)
    Q2 = np.array(dstQ)

    for iFrame in range(0, nFrame):

        # 결과 저장될 이미지 공간 생성
        morphedIm = np.zeros(img1.shape, np.float32)

        # 스텝마다 제어선을 다르게 하기 위해 중간 프레임에 대한 제어선 계산
        # 보간된 제어선을 저장할 interpolated lines 배열 생성

        P = np.array(srcP) + dP * (iFrame + 1)
        Q = np.array(srcQ) + dQ * (iFrame + 1)

        # Croos-disolve weight, 프레임 넘버에 따라 img1 과 img2의 컬러 블렌딩 가중치 사전 계산

        wI2 = float(2 * (iFrame + 1) * (1 / (nFrame + 1)))
        wI1 = float(2 - wI2)

        # Beier-Neely's multiple-line morphing algorithm
        # 각 픽셀 마다 반복
        for h_index in range(0, height):
            for w_index in range(0, width):
                # print(iFrame+1, h_index, w_index) # 현재 작업 중인 위치 출력
                # 픽셀 좌표, 누적 변위, 총 가중치 초기화
                pixel = np.array([w_index, h_index])
                DSUM1 = np.array([0.0, 0.0])
                DSUM2 = np.array([0.0, 0.0])
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
                    DSUM2 = DSUM2 + (xPrime2 - pixel) * lineWeight
                    totalweight += lineWeight

                xPrime1 = pixel + DSUM1 / totalweight
                xPrime2 = pixel + DSUM2 / totalweight

                srcX = int(xPrime1[0])
                srcY = int(xPrime1[1])
                destX = int(xPrime2[0])
                destY = int(xPrime2[1])

                if(srcX in range(0, width) and srcY in range(0, height)):
                    srcRGB = img1[srcY][srcX]
                else:
                    srcRGB = img1[h_index][w_index]

                if(destX in range(0, width) and destY in range(0, height)):
                    destRGB = img2[destY][destX]
                else:
                    destRGB = img2[h_index][w_index]

                R = (wI1 * srcRGB[0] + wI2 * destRGB[0]) / 2
                G = (wI1 * srcRGB[1] + wI2 * destRGB[1]) / 2
                B = (wI1 * srcRGB[2] + wI2 * destRGB[2]) / 2

                morphedIm[h_index][w_index] = [int(R), int(G), int(B)]

        morphedIm = np.uint8(morphedIm)
        cv2.imwrite('Frame' + str(iFrame + 1) + '.jpg', morphedIm)
        outputs[iFrame] = cv2.cvtColor(morphedIm, cv2.COLOR_BGR2RGB)
        print('saved frame', iFrame + 1)


def mouse_Input(img1, img2):
    global is_First

    is_First = True
    MsgBox1()
    cv2.imshow('example', example)
    drawing1 = mouseBrush(img1)

    is_First = False
    MsgBox2()
    cv2.imshow('First drawing', drawing1)
    color_reset()
    drawing2 = mouseBrush(img2)

    cv2.imshow("First drawing", drawing1)
    cv2.imshow("Second drawing", drawing2)
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

example = cv2.imread("images/example.png")
original1 = cv2.imread("images/P1.jpg")
original2 = cv2.imread("images/P2.jpg")
nFrame = 4

[img1, img2] = doResizing(original1, original2)

height, width, channels = img1.shape
outputs = np.zeros((nFrame, height, width, channels), np.float32)

mouse_Input(img1, img2)

if not(len(srcP) == len(srcQ) == len(dstP) == len(dstQ)):
    MsgBox_Fail1()
    sys.exit(-2)

doMorphing(img1, img2, nFrame, outputs)
MsgBox_Success()

for i in range(nFrame):
    plt.subplots(1, 4, i + 1), plt.imshow(np.uint8(outputs[i]))
    plt.title('Step : ' + str(i+1)), plt.xticks([]), plt.yticks([])

plt.show()


