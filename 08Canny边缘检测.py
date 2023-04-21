'''
1) 使用高斯滤波器，平滑图像，去除噪声
2）计算图像中像素点的梯度强度和方向
3）应用非极大值（NMS）抑制，以消除把边缘检测带来的杂散效应
4）应用双阈值（DT）检测来确定真实的和潜在的边缘
5）通过抑制孤立的弱边缘最终完成边缘检测
'''
import cv2
import numpy as np

def cv_show(image, path):
	cv2.imshow(image, path)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


# img = cv2.imread("imageSource/lena.png", cv2.IMREAD_GRAYSCALE)
# # (minvalue, maxvalue)
# v1 = cv2.Canny(img, 80, 150)
# v2 = cv2.Canny(img, 100, 100)
# res = np.hstack((img, v1, v2))
# cv_show("res", res)

img = cv2.imread("imageSource/1.jpg", cv2.IMREAD_GRAYSCALE)
v1 = cv2.Canny(img, 120, 200)
v2 = cv2.Canny(img, 50, 100)
res = np.hstack((img, v1, v2))
cv_show("res", res)













