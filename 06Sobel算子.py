import cv2
def cv_show(image, path):
	cv2.imshow(image, path)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


# img = cv2.imread("imageSource/pie.png")
# sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# sobelx = cv2.convertScaleAbs(sobelx)
# cv_show("sobelx", sobelx)
#
# sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
# sobely = cv2.convertScaleAbs(sobely)
# cv_show("sobely", sobely)
#
# sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
# cv_show("sovelxy", sobelxy)
#
# sobelxy2 = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)
# cv_show("sovelxy2", sobelxy2)

'''lena_test'''
img = cv2.imread("imageSource/lena.png")
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)

sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv_show("sovelxy", sobelxy)

sobelxy2 = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)
sobelxy2 = cv2.convertScaleAbs(sobelxy2)
cv_show("sovelxy2", sobelxy2)
