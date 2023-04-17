import cv2
import numpy as np
import matplotlib.pyplot as plt
def cv_show(image, path):
	cv2.imshow(image, path)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

# 转换cv图像格式
def deallmg(img):
	b, g, r = cv2.split(img)
	img_rgb = cv2.merge([r, g, b])
	return img_rgb

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

# '''彩色通道提取'''
# img = cv2.imread("imageSource/tiger.png")
# b, g, r = cv2.split(img)
# img2 = cv2.merge([b, g, r])
# print(img2)
# # 只保留R
# cur_img = img.copy()
# cur_img[:, :, 0] = 0
# cur_img[:, :, 1] = 0
# cv_show("R", cur_img)
# # 只保留G
# cur_img = img.copy()
# cur_img[:, :, 2] = 0
# cur_img[:, :, 0] = 0
# cv_show("G", cur_img)
# # 只保留B
# cur_img = img.copy()
# cur_img[:, :, 2] = 0
# cur_img[:, :, 1] = 0
# cv_show("B", cur_img)

'''边界填充'''
# img = cv2.imread("imageSource/tiger.png")
# top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)
# replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_WRAP)
# constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_CONSTANT, value=0)
# plt.subplot(231), plt.imshow(deallmg(img), 'gray'), plt.title('ORIGINAL')
# plt.subplot(232), plt.imshow(deallmg(replicate), 'gray'), plt.title('REPLICATE')    # 边界复制
# plt.subplot(233), plt.imshow(deallmg(reflect), 'gray'), plt.title('REFLECT')      # 边界反射 abc|cba
# plt.subplot(234),plt.imshow(deallmg(reflect101), 'gray'), plt.title('REFLECT_101')  # 边界为轴反射 abc|ba
# plt.subplot(235), plt.imshow(deallmg(wrap), 'gray'), plt.title('WRAP')   # 包装法 abc| ghabc | gh
# plt.subplot(236), plt.imshow(deallmg(constant), 'gray'), plt.title('CONSTANT')   # 常量法
# plt.show()

'''基本运算'''
# img = cv2.imread("imageSource/tiger.png")
# print(img[:5, :5, 0])
# img2 = img + 30
# print(img2[:5, :5, 0])
#
# print((img+img2)[:5, :5, 0])    # 会自行%256
#
# print(cv2.add(img, img2)[:5, :5, 0])    # 越界置255

'''图像融合'''
img_dog = cv2.imread("imageSource/dog.png")
img_tiger = cv2.imread("imageSource/tiger.png")
# print(img_tiger.shape)  # (591, 725, 3)

img_dog = cv2.resize(img_dog, (725, 591))   # 像素变换
# img_dog = cv2.resize(img_dog, (0, 0), fx=3, fy=3)   # 比例变换
res = cv2.addWeighted(img_tiger, 0.4, img_dog, 0.6, 0)
plt.imshow(deallmg(res))
plt.show()











