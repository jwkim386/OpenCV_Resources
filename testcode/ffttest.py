import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

img = cv2.imread('messi5.jpg',0)
rows,cols = img.shape

st = time.perf_counter()
f = np.fft.fft2(img)
end = time.perf_counter()

fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

st1 = time.perf_counter()
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
end1 = time.perf_counter()
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

print('Original: np.fft: ', end-st, 'cv2.dft: ', end1-st1)

plt.subplot(223),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

nrows = cv2.getOptimalDFTSize(rows)
ncols = cv2.getOptimalDFTSize(cols)

right = ncols - cols
bottom = nrows - rows
bordertype = cv2.BORDER_CONSTANT #just to avoid line breakup in PDF file
nimg = cv2.copyMakeBorder(img,0,bottom,0,right,bordertype, value = 0)

st2 = time.perf_counter()
f = np.fft.fft2(nimg)
end2 = time.perf_counter()

st3 = time.perf_counter()
dft = cv2.dft(np.float32(nimg),flags = cv2.DFT_COMPLEX_OUTPUT)
end3 = time.perf_counter()

print('Padding: np.fft: ', end2-st2, 'cv2.dft: ', end3-st3)

plt.show()

