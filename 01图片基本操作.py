import cv2
import numpy as np

def cv_show(image, path):
	cv2.imshow(image, path)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

# img = cv2.imread("imageSource/tiger.png")
# cv2.imshow('image', img)
# # 等待时间
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(img.shape)

# img = cv2.imread("imageSource/tiger.png", cv2.IMREAD_GRAYSCALE)
# # cv2.imshow('image', img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# cv2.imwrite('imageSource/greytiger.png',img)
# print(img.size)

'''截取部分图像'''
# img = cv2.imread("imageSource/tiger.png")
# tiger = img[0:200, 0:200]
# cv_show('tiger', tiger)

'''彩色通道提取'''
img = cv2.imread("imageSource/tiger.png")
b, g, r = cv2.split(img)
img2 = cv2.merge([b, g, r])
print(img2)
# 只保留R
cur_img = img.copy()
cur_img[:, :, 0] = 0
cur_img[:, :, 1] = 0
cv_show("R", cur_img)
# 只保留G
cur_img = img.copy()
cur_img[:, :, 2] = 0
cur_img[:, :, 0] = 0
cv_show("G", cur_img)
# 只保留B
cur_img = img.copy()
cur_img[:, :, 2] = 0
cur_img[:, :, 1] = 0
cv_show("B", cur_img)
