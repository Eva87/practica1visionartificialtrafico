#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín

#pip install opencv-contrib-python

import cv2
from matplotlib import pyplot as plt
import numpy as np
from random import random
from colorsys import hsv_to_rgb

#esto aclara la imagen
#m_power_law_transformation = cv2.pow (im, 0.6)
img=cv2.imread("./test/00482.jpg", 0)
#inicializamos la imagen RGB a niveles de gris
img2 = cv2.imread("./test/00482.jpg", cv2.IMREAD_GRAYSCALE)
'''
imagencolor = cv2.imread("./train_recortadas/01/00411.jpg")
imagenbyn = cv2.imread("./train_recortadas/01/00411.jpg", cv2.IMREAD_GRAYSCALE)

'''
imagencolor = cv2.imread("./test/00482.jpg", cv2.IMREAD_COLOR)
imagenbyn = cv2.imread("./test/00482.jpg", cv2.IMREAD_GRAYSCALE)
'''
imagencolor = cv2.imread("./test/00400.jpg", cv2.IMREAD_COLOR)
#inicializamos la imagen RGB a niveles de gris
imagenbyn = cv2.imread("./test/00400.jpg", cv2.IMREAD_GRAYSCALE)
'''
'''
imagensincambios = cv2.imread("./test/00400.jpg", cv2.IMREAD_UNCHANGED)
imgsinparametros = cv2.imread("./test/00400.jpg")

'''
#inicializamos la imagen sin cambios incluyendo el canal alfa

imagensincambios = cv2.imread("./test/00482.jpg", cv2.IMREAD_UNCHANGED)
imgsinparametros = cv2.imread("./test/00482.jpg")

'''
imagensincambios = cv2.imread("./20201003121440748.png", cv2.IMREAD_UNCHANGED)
imgsinparametros = cv2.imread("./20201003121440748.png")'''
'''
imagensincambios = cv2.imread("./Captura.png", cv2.IMREAD_UNCHANGED)
imgsinparametros = cv2.imread("./Captura.png")'''







a=0
image2 = np.uint8(255.0 * (img - img.min()) / (img.max() - img.min()))
print('nivel de brillo máximo = ', img.max())
print('nivel de brillo mìnimo = ', img.min())
# umbralización
# imagen oscura 20 y imagen clara 100
#if img.max()
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
keypoints=mser.detect(gray,None)
for keypoint in keypoints:
    radius = int(0.5 * keypoint.size)
    x, y = np.int64(keypoint.pt)
    cv2.circle(imagencolor, (x, y), radius, (0, 255, 255), 2)




#cv2.imshow("foto", image2,  vmin=0, vmax=255)
'''cv2.imshow("y=0.2992+0.587G+0.114B", y)
cv2.imshow("u=B-Y", u)
cv2.imshow("v=R-Y", v)

cv2.imshow("b", b)
cv2.imshow("r", r)
cv2.imshow("g", g)
'''


cv2.imshow("imu", imu)
cv2.imshow("output", output)
cv2.imshow('Imágenes', np.hstack([imgsinparametros, imagencolor]))
cv2.waitKey(0)