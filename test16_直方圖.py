#直方圖

import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('test6.jpg', 0)
# 别忘了中括号 [img],[0],None,[256],[0,256]，只有 mask 没有中括号
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])

img2 = cv2.imread('test6.jpg')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    #calcHist 建立累積直方圖，看每個顏色值累積的像素值是多少
    histr = cv2.calcHist([img2], [i], None, [256], [0, 256])
    plt.subplot(224), plt.plot(histr, color=col),
    #把RGB三個直方圖畫在同一個圖中
    plt.xlim([0, 256]), plt.title('Histogram')
    

plt.subplot(221), plt.imshow(img1, 'gray'), plt.title('Image1')
plt.subplot(222), plt.hist(img1.ravel(), 256, [0, 256]),
plt.title('Histogram'), plt.xlim([0, 256])
plt.subplot(223), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)), plt.title('Image2')
plt.show()