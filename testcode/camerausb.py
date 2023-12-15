import cv2
width = 800
height = 448
fps = 30
device = "/dev/video0"
gst_str = f"v4l2src device={device} io-mode=2 \
	! image/jpeg, width=(int)320, height=(int)240, framerate=30/1 \
	! nvv4l2decoder mjpeg=1 ! nvvidconv ! video/x-raw,format=BGRx \
	! videoconvert ! video/x-raw, format=BGR ! appsink"
cap = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)
while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("frame", cv2.resize(frame,(640,480), interpolation=cv2.INTER_CUBIC))
        if cv2.waitKey(33) == 27:
            break

cv2.destroyAllWindows()
