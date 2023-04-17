import cv2
import numpy as np
import matplotlib.pyplot as plt

def deallmg(img):
	b, g, r = cv2.split(img)
	img_rgb = cv2.merge([r, g, b])
	return img_rgb

# ret, dst = cv2.threshold(src, thresh, maxval, type)
# src 单通道图（一般灰度）


img = deallmg(cv2.imread("imageSource/tiger.png"))
img_gray = cv2.imread("imageSource/tiger.png", cv2.IMREAD_GRAYSCALE)
ret, thresh1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)     # 0/255
ret, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)     # <=127
ret, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)     # 0/>=127
ret, thresh5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
	plt.subplot(2, 3, i+1), plt.imshow((images[i]), 'gray')
	plt.title(titles[i])
	plt.xticks([]), plt.yticks([])
plt.show()