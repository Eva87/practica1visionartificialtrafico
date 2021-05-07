import cv2
import numpy as np
from random import random
from colorsys import hsv_to_rgb
img=cv2.imread("./test/00482.jpg", 0)
#inicializamos la imagen RGB a niveles de gris
img2 = cv2.imread("./test/00482.jpg", cv2.IMREAD_GRAYSCALE)
imagencolor = cv2.imread("./test/00482.jpg", cv2.IMREAD_COLOR)

imu = ((img2 >100)*255).astype(np.uint8)
#MSER
output = np.zeros((imu.shape[0],imu.shape[1],3),dtype=np.uint8)
mser = cv2.MSER_create(_delta=5,_max_variation=0.5,_max_area=20000)
polygons = mser.detectRegions(imu)
for polygon in polygons[0]:
    colorRGB = hsv_to_rgb(random(),1,1)
    colorRGB = tuple(int(color*255) for color in colorRGB)
    output = cv2.fillPoly(output,[polygon],colorRGB)

gray = cv2.cvtColor(imagencolor, cv2.COLOR_BGR2GRAY)  # Convertimos la imagen a escala de grises.
cv2.imshow("imu", imu)
cv2.imshow("output", output)
cv2.waitKey(0)
