import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("imageSource/lena.png", 0)
img_float32 = np.float32(img)

dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
# plt.subplot(121), plt.imshow(img, cmap='gray')
# plt.title("Input Image"), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
# plt.title("Magnitude Spectrum"), plt.xticks([]), plt.yticks([])
# plt.show()

rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)

'''低通滤波'''
# mask = np.zeros((rows, cols, 2), np.uint8)
# mask[crow-30: crow+30, ccol-30: ccol+30] = 1

'''高通滤波'''
mask = np.ones((rows, cols, 2), np.uint8)
mask[crow-30: crow+30, ccol-30: ccol+30] = 0

# IDFT 傅里叶逆变换
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title("Input Image"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap='gray')
plt.title("Result"), plt.xticks([]), plt.yticks([])
plt.show()