import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import random
from colorsys import hsv_to_rgb
import sys
sys.path.insert(1, './practica1visionartificialtrafico')
'''from mascarasdelasformasdelassennales import arraymaskstop
from mascarasdelasformasdelassennales import arraymaskpeligro
from mascarasdelasformasdelassennales import arraymaskprohibido'''
from mascarasdelasformasdelassennales import *
from mejoradeimagen import *

imagenH = cv2.imread("./train/00141.ppm",cv2.IMREAD_GRAYSCALE)
imagen = cv2.imread("./test/00420.jpg") # No funciona
imagen = cv2.imread("./test/00400.jpg") # No funciona
imagen = cv2.imread("./test/00403.jpg") # No funciona
imagen = cv2.imread("./train/00141.ppm") # Falla
imagen = cv2.imread("./test/00575.jpg") # No funciona...
imagen = cv2.imread("./train_recortadas/21/00001.ppm") # Falla


imagen = cv2.imread("./test/00434.jpg") # Funciona prohibido
imagen = cv2.imread("./test/00465.jpg") # Funciona ceda
imagen = cv2.imread("./test/00481.jpg") # Funciona peligro

imagen = cv2.imread("./test/00567.jpg") # Funciona medio peligro y prohibido
imagen = cv2.imread("./test/00482.jpg") # Funciona prohibido
imagen = cv2.imread("./test/00411.jpg") # Funciona prohibido
imagen = cv2.imread("./test/00446.jpg") # Funciona prohibido
imagen = cv2.imread("./train/00013.ppm") # Funciona prohibido
imagen = cv2.imread("./test/00455.jpg") # Funciona medio peligro
imagen = cv2.imread("./test/00507.jpg") # Funciona peligro con cachito
imagen = cv2.imread("./test/00557.jpg") # Funciona ceda y peligro
imagen = cv2.imread("./train/00023.ppm") # peligro error pq llega a posicion negativa
imagen = cv2.imread("./test/00548.jpg") # Funciona stop
imagen = cv2.imread("./train/00078.ppm") # Funciona prohibido
imagen = cv2.imread("./train/00013.ppm") # Funciona prohibido
imagen = cv2.imread("./test/00482.jpg", cv2.IMREAD_COLOR)
imagen = cv2.imread("./test/00434.jpg") # Funciona



'''
arraymascarastop=arraymaskstop
arraymascarapeligro=arraymaskpeligro
arraymascaraprohibido=arraymaskprohibido'''


imagenescalagrises= cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
imagenhsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)


#contrast_img = cv2.addWeighted(imagen, 2.5, np.zeros(imagen.shape, imagen.dtype), 0, 0)



(cannybordes, cerradoimagen)=filtradorojoDifuminarNucleoCerradoCanny(imagenhsv)
salMSER=hacedordeMSER(cannybordes)


contornos, jerarquia = cv2.findContours(cannybordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


print('number', len(contornos))




i = 0
res = salMSER.copy()
res2 = imagen.copy()
for con in contornos:
    rect = cv2.minAreaRect(con)
    box = np.int0(cv2.boxPoints(rect))
    '''Aqui hay que hacer la busqueda de la señal concreta en cada iteracion
    
    Aqui se buscan las mascaras de las señales
    si se encuentran, se guardan en 4 variables que luego se mostraran y se almacenaran txt'''


    distancia1 = rect[1][0]
    distancia2 = rect[1][1]
    if (abs(distancia1-distancia2)<5):

        cv2.drawContours(res, [box], -1, (0, 0, 255), 2)
        cv2.drawContours(res2, [box], -1, (0, 0, 255), 2)



        h1 = max([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
        h2 = min([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
        l1 = max([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
        l2 = min([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])


        aux = None

        if h1 - h2 > 0 and l1 - l2 > 0:
            temp = imagen[h2:h1, l2:l1]
            i = i + 1
            cv2.imshow('sign' + str(i), temp)
            aux = temp
            #aux = cv2.cvtColor(aux,cv2.COLOR_BGR2GRAY)



    '''problema si no recoge ningun cuadrado da error
     asique hay que hacer que si no hay cuadraros no entrem lo cual no encuentro
     pero es una tontada
     
     
     segundo problema, hay que pasar la imagen a blanco y negro o no
     Ana dice que si, yo creo que no pero....
     
     
     Y luego cuando se sepa si es la señal o no a una nueva funcion le pasariamos los 4 puntos 
     y la señal que es
     pero es cuando ya funcione
     y es comun a todos
     
     por cierto cuando funcione lo de los contornos, tambien sera una funcion comun, asique habra que moverlo
     pero es problema de nuestros yo de mañana
     '''




    if 'aux' in locals():
        #redimensionamos imagen de la señal filtrada a 25*25
        dim = (25, 25)
        redimensionado = cv2.resize(aux, dim, interpolation = cv2.INTER_AREA)

        '''Ahora la imagen en byn'''

        (auxiliarsumamascarastop,auxiliarsumamascaraprohibido,auxiliarsumamascarapeligro) = correlarm_aplicarmascarasennal(redimensionado)



        print("auxiliarsumamascarastop" )
        print( auxiliarsumamascarastop)

        print("auxiliarsumamascarapeligro" )
        print( auxiliarsumamascarapeligro)

        print("auxiliarsumamascaraprohibido" )
        print( auxiliarsumamascaraprohibido)

'''Dudas:


en la salida gt.txt 00027.ppm;969;386;1024;441;2 son cinco valores, con que se corresponden
x1,x2,y1,y2,tiposeñal
almacenar imagenes detectadas


como usar el main.py



'''


cv2.imshow('original',imagen)
cv2.imshow('res',res)
cv2.imshow('res2',res2)
#cv2.imshow('contrast_img',contrast_img)
cv2.imshow('canny', cannybordes)
cv2.imshow('redimensionado', redimensionado)
cv2.imshow('salidadelmser', salMSER)
cv2.imshow('aux', aux)
cv2.waitKey(0)



'''
 #   print([box])

h1 = max([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
h2 = min([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
l1 = max([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
l2 = min([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])

print('h1', h1)
print('h2', h2)
print('l1', l1)
print('l2', l2)'''