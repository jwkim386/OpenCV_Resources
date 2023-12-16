import numpy as np
import cv2

cap = cv2.VideoCapture('Shopping.mp4')
if not cap.isOpened():
    print("Cannot open cam")
    exit()

ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame ")
        break

#    gray = cv2.cvtColor(frame, cv2. COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

print("width= ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("height = ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.release()
cv2.destroyAllWindows()
