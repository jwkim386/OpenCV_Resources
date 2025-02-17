import cv2
import numpy as np

# YOLO Load
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# for using GPU
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# get image
video = cv2.VideoCapture('highway_traffic.mp4')

count = 0
while video.isOpened():
    ret, img = video.read()
    if not ret:
        break
    if int(video.get(1)) % 7 == 0:
        img = cv2.resize(img, None, fx=0.8, fy=0.8)
        height, width, channels = img.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True,
					 crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # display information
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # coordinates
                    x = int(center_x-w/2)
                    y = int(center_y-h/2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN

        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[i]
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
                cv2.putText(img, label, (x, y+30), font, 2, color, 2)

        cv2.imshow('object_detection', img)

        key = cv2.waitKey(1)
        if key == 32:  # Space for pause
            key = cv2.waitKey(0)
        if key == 27:  # ESC
            break

cv2.destroyAllWindows()
