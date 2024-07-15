import cv2
width = 720
height = 480
fps = 30
fname = "highway2.mp4"
gst_str = f"filesrc location={fname} ! qtdemux ! queue\
	! h264parse ! omxh264dec ! nvvidconv\
	! video/x-raw,format=BGRx,width={width},height={height}\
	! videorate ! video/x-raw,framerate={fps}/1 ! queue \
	! videoconvert ! queue ! video/x-raw, format=BGR ! appsink"
cap = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)
while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("frame", frame)
        if cv2.waitKey(33) == 27:
            break

cv2.destroyAllWindows()
