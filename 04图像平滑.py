import cv2
import numpy as np
def cv_show(image, path):
	cv2.imshow(image, path)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


img = cv2.imread("imageSource/lenaNoise.png")
cv_show('img', img)

'''均值滤波'''
# # 简单的平均卷积操作
# # 卷积核[[1,1,1],[1,1,1],[1,1,1]]
blur = cv2.blur(img, (3, 3))
# cv_show("blur", blur)

'''方框滤波'''
# # 基本和均值一样， 可以选择归一化
# # 若归一化和均值一样
# box = cv2.boxFilter(img, -1, (3, 3), normalize=True)
# cv_show("box", box)
#
# # 未归一化
# box2 = cv2.boxFilter(img, -1, (3, 3), normalize=False)
# cv_show("box2", box2)

'''高斯滤波'''
# # 高斯模糊的卷积核里的数值满足高斯分布
gaussian = cv2.GaussianBlur(img, (5, 5), 1)
# cv_show("gaussian", gaussian)

'''中值滤波'''
median = cv2.medianBlur(img, 5)
# cv_show("median", median)

'''展示所有的'''
# 拼接对比
res = np.hstack((blur, gaussian, median))
cv_show("median vs average", res)

