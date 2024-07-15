import numpy as np
import cv2
import time

#cap = cv2.VideoCapture('filesrc location=/home/adas/Documents/test_data/highway3_4lane1.mp4 ! qtdemux ! queue ! h264parse ! omxh264dec ! nvvidconv ! video/x-raw,format=BGRx,width=800,height=450 ! queue ! videoconvert ! queue ! video/x-raw, format=BGR ! appsink', cv2.CAP_GSTREAMER)

#cap = cv2.VideoCapture('v4l2src device=/dev/video0 ! nvvidconv ! video/x-raw, format=YUY2, width=800,height=448 ! videoconvert ! appsink', cv2.CAP_GSTREAMER) #s/w codec

cap = cv2.VideoCapture ('v4l2src device=/dev/video0 io-mode=2 ! image/jpeg, width=(int)800, height=(int)448, framerate=30/1 ! nvv4l2decoder mjpeg=1 ! nvvidconv ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink', cv2.CAP_GSTREAMER) #h/w NVJPG codec

#cap = cv2.VideoCapture('v4l2src device=/dev/video0 io-mode=2 ! queue ! image/jpeg,framerate=30/1,width=1280,height=720 ! jpegparse ! nvjpegdec ! video/x-raw ! videoconvert ! queue ! video/x-raw,width=1280,height=720,format=BGRx,framerate=30/1 ! ximagesink', cv2.CAP_GSTREAMER) #not work

# usb cam fps test on terminal
# gst-launch-1.0 v4l2src device=/dev/video0 io-mode=2 ! image/jpeg,width=1920,height=1080,framerate=30/1,format=MJPG ! jpegdec ! videoconvert ! video/x-raw,format=BGR ! fpsdisplaysink text-overlay=0 video-sink=fakesink sync=0 -v

#if not cap.isOpened():
#    print("Cannot open camera")
#    exit()

#s/w codec
#cap = cv2.VideoCapture(0)
#codec = 0x47504A4D # MJPG
#cap.set(cv2.CAP_PROP_FPS, 30.0)
#cap.set(cv2.CAP_PROP_FOURCC, codec)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m','j','p','g'))
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 448)

n = 1

while cap.isOpened():
    # Capture frame-by-frame
    st = time.perf_counter()
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    print(n, ' = ', time.perf_counter() - st)
#    time.sleep(0.03)
    n = n+1
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
