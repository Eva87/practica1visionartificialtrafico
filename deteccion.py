#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín

import cv2
import sklearn
from matplotlib import pyplot as plt
import numpy as np
#img=cv2.imread("./test/00401.jpg") # No se ve un pimiento, es super oscura ¿aclararla?
#img=cv2.imread("./test/00423.jpg")
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#plt.show()
#esto aclara la imagen

#m_power_law_transformation = cv2.pow (im, 0.6)
#cv2.imshow ('Original Image', img)
#cv2.imshow ('Power Transformación de ley ', im)
#cv2.waitKey (0)


# aqui buscaremos color rojo
# un color no es un unico numero asique vamos a poner un rango 100, 200 .... cuantos
#RGB rojo el primero pero el rango tiene que incluir parte de verde y azul, pq tb hay rojos con parte de estos
# pero cuanto
#https://omes-va.com/deteccion-de-colores/
#en esa pagina si no lo saco viene
#rango_parte_inferior_bajo = np.array([0,100,20], np.uint8)
#rango_parte_superior_bajo =  np.array([8,255,255], np.uint8)
#rango_parte_inferior_alto =  np.array([175,100,20], np.uint8)
#rango_parte_superior_alto = np.array([179,255,255], np.uint8)

#Establecemos el rango mínimo y máximo de (Blue, Green, Red):
#OpenCV utiliza el espacio de color BGR en vez de RGB (es decir, invierte el orden de las componentes R y B)
#rojo_bajos = np.array([0,111,255])
#rojo_altos = np.array([0, 0, 113])

# Detectamos los píxeles que estén dentro del rango que hemos establecido:
#mask = cv2.inRange(im, rojo_bajos, rojo_altos)

#Mostramos la imagen original y la máscara:
#cv2.imshow("Original", im)
#cv2.imshow("Rojo", mask)

from random import random
from colorsys import hsv_to_rgb
from matplotlib import pyplot as plt
img=cv2.imread("./test/00482.jpg", 0)

#inicializamos la imagen RGB a niveles de gris
img2 = cv2.imread("./test/00482.jpg", cv2.IMREAD_GRAYSCALE)

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

#cv2.imshow("foto", image2,  vmin=0, vmax=255)
cv2.imshow("foto2", imu)
cv2.imshow("foto3", output)
cv2.waitKey(0)