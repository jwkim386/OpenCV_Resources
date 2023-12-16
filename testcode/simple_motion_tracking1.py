import cv2
import numpy as np

thresh = 25
max_diff = 5
a, b = None, None

#cap = cv2.VideoCapture(-1)
cap = cv2.VideoCapture ('v4l2src device=/dev/video0 io-mode=2 ! image/jpeg, width=(int)800, height=(int)448, framerate=30/1 ! nvv4l2decoder mjpeg=1 ! nvvidconv ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink', cv2.CAP_GSTREAMER) #h/w NVJPG codec
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

if cap.isOpened():
    ret, a = cap.read()

    while ret:
        ret, b = cap.read()
        
        if not ret:
            break
        
        a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
        b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        diff1 = cv2.absdiff(a_gray, b_gray)
        ret, diff_t = cv2.threshold(diff1, thresh, 255, cv2.THRESH_BINARY)
        k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        diff = cv2.morphologyEx(diff_t, cv2.MORPH_OPEN, k)
        diff_cnt = cv2.countNonZero(diff)
        
        if diff_cnt > max_diff:
            nzero = np.nonzero(diff)
            cv2.rectangle(b, (min(nzero[1]), min(nzero[0])), 
                          (max(nzero[1]), max(nzero[0])), (0, 255, 0), 2)
        '''
        rectangle: pt1, pt2 기준으로 사각형 프레임을 만들어줌.
        nzero: diff는 카메라 영상과 사이즈가 같으며, a, b프레임의 차이 어레이를 의미함.
        (min(nzero[1]), min(nzero[0]): diff에서 0이 아닌 값 중 행, 열이 가장 작은 포인트
        (max(nzero[1]), max(nzero[0]): diff에서 0이 아닌 값 중 행, 열이 가장 큰 포인트
        (0, 255, 0): 사각형을 그릴 색상 값
        2 : thickness
        '''

        cv2.putText(b, "Motion detected!!", (10, 30),
                        cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        cv2.imshow('motion', b)
        
        a = b
        
        if cv2.waitKey(1) & 0xFF == 27:
            break
