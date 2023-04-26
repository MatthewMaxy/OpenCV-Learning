import cv2
import matplotlib.pyplot as plt
import numpy as np

img_rgb = cv2.imread("imageSource/lena.png")
img = cv2.imread("imageSource/lena.png",0)
face = cv2.imread("imageSource/lenaface.png", 0)
w, h = face.shape[:]

'''匹配展示比较'''

# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# for meth in methods:
# 	img2 = img.copy()
# 	method = eval(meth)
# 	res = cv2.matchTemplate(img, face, method)
# 	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#
# 	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
# 		top_left = min_loc
# 	else:
# 		top_left = max_loc
# 	bottom_right = (top_left[0] + w, top_left[1] + h)
#
# 	cv2.rectangle(img2, top_left, bottom_right, 255, 2)
# 	plt.subplot(121), plt.imshow(res, cmap='gray')
# 	plt.xticks([]), plt.yticks([])
# 	plt.subplot(122), plt.imshow(img2, cmap='gray')
# 	plt.xticks([]), plt.yticks([])
# 	plt.suptitle(meth)
# 	plt.show()

'''阈值多匹配'''
res = cv2.matchTemplate(img, face, cv2.TM_CCORR_NORMED)
threshold = 0.91
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
	bottom_right = (pt[0] + w, pt[1] + h)
	cv2.rectangle(img_rgb, pt, bottom_right, (0, 0, 255), 2)

cv2.imshow('img_rgb', img_rgb)
cv2.waitKey()