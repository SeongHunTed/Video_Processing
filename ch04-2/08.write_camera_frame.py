import cv2

capture = cv2.VideoCapture(0)
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

fps = 29.97
delay = round(1000/fps)
size = (640, 480)

fourcc = cv2.VideoWriter_fourcc(*'DX50')

capture.set(cv2.CAP_PROP_FPS, fps)
capture.set(cv2.CAP_PROP_ZOOM, 1)
capture.set(cv2.CAP_PROP_FOCUS, 0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])

print("프레임 해상도: %s - %s" % (capture.get(cv2.CAP_PROP_FRAME_WIDTH), capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("압축코덱 숫자:", fourcc)
print("delay: %2d ms" % delay)
print("fps: %.2f" % fps)

writer = cv2.VideoWriter("images/write_video_file.avi", fourcc, fps, size)
if writer.isOpened() == False: raise Exception("동엿아 파일 개방 안됨")

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(delay) >= 0: break

    writer.write(frame)
    cv2.imshow("View Frame from Camera", frame)

writer.release()
capture.release()