import cv2

def cv_show(image, path):
	cv2.imshow(image, path)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


img = cv2.imread("imageSource/lena.png")

# 高斯金字塔
# up = cv2.pyrUp(img)
# down = cv2.pyrDown(img)
# down_up = cv2.pyrUp(down)
# cv_show("img", img)
# cv_show("up", up)
# cv_show("down", down)
# cv_show("down_up", down_up)

# 拉普拉斯金字塔
down = cv2.pyrDown(img)
up = cv2.pyrUp(down)
L_1 = img - up
cv_show("L-1", L_1)
