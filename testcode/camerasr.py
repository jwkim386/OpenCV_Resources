import cv2
from cv2 import dnn_superres

width = 800
height = 448
fps = 30
device = "/dev/video0"
gst_str = f"v4l2src device={device} io-mode=2 \
	! image/jpeg, width=(int)320, height=(int)240, framerate=30/1 \
	! nvv4l2decoder mjpeg=1 ! nvvidconv ! video/x-raw,format=BGRx \
	! videoconvert ! video/x-raw, format=BGR ! appsink"

cap = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

# Create an SR object - only function that differs from c++ code
sr = dnn_superres.DnnSuperResImpl_create()

# Read the desired model
path = "LapSRN_x2.pb"
sr.readModel(path)
sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

# Set the desired model and scale to get correct pre- and post-processing
sr.setModel("lapsrn", 2)
                       
while True:
        ret, frame = cap.read()
        if not ret:
            break
        #upsample image
        frame1 = sr.upsample(frame)
        cv2.imshow("frame", frame1)
        if cv2.waitKey(33) == 27:
            break

cv2.destroyAllWindows()

