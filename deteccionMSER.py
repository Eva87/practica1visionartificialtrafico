import cv2
import numpy as np
from random import random
from colorsys import hsv_to_rgb
from signalMask import *
from mejoradeimagen import *

imagen = cv2.imread("./test/00431.jpg")
imagen = cv2.imread("./train_recortadas/01/00000.ppm")


cv2.imshow("original",imagen)

contrast_img = cv2.addWeighted(imagen, 2.5, np.zeros(imagen.shape, imagen.dtype), 0, 0)
cv2.imshow("contrast",contrast_img)

imagenhsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",imagenhsv)
redDer, bin = mascararojo(imagenhsv)
imagenBinaria = bin
cv2.imshow("gris",imagenBinaria)
cv2.waitKey(0)

salMSER = hacedordeMSER(imagenBinaria)
result = salMSER.copy()
result2 = imagen.copy()
cv2.imshow("MSER",salMSER)

contornos, jerarquia = cv2.findContours(bin.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print( len(contornos))
if len(contornos) > 0:

    recorteCorrelarSignals(contornos, result, result2, imagen,"mser")

cv2.waitKey(0)




