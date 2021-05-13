import cv2
import numpy as np
from mascarasdelasformasdelassennales import *
from mejoradeimagen import *
imagenH = cv2.imread("./train/00141.ppm",cv2.IMREAD_GRAYSCALE)
imagen = cv2.imread("./test/00482.jpg", cv2.IMREAD_COLOR)
imagen = cv2.imread("./test/00434.jpg") # Funciona
imagen = cv2.imread("./test/00403.jpg")
imagen = cv2.imread("./test/00420.jpg")
imagen = cv2.imread("./test/00411.jpg")
imagen = cv2.imread("./test/00575.jpg")
imagen = cv2.imread("./train/00141.ppm")


imagen = cv2.imread("./train/00013.ppm")  # Funciona prohibido ok bien ambas
imagen = cv2.imread("./test/00507.jpg")  # Funciona peligro con cachito bien ambas
imagen = cv2.imread("./test/00548.jpg")  # Funciona stop 3  ambas
imagen = cv2.imread("./test/00428.jpg")  #
imagen = cv2.imread("./test/00446.jpg")  # Funciona prohibido ok 1 bien 1 mal ambas
imagen = cv2.imread("./test/00482.jpg", cv2.IMREAD_COLOR) #Las dos señales de stop juntas no se muestra
imagen = cv2.imread("./train/00027.ppm")  # Funciona prohibido ok bien ambas



#contrast_img = cv2.addWeighted(imagen, 2.5, np.zeros(imagen.shape, imagen.dtype), 0, 0)
imagenhsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)


(cannybordes, cerradoimagen)=filtradorojoDifuminarNucleoCerradoCanny(imagenhsv)



contornos, hierarchy = cv2.findContours(cerradoimagen.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.findContours(cerradoimagen.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contornos) > 0:
    result2 = imagen.copy()
    hacedorDeCachitosYMascaraSennales(contornos, result2, result2, imagen)



cv2.imshow('hsv', imagenhsv)
cv2.imshow('closed', cerradoimagen)
#cv2.imshow('erode', erode)
#cv2.imshow('dilate', dilate)
cv2.waitKey(0)

