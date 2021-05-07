import cv2
import numpy as np

np.set_printoptions(suppress=True)
img = cv2.imread("./test/00575.jpg")
img = cv2.imread("./test/00411.jpg")
img = cv2.imread("./test/00420.jpg")
img = cv2.imread("./test/00403.jpg")
img = cv2.imread("./test/00482.jpg")

#img=cv2.resize(img,100,None,None,15,15)
scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (25, 25)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

cv2.imshow("img", resized)
cv2.waitKey(0)