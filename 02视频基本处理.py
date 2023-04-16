import cv2
vc = cv2.VideoCapture("VideoSource/test1.mp4")
# if vc.isOpened():
# 	open, frame = vc.read()
# else:
# 	open = False
while open:
	ret, frame = vc.read()
	if frame is None:
		break
	if ret == True:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
		cv2.imshow('result', gray)
		if cv2.waitKey(33) & 0xFF == 27:    # waitKey(N)对应等待时间，如本视频为30帧，为还原应该是waitKsy(33)
			break
vc.release()
cv2.destroyAllWindows()