#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
#pip install opencv-contrib-python
import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import random
from colorsys import hsv_to_rgb
import sys
from signalMask import *
from mejoradeimagen import *

imagen = cv2.imread("./test/00482.jpg", cv2.IMREAD_COLOR) #Las dos señales de stop juntas no se muestra
imagen = cv2.imread("./train/00013.ppm")  # Funciona prohibido ok bien ambas
imagen = cv2.imread("./train/00013.ppm")  # Funciona prohibido ok bien ambas
imagen = cv2.imread("./test/00507.jpg")  # Funciona peligro con cachito bien ambas
imagen = cv2.imread("./test/00548.jpg")  # Funciona stop 3  ambas
imagen = cv2.imread("./test/00446.jpg")  # Funciona prohibido ok 1 bien 1 mal ambas
imagen = cv2.imread("./test/00428.jpg")  #


imagen = cv2.imread("./test/00434.jpg")  # Funciona ok es prohibido y pone peligro mal ambas
imagen = cv2.imread("./train/00023.ppm")  # peligro no coge peligro mal ambas
imagen = cv2.imread("./test/00481.jpg")  # Funciona peligro no ambas
imagen = cv2.imread("./test/00431.jpg")  #
imagen = cv2.imread("./test/00434.jpg")  # Funciona prohibido mal ambos
imagen = cv2.imread("./test/00423.jpg")  #
imagen = cv2.imread("./train/00078.ppm")  # Funciona peligro

imagen = cv2.imread("./test/00411.jpg")  # bien rgb
imagen = cv2.imread("./test/00557.jpg")  # Funciona ceda y peligro bien en rgb ceda reconoce peligro en rgb
imagen = cv2.imread("./test/00411.jpg")  # Funciona prohibido ok bien rgb
imagen = cv2.imread("./test/00433.jpg")
imagen = cv2.imread("./test/00431.jpg")
imagen = cv2.imread("./20201003121440748.jpg")
imagen = cv2.imread("./train_10_ejemplos/00003.ppm")

'''
imagen = cv2.imread("./test/00409.jpg")  # No tiene señales
imagen = cv2.imread("./test/00407.jpg")  #no tiene señales
imagen = cv2.imread("./test/00429.jpg")  #no tiene naa
imagen = cv2.imread("./train_recortadas/21/00004.ppm")  # Falla las recortadas no pilla nada
imagen = cv2.imread("./test/00567.jpg")  # Funciona medio peligro y prohibido no saca nada
imagen = cv2.imread("./test/00455.jpg")  # Funciona medio peligro nada
imagen = cv2.imread("./train/00141.ppm")  #  no pilla nada
imagen = cv2.imread("./test/00575.jpg")  # pilla 4 vacias
imagen = cv2.imread("./test/00402.jpg")  #
imagen = cv2.imread("./test/00419.jpg")  #
imagen = cv2.imread("./test/00413.jpg")  #
imagen = cv2.imread("./test/00416.jpg")  #
imagen = cv2.imread("./test/00406.jpg")  # prohibido no pilla
imagen = cv2.imread("./test/00427.jpg")  #
imagen = cv2.imread("./test/00425.jpg")  #
imagen = cv2.imread("./test/00482.jpg")  # Funciona prohibido ok esta es la rectangular no la coge
imagen = cv2.imread("./test/00418.jpg")  # dos señales, no distingue a 15 si bien
imagen = cv2.imread("./test/00465.jpg")  # Funciona ceda lo pilla con 12 pero mal
'''

'''
imagen = cv2.imread("./test/00422.jpg")  #
imagen = cv2.imread("./test/00424.jpg")  #
imagen = cv2.imread("./test/00426.jpg")  #
imagen = cv2.imread("./test/00430.jpg")  # 
imagen = cv2.imread("./test/00410.jpg")  #
imagen = cv2.imread("./test/00412.jpg")  #
imagen = cv2.imread("./test/00414.jpg")  #
imagen = cv2.imread("./test/00415.jpg")  #
imagen = cv2.imread("./test/00417.jpg")  #
imagen = cv2.imread("./test/00445.jpg")
imagen = cv2.imread("./test/00403.jpg")  # No funciona
imagen = cv2.imread("./test/00400.jpg")  # No funciona
imagen = cv2.imread("./test/00420.jpg")  # No funciona
imagen = cv2.imread("./test/00444.jpg")
imagen = cv2.imread("./test/00408.jpg")  #
imagen = cv2.imread("./test/00405.jpg")  #
imagen = cv2.imread("./test/00404.jpg")  #
imagen = cv2.imread("./test/00401.jpg")  #
imagen = cv2.imread("./test/00421.jpg")  #
'''




imagenescalagrises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
imagenhsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

(cannybordes, cerradoimagen) = filtradorojoDifuminarNucleoCerradoCanny(imagenhsv)

contornos, jerarquia = cv2.findContours(cannybordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contornos) > 0:
    salMSER = hacedordeMSER(cannybordes)

    result = salMSER.copy()
    result2 = imagen.copy()

    recorteCorrelarSignals(contornos, result, result2, imagen, "alternativa2")



'''
problema, hay que pasar la imagen a blanco y negro o no
'''


'''

en la salida gt.txt 00027.ppm;969;386;1024;441;2 son cinco valores, con que se corresponden
x1,x2,y1,y2,tiposeñal
almacenar imagenes detectadas


como usar el main.py

 guardaremos la imagen en una carpeta o en 3 carpetas una para cada señal

'''
'''
    

Hay que guardar la imagen recortada para seguir trabajando con ella recortada?

imagen es RGB pq funciona mejor si lo trato como BGR

la mascara de 25*25 es mejor con 1 o con 255

    '''

cv2.imshow('original', imagen)
'''cv2.imshow('canny', cannybordes)
cv2.imshow('salidadelmser', salMSER)'''
cv2.waitKey(0)


