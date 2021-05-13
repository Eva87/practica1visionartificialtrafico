#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
#pip install opencv-contrib-python
import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import random
from colorsys import hsv_to_rgb
import sys
from mascarasdelasformasdelassennales import *
from mejoradeimagen import *

imagen = cv2.imread("./test/00482.jpg", cv2.IMREAD_COLOR) #Las dos señales de stop juntas no se muestra
imagen = cv2.imread("./test/00446.jpg")  # Funciona prohibido ok 1 bien 1 mal ambas
imagen = cv2.imread("./train/00013.ppm")  # Funciona prohibido ok bien ambas
imagen = cv2.imread("./train/00013.ppm")  # Funciona prohibido ok bien ambas
imagen = cv2.imread("./test/00434.jpg")  # Funciona ok es prohibido y pone peligro mal ambas
imagen = cv2.imread("./test/00482.jpg")  # Funciona prohibido ok esta es la rectangular no la coge
imagen = cv2.imread("./train/00023.ppm")  # peligro no coge peligro mal ambas
imagen = cv2.imread("./test/00557.jpg")  # Funciona ceda y peligro bien en rgb ceda reconoce peligro en rgb
imagen = cv2.imread("./test/00481.jpg")  # Funciona peligro no ambas
imagen = cv2.imread("./test/00548.jpg")  # Funciona stop 3 mal ambas
imagen = cv2.imread("./test/00507.jpg")  # Funciona peligro con cachito bien ambas
imagen = cv2.imread("./test/00567.jpg")  # Funciona medio peligro y prohibido no saca nada
imagen = cv2.imread("./test/00411.jpg")  # Funciona prohibido ok bien rgb
imagen = cv2.imread("./test/00455.jpg")  # Funciona medio peligro nada

imagen = cv2.imread("./test/00465.jpg")  # Funciona ceda no pilla el ceda
imagen = cv2.imread("./test/00434.jpg")  # Funciona prohibido mal ambos
imagen = cv2.imread("./train_recortadas/21/00004.ppm")  # Falla las recortadas no pilla nada
imagen = cv2.imread("./test/00575.jpg")  # pilla 4 vacias
imagen = cv2.imread("./train/00141.ppm")  #  no pilla nada
imagen = cv2.imread("./train/00078.ppm")  # Funciona peligro bien rgb


'''
imagen = cv2.imread("./test/00444.jpg")
imagen = cv2.imread("./test/00445.jpg")
imagen = cv2.imread("./test/00403.jpg")  # No funciona
imagen = cv2.imread("./test/00400.jpg")  # No funciona
imagen = cv2.imread("./test/00420.jpg")  # No funciona
'''

imagenescalagrises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
imagenhsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

(cannybordes, cerradoimagen) = filtradorojoDifuminarNucleoCerradoCanny(imagenhsv)
salMSER = hacedordeMSER(cannybordes)


guardarenfichero=hacedorDeCachitosYMascaraSennales(cannybordes)


