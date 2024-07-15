import cv2 as cv
import time

##vod = cv.VideoCapture('media/corn.mp4')
##ret, frame = vod.read()
frame = cv.imread('Howling-1254383.png')
# create a frame on GPU for images
gpu_frame = cv.cuda_GpuMat()
scale = 1

st = time.perf_counter()

# send 1st frame to GPU 
gpu_frame.upload(frame)

# resize image (numpy.ndarray, cv2.cuda_GpuMat)
resized = cv.cuda.resize(gpu_frame, (640,480))
# apply luv, hsv, and grayscale filters to resized image
luv = cv.cuda.cvtColor(resized, cv.COLOR_BGR2LUV)
hsv = cv.cuda.cvtColor(resized, cv.COLOR_BGR2HSV)
gray = cv.cuda.cvtColor(resized, cv.COLOR_BGR2GRAY)
resized = resized.download()
luv = luv.download()
hsv = hsv.download()
gray = gray.download()

end = time.perf_counter()


print('gpu time: ', end-st)

st1 = time.perf_counter()
# resize image (numpy.ndarray, cv2.cuda_GpuMat)
resized = cv.resize(gpu_frame, (640,480))
# apply luv, hsv, and grayscale filters to resized image
luv = cv.cvtColor(resized, cv.COLOR_BGR2LUV)
hsv = cv.cvtColor(resized, cv.COLOR_BGR2HSV)
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

end1 = time.perf_counter()

print('cpu time: ', end1-st1)
