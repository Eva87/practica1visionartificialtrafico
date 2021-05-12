import cv2
import numpy as np
from random import random
from colorsys import hsv_to_rgb
from mascarasdelasformasdelassennales import *
from mejoradeimagen import *


img=cv2.imread("./test/00482.jpg", 0)


#inicializamos la imagen RGB a niveles de gris
imagenGris = cv2.imread("./test/00482.jpg", cv2.IMREAD_GRAYSCALE)
imagenColor = cv2.imread("./test/00482.jpg", cv2.IMREAD_COLOR)

'''

contrast_img = cv2.addWeighted(imagenColor, 2.5, np.zeros(imagenColor.shape, imagenColor.dtype), 0, 0)
imagenhsv = cv2.cvtColor(imagenColor, cv2.COLOR_BGR2HSV)
cv2.imshow('original',imagenColor)
cv2.imshow('conContraste',contrast_img)
cannyImagen2 = cv2.Canny(imagenColor,200,300)
cv2.imshow('COriginal',cannyImagen2)

rojo_bajo = np.array([0, 80, 40])
rojo_alto = np.array([10, 255, 255])
rojo_bajo2 = np.array([160, 50, 45])
rojo_alto2 = np.array([186, 255, 255])
mascara1 = cv2.inRange(imagenhsv, rojo_bajo, rojo_alto)
mascara2 = cv2.inRange(imagenhsv, rojo_bajo2, rojo_alto2)
mascaraFinal = cv2.add(mascara1,mascara2)

blurdifuminarrojo = cv2.blur(mascaraFinal, (9, 9))


retderecho, binario = cv2.threshold(blurdifuminarrojo, 127, 255, cv2.THRESH_BINARY)
nucleo = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
cerradoimagen = cv2.morphologyEx(binario, cv2.MORPH_CLOSE, nucleo)
cannybordes = cv2.Canny(cerradoimagen, 200, 300)


imageUint8 = ((cannybordes > 100) * 255).astype(np.uint8)

#MSER
arrayCeros = np.zeros((imageUint8.shape[0], imageUint8.shape[1], 3), dtype=np.uint8)
mser = cv2.MSER_create(_delta=5,_max_variation=0.5,_max_area=20000)
polygons = mser.detectRegions(imageUint8)
for polygon in polygons[0]:
    colorRGB = hsv_to_rgb(random(),1,1)
    colorRGB = tuple(int(color*255) for color in colorRGB)
    salidaMSER = cv2.fillPoly(arrayCeros, [polygon], colorRGB)'''


imagenhsv = cv2.cvtColor(imagenColor, cv2.COLOR_BGR2HSV)
cv2.imshow('original',imagenColor)


(cannybordes, cerradoimagen)=filtradorojoDifuminarNucleoCerradoCanny(imagenhsv)
salMSER=hacedordeMSER(cannybordes)


# Convertimos la imagen a escala de grises.
gray = cv2.cvtColor(salMSER, cv2.COLOR_BGR2GRAY)

'''ret, binary = cv2.threshold(salidaMSER, 127, 255, 0)


contours, hierarchy = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
imagencontornos = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt=contours[0]
x,y,w,h=cv2.boundingRect(cnt)
img =cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)'''


contours, hierarchy = cv2.findContours(cerradoimagen.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.findContours(cerradoimagen.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
i = 0
res = imagenColor.copy()
for con in contours:
    rect = cv2.minAreaRect(con)
    box = np.int0(cv2.boxPoints(rect))


    cv2.drawContours(res, [box], -1, (0, 0, 255), 2)
    print([box])


(auxiliarsumamascarastop,auxiliarsumamascaraprohibido,auxiliarsumamascarapeligro) = correlarm_aplicarmascarasennal(res)




cv2.imshow('res', res)
cv2.imshow("rectascalculadas", img)
cv2.imshow("salidaMSER", salMSER)
cv2.waitKey(0)
