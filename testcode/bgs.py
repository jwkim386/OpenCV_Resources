from __future__ import print_function
import cv2

backSub = cv2.createBackgroundSubtractorMOG2()

capture = cv2.VideoCapture('vtest.avi')

if not capture.isOpened():
    print('Unable to open: video source')
    exit(0)

while True:
    ret, frame = capture.read()
    frame = cv2.resize(frame, (640,360))
    
    if frame is None:
        break

    fgMask = backSub.apply(frame)
    cv2.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv2.putText(frame, str(capture.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgMask)
    
    keyboard = cv2.waitKey(1)

    if keyboard == 'q' or keyboard == 27:
        break

capture.release()
cv2.destroyAllWindows()
