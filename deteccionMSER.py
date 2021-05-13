import cv2
import numpy as np
from random import random
from colorsys import hsv_to_rgb
from mascarasdelasformasdelassennales import *
from mejoradeimagen import *




#inicializamos la imagen RGB a niveles de gris
imagen = cv2.imread("./test/00485.jpg")

'''

imagenhsv = cv2.cvtColor(imagenColor, cv2.COLOR_BGR2HSV)
cv2.imshow('original',imagenColor)
cv2.imshow('conContraste',contrast_img)
cv2.imshow('COriginal',cannyImagen2)

'''


contrast_img = cv2.addWeighted(imagen, 2.5, np.zeros(imagen.shape, imagen.dtype), 0, 0)
cannyImagen = cv2.Canny(contrast_img,200,300)

imagenhsv = cv2.cvtColor(contrast_img, cv2.COLOR_BGR2HSV)

rojo_bajo = np.array([0, 80, 40])
rojo_alto = np.array([10, 255, 255])
rojo_bajo2 = np.array([160, 50, 45])
rojo_alto2 = np.array([186, 255, 255])
mascara1 = cv2.inRange(imagenhsv, rojo_bajo, rojo_alto)
mascara2 = cv2.inRange(imagenhsv, rojo_bajo2, rojo_alto2)
mascaraFinal = cv2.add(mascara1, mascara2)

blurdifuminarrojo = cv2.blur(mascaraFinal, (9, 9))

retderecho, binario = cv2.threshold(blurdifuminarrojo, 127, 255, cv2.THRESH_BINARY)
nucleo = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
cerradoimagen = cv2.morphologyEx(binario, cv2.MORPH_CLOSE, nucleo)
erode = cv2.erode(cerradoimagen, None, iterations=4)
#dilate = cv2.dilate(erode, None, iterations=4)
cannybordes = cv2.Canny(erode, 200, 300)



contornos, jerarquia = cv2.findContours(cannybordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print( len(contornos))
if len(contornos) > 0:
    salMSER = hacedordeMSER(cannybordes)

    result = salMSER.copy()
    result2 = imagen.copy()

    hacedorDeCachitosYMascaraSennales(contornos, result, result2, imagen)





