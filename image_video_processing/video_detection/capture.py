import cv2
import time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

frames = 0
start = time.time()
while True:  # while-loop turns the frames into a video
    check, frame = video.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames += 1

    cv2.imshow("vid", frame)  # gray_img if i want the frame to be gray
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

sec = time.time() - start
print(f"Frames:{frames} in {sec}s => {frames / sec}fps")
video.release()
cv2.destroyAllWindows
