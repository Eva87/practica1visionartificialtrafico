import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import random
from colorsys import hsv_to_rgb


imagenH = cv2.imread("./train/00141.ppm",cv2.IMREAD_GRAYSCALE)
imagen = cv2.imread("./train/00141.ppm") # Falla
imagen = cv2.imread("./test/00434.jpg") # Funciona
imagen = cv2.imread("./test/00411.jpg") # Funciona
imagen = cv2.imread("./test/00420.jpg") # No funciona
imagen = cv2.imread("./test/00400.jpg") # No funciona
imagen = cv2.imread("./test/00575.jpg") # No funciona...
imagen = cv2.imread("./test/00403.jpg") # No funciona
imagen = cv2.imread("./test/00482.jpg") # Funciona



imagenescalagrises= cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

imagenhsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)


'''
imu = ((imagen >100)*255).astype(np.uint8)
#MSER
salidadelmser = np.zeros((imu.shape[0], imu.shape[1], 3), dtype=np.uint8)
mser = cv2.MSER_create(_delta=5,_max_variation=0.5,_max_area=20000)
polygons = mser.detectRegions(imu)
for polygon in polygons[0]:
    colorRGB = hsv_to_rgb(random(),1,1)
    colorRGB = tuple(int(color*255) for color in colorRGB)
    salidadelmser = cv2.fillPoly(salidadelmser, [polygon], colorRGB)






cannyImagen2 = cv2.Canny(salidadelmser,200,300)'''



contrast_img = cv2.addWeighted(imagen, 2.5, np.zeros(imagen.shape, imagen.dtype), 0, 0)

#msermascanny = salidadelmser and cannyImagen2
#imagenhsv = cv2.cvtColor(contrast_img, cv2.COLOR_BGR2HSV)


rojo_bajo = np.array([0, 80, 40])
rojo_alto = np.array([10, 255, 255])
rojo_bajo2 = np.array([160, 50, 45])
rojo_alto2 = np.array([186, 255, 255])
mascara1 = cv2.inRange(imagenhsv, rojo_bajo, rojo_alto)
mascara2 = cv2.inRange(imagenhsv, rojo_bajo2, rojo_alto2)
mascaraFinal = cv2.add(mascara1,mascara2)

blurdifuminarrojo = cv2.blur(mascaraFinal, (9, 9))


ret, binary = cv2.threshold(blurdifuminarrojo, 127, 255, cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
canny = cv2.Canny(closed,200,300)



imu = ((canny >100)*255).astype(np.uint8)
#MSER
salidadelmser = np.zeros((imu.shape[0], imu.shape[1], 3), dtype=np.uint8)
mser = cv2.MSER_create(_delta=5,_max_variation=0.5,_max_area=20000)
polygons = mser.detectRegions(imu)
for polygon in polygons[0]:
    colorRGB = hsv_to_rgb(random(),1,1)
    colorRGB = tuple(int(color*255) for color in colorRGB)
    salidadelmser = cv2.fillPoly(salidadelmser, [polygon], colorRGB)



contours, hierarchy = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('number', len(contours))


#Aui poner detector de circulos???


i = 0
res = salidadelmser.copy()
for con in contours:
    rect = cv2.minAreaRect(con)
    box = np.int0(cv2.boxPoints(rect))
    cv2.drawContours(res, [box], -1, (0, 0, 255), 2)
    print([box])
    '''Aqui hay que hacer la busqueda de la señal concreta en cada iteracion
    
    Aqui se buscan las mascaras de las señales
    si se encuentran, se guardan en 4 variables que luego se mostraran y se almacenaran txt'''



h1 = max([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
h2 = min([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
l1 = max([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
l2 = min([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
print('h1', h1)
print('h2', h2)
print('l1', l1)
print('l2', l2)

aux = None

if h1 - h2 > 0 and l1 - l2 > 0:
    temp = imagen[h2:h1, l2:l1]
    i = i + 1
    cv2.imshow('sign' + str(i), temp)
    aux = temp
    #aux = cv2.cvtColor(aux,cv2.COLOR_BGR2GRAY)





arrayprohibido= np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                         )






#redimensionamos imagen de la señal filtrada a 25*25
dim = (25, 25)
redimensionado = cv2.resize(aux, dim, interpolation = cv2.INTER_AREA)






cv2.imshow('original',imagen)
cv2.imshow('contrast_img',contrast_img)
cv2.imshow('canny',canny)
cv2.imshow('redimensionado', redimensionado)
cv2.imshow('salidadelmser', salidadelmser)
cv2.imshow('aux', aux)
cv2.waitKey(0)

