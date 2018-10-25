import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./test_image.jpg")

## gray filter
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## blur filter
img_blur = cv2.GaussianBlur(img_gray,(5, 5), 0 )

x_num = 3
y_num = 1

fig = plt.figure()
plt.subplot(x_num, y_num, 1)
plt.title("defualt image")
plt.imshow(img)

plt.subplot(x_num, y_num, 2)
plt.title("gray fitler")
plt.imshow(img_gray)

plt.subplot(x_num, y_num, 3)
plt.title("gray fitler")
plt.imshow(img_blur)
plt.show()