import cv2
from random import random
from colorsys  import hsv_to_rgb
import numpy as np

img = cv2.imread('test/00449.jpg')
img_to_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
img_to_yuv[:, :, 0] = cv2.equalizeHist(img_to_yuv[:, :, 0])
hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
cv2.imshow("Equalizada",hist_equalization_result)
equGris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gris",equGris)


# MSER
output = np.zeros((equGris.shape[0], equGris.shape[1], 3), dtype=np.uint8)
mser = cv2.MSER_create(_delta=5, _max_variation=0.50, _max_area=2000,_min_area=200)
polygons = mser.detectRegions(equGris)
for polygon in polygons[0]:
    colorRGB = hsv_to_rgb(random(), 1, 1)
    colorRGB = tuple(int(color * 255) for color in colorRGB)
    output = cv2.fillPoly(output, [polygon], colorRGB)
cv2.imshow("salidaMSER",output)
cv2.waitKey(0)

#Falta el boundingRect, hacer que las imagenes se pongan rectas , agrandar region rectangulo
