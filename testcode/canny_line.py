import cv2
import numpy as np
import time

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
            print('There is no video stream !!')
            break

        st = time.perf_counter()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(img,(5,5),0)
        edges = cv2.Canny(blur,100,200)

##        lines = cv2.HoughLines(edges[int(height/2):, int(width/4):int(3*width/4)],1,np.pi/180,200)
##        print(lines)
##        for line in lines:
##            rho,theta = line[0]
##            a = np.cos(theta)
##            b = np.sin(theta)
##            x0 = a*rho
##            y0 = b*rho
##            x1 = int(x0 + 1000*(-b))
##            y1 = int(y0 + 1000*(a))
##            x2 = int(x0 - 1000*(-b))
##            y2 = int(y0 - 1000*(a))
##            cv2.line(edges,(x1,y1), (x2,y2), (0, 255, 0), 2)
        
        
        end = time.perf_counter()
        
        cv2.putText(edges, "time: "+str(end-st), (100,20), \
                 cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,255,255),2,cv2.LINE_AA)
        cv2.imshow("frame", edges)
        if cv2.waitKey(33) == 27:
            break

cv2.destroyAllWindows()
