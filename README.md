# OpenCV-learning

## 介绍

​	学习OpenCV的一些文件与代码

## 问题记录

#### 1. cv2.merge()

```python
b, g, r = cv2.split(img)
# ! img2 = cv2.merge(b, g, r) 
# ! merge() takes at most 2 arguments (3 given)
img2 = cv2.merge([b, g, r])
```

#### 2. 使用plt输出图像变色问题

```python
def deallmg(img):
	b, g, r = cv2.split(img)
	img_rgb = cv2.merge([r, g, b])
	return img_rgb
```

#### 3. 图像尺寸转换

```py
# 将 img_dog 尺寸转化与 img_tiger 一致
# print(img_tiger.shape)  # (591, 725, 3)
img_dog = cv2.resize(img_dog, (725, 591))   # 像素变换 （！！！顺序！！！）
```

