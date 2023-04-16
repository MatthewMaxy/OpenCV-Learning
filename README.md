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

