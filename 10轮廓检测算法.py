import cv2

def cv_show(image, path):
	cv2.imshow(image, path)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

'''轮廓提取'''

# img = cv2.imread("imageSource/contour.png")
# gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
# ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#
#
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# draw_img = img.copy()
# res = cv2.drawContours(draw_img, contours, -1, (0, 0, 255), 2)
# cv_show("img", res)
#
# # 面积
# cnt = contours[0]
# print(cv2.contourArea(cnt))
#
# # 周长
# print(cv2.arcLength(cnt, True))

'''轮廓近似'''
img = cv2.imread("imageSource/contour.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cnt = contours[0]
draw_img = img.copy()
res = cv2.drawContours(draw_img, cnt, -1, (0, 0, 255), 2)
cv_show("res", res)
epsilon = 0.01*cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)

draw_img = img.copy()
res = cv2.drawContours(draw_img, [approx], -1, (0, 0, 255), 2)
cv_show("res", res)