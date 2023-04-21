import cv2
import numpy as np


def cv_show(image, path):
	cv2.imshow(image, path)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


img = cv2.imread("imageSource/seu.png",)
# cv_show("img", img)
kernel = np.ones((3, 3), np.uint8)

'''腐蚀操作'''

# erosion = cv2.erode(img, kernel, iterations=1)
# cv_show("erosion", erosion)

'''膨胀操作'''
# dilate = cv2.dilate(erosion, kernel, iterations=1)
# res = np.hstack((img, erosion, dilate))
# cv_show("vs", res)

'''开运算：先腐蚀再膨胀'''
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

'''闭运算：先膨胀再腐蚀'''
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# src = np.hstack((img, opening, closing))
# cv_show("vs", src)

'''梯度 = 膨胀 - 腐蚀'''
# gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# cv_show("gradient", gradient)

'''礼帽 = 原始输入 - 开运算结果'''
# tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# cv_show("tophat", tophat)

'''黑帽 = 闭运算 - 原始输入'''
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv_show("blackhat", blackhat)
