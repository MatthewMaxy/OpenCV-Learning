import cv2
import matplotlib.pyplot as plt
import numpy as np

def cv_show(image, path):
	cv2.imshow(image, path)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

'''gray图'''
# img = cv2.imread("imageSource/dog.png", 0)
# hist = cv2.calcHist([img], [0], None, [256], [0,256])
# # print(hist.shape)
# plt.hist(img.ravel(), 256)
# plt.show()

'''RGB图'''
# img = cv2.imread("imageSource/dog.png")
# color = ('b', 'g', 'r')
# for i, col in enumerate(color):
# 	hist = cv2.calcHist([img], [i], None, [256], [0, 256])
# # print(hist.shape)
# 	plt.plot(hist, color=col)
# 	plt.xlim([0, 256])
# plt.show()

'''蒙版'''
# img = cv2.imread("imageSource/dog.png", 0)
# mask = np.zeros(img.shape[:2], np.uint8)
# # print(mask.shape)
# mask[100:550, 100:800] = 255
# masked_img = cv2.bitwise_and(img, img, mask=mask)
# # cv_show('masked_img', masked_img)
# hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
# hist_mask = cv2.calcHist([masked_img], [0], mask, [256], [0, 256])
#
# plt.subplot(221), plt.imshow(img, 'gray')
# plt.subplot(222), plt.imshow(mask, 'gray')
# plt.subplot(223), plt.imshow(masked_img, 'gray')
# plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
# plt.xlim([0, 256])
# plt.show()

'''直方图均衡化'''
img = cv2.imread("imageSource/lena.png", 0)
# plt.hist(img.ravel(), 256)
# plt.show()
equ = cv2.equalizeHist(img)
# plt.hist(equ.ravel(), 256)
# plt.show()
# res = np.hstack((img, equ))
# cv_show("res", res)

'''自适应均衡化'''
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
res_clahe = clahe.apply(img)
res = np.hstack((img, equ, res_clahe))
cv_show("res", res)

'''彩色图均衡化'''
def equalize_clahe_color(img):
	cla = cv2.createCLAHE(clipLimit=2.0)
	channels = cv2.split(img)
	eq_channels = []
	for ch in channels:
		eq_channels.append(cla.apply(ch))
	eq_image = cv2.merge(eq_channels)
	return eq_image

image = cv2.imread("imageSource/lena.png")
image_clahe_color = equalize_clahe_color(image)
res = np.hstack((image, image_clahe_color))
cv_show("lena", res)