contornos, jerarquia = cv2.findContours(cannybordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print('number', len(contornos))

i = 0
res = salMSER.copy()
res2 = imagen.copy()
for con in contornos:
    rect = cv2.minAreaRect(con)
    box = np.int0(cv2.boxPoints(rect))

    distancia1 = rect[1][0]
    distancia2 = rect[1][1]

    if (abs(distancia1 - distancia2) < 10 and distancia1>25):
    #if (abs(distancia1 - distancia2) < 30 and distancia1>25):

        cv2.drawContours(res, [box], -1, (0, 0, 255), 2)
        cv2.drawContours(res2, [box], -1, (0, 0, 255), 2)

        h1 = max([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
        h2 = min([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
        l1 = max([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
        l2 = min([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])

        aux = 0
        if h1 - h2 > 0 and l1 - l2 > 0:
            #Aqui recortamos la imagen encontrada como contorno
            temp = imagen[h2:h1, l2:l1]
            i = i + 1
            cv2.imshow('sign' + str(i), temp)
            aux = temp
            # aux = cv2.cvtColor(aux,cv2.COLOR_BGR2GRAY)

            if aux  is not None :
                # redimensionamos imagen de la señal filtrada a 25*25
                dim = (25, 25)
                redimensionado = cv2.resize(aux, dim, interpolation=cv2.INTER_AREA)

                '''Ahora la imagen en byn'''

                (auxiliarsumamascarastop, auxiliarsumamascaraprohibido,
                 auxiliarsumamascarapeligro,auxiliarsumamascarapeligro45) = correlarm_aplicarmascarasennal(redimensionado)

                print("auxiliarsumamascarastop")
                print(auxiliarsumamascarastop)

                print("auxiliarsumamascarapeligro")
                print(auxiliarsumamascarapeligro)
                print("auxiliarsumamascarapeligro45")
                print(auxiliarsumamascarapeligro45)

                print("auxiliarsumamascaraprohibido")
                print(auxiliarsumamascaraprohibido)
                #Aqui comparamos la imagen redimensionada con las mascaras que tenemos de las señales
                #Y lo guardamos en una variable segun su situacion y señal que es
                # Tambien guardaremos la imagen en una carpeta o en 3 carpetas una para cada señal
                #Si es rgb
                if auxiliarsumamascarastop[0]>auxiliarsumamascarapeligro[0] and auxiliarsumamascarastop[0]>auxiliarsumamascaraprohibido[0] and  auxiliarsumamascarastop[0]>auxiliarsumamascarapeligro45[0]:
                    print("stop rgb")
                elif auxiliarsumamascaraprohibido[0]>auxiliarsumamascarapeligro[0] and auxiliarsumamascaraprohibido[0]>auxiliarsumamascarapeligro45[0] and auxiliarsumamascaraprohibido[0]>auxiliarsumamascarastop[0]:
                    print("prohibido rgb")
                elif (auxiliarsumamascarapeligro[0]>auxiliarsumamascarastop[0] and auxiliarsumamascarapeligro[0]>auxiliarsumamascaraprohibido[0]) or (auxiliarsumamascarapeligro45[0]>auxiliarsumamascarastop[0] and auxiliarsumamascarapeligro45[0]>auxiliarsumamascaraprohibido[0]):
                    print("peligro rgb")

                #si es bgr
                if auxiliarsumamascarastop[2]>auxiliarsumamascarapeligro[2] and auxiliarsumamascarastop[2]>auxiliarsumamascaraprohibido[2] and  auxiliarsumamascarastop[2]>auxiliarsumamascarapeligro45[2]:
                    print("stop  bgr")
                elif auxiliarsumamascaraprohibido[2]>auxiliarsumamascarapeligro[2] and auxiliarsumamascaraprohibido[2]>auxiliarsumamascarapeligro45[2] and auxiliarsumamascaraprohibido[2]>auxiliarsumamascarastop[2]:
                    print("prohibido bgr")
                elif (auxiliarsumamascarapeligro[2]>auxiliarsumamascarastop[2] and auxiliarsumamascarapeligro[2]>auxiliarsumamascaraprohibido[2]) or (auxiliarsumamascarapeligro45[2]>auxiliarsumamascarastop[2] and auxiliarsumamascarapeligro45[2]>auxiliarsumamascaraprohibido[2]):
                    print("peligro bgr")

                '''

                         problema, hay que pasar la imagen a blanco y negro o no
                         Ana dice que si, yo creo que no pero....


                         Y luego cuando se sepa si es la señal o no a una nueva funcion le pasariamos los 4 puntos 
                         y la señal que es
                         pero es cuando ya funcione
                         y es comun a todos

                         por cierto cuando funcione lo de los contornos, tambien sera una funcion comun, asique habra que moverlo
                         pero es problema de nuestros yo de mañana
                '''
                '''Lo siguiente es si es tal o pascual guardar en ficherosalida
                y guardar las señales reconocidas en carpeta salida por ejemplo'''

                '''
                cv2.imshow('redimensionado', redimensionado)

                cv2.imshow('aux', aux)'''
#Aqui lo sacamos al fichero de texto
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
cv2.imshow('res', res)
cv2.imshow('res2', res2)
'''cv2.imshow('canny', cannybordes)
cv2.imshow('salidadelmser', salMSER)'''
cv2.waitKey(0)


