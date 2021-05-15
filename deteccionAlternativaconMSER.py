#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
#pip install opencv-contrib-python
import cv2
from mejoradeimagen import *

imagen = cv2.imread("./train/00013.ppm")  # Funciona prohibido ok bien ambas


imagen = cv2.imread("./test/00434.jpg")  # Funciona ok es prohibido y pone peligro mal ambas
imagen = cv2.imread("./train/00023.ppm")  # peligro no coge peligro mal ambas
imagen = cv2.imread("./test/00481.jpg")  # Funciona peligro no ambas
imagen = cv2.imread("./test/00431.jpg")  #
imagen = cv2.imread("./test/00434.jpg")  # Funciona prohibido mal ambos
imagen = cv2.imread("./test/00423.jpg")  #
imagen = cv2.imread("./train/00078.ppm")  # Funciona peligro

imagen = cv2.imread("./test/00557.jpg")  # Funciona ceda y peligro bien en rgb ceda reconoce peligro en rgb
imagen = cv2.imread("./test/00411.jpg")  # Funciona prohibido ok bien rgb
imagen = cv2.imread("./test/00433.jpg")
imagen = cv2.imread("./train_10_ejemplos/00001.ppm")
imagen = cv2.imread("./train_recortadas/00/00003.ppm")
imagen = cv2.imread("./train_10_ejemplos/00003.ppm")
imagen = cv2.imread("./test/00411.jpg")  # bien rgb
imagen = cv2.imread("./20201003121440748.jpg")

'''
imagen = cv2.imread("./test/00567.jpg")  # Funciona medio peligro y prohibido no saca nada
imagen = cv2.imread("./train/00141.ppm")  #  no pilla nada
imagen = cv2.imread("./test/00575.jpg")  # pilla 4 vacias
imagen = cv2.imread("./test/00402.jpg")  #
imagen = cv2.imread("./test/00419.jpg")  #
imagen = cv2.imread("./test/00413.jpg")  #
imagen = cv2.imread("./test/00416.jpg")  #
'''
strinentradaimg="./train_recortadas/01/00022.ppm"
imagen = cv2.imread("./test/00507.jpg")  # Funciona peligro con cachito bien ambas
imagen = cv2.imread("./test/00431.jpg")
imagen = cv2.imread("./test/00428.jpg")  #
imagen = cv2.imread("./test/00446.jpg")  # Funciona prohibido ok 1 bien 1 mal ambas
imagen = cv2.imread("./test/00548.jpg")  # Funciona stop 3  ambas
imagen = cv2.imread("./train/00013.ppm")  # Funciona prohibido ok bien ambas
imagen = cv2.imread("./test/00482.jpg", cv2.IMREAD_COLOR) #Las dos señales de stop juntas no se muestra
imagen = cv2.imread(strinentradaimg)



imagen=cv2.medianBlur(imagen,5)
imagenhsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

(cannybordes, cerradoimagen) = filtradorojoDifuminarNucleoCerradoCanny(imagenhsv)

contornos, jerarquia = cv2.findContours(cannybordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contornos) > 0:
    salMSER = hacedordeMSER(cannybordes)
    if salMSER is not None:
        result = salMSER.copy()
        result2 = imagen.copy()

        recorteCorrelarSignals(contornos, result, result2, imagen, "alternativa2", strinentradaimg)

'''
en la salida falta el nombre de entrada al principio y el peso al final

como usar el main.py
'''


cv2.imshow('original', imagen)
cv2.waitKey(0)


