import math

import numpy as np
import cv2
from random import random
from colorsys import hsv_to_rgb

from guardarficherosennalessalida import *
from mascarasdelasformasdelassennales import *
def mascararojo (imagenHSV):
    rojo_bajo = np.array([0, 80, 40])
    rojo_alto = np.array([10, 255, 255])
    rojo_bajo2 = np.array([160, 50, 45])
    rojo_alto2 = np.array([186, 255, 255])
    mascara1 = cv2.inRange(imagenHSV, rojo_bajo, rojo_alto)
    mascara2 = cv2.inRange(imagenHSV, rojo_bajo2, rojo_alto2)
    mascaraFinal = cv2.add(mascara1, mascara2)

    blurdifuminarrojo = cv2.blur(mascaraFinal, (9, 9))

    retderecho, binario = cv2.threshold(blurdifuminarrojo, 127, 255, cv2.THRESH_BINARY)

    return retderecho,binario

def filtradorojoDifuminarNucleoCerradoCanny(entimagenHSV):
    retdere,binary=mascararojo(entimagenHSV)
    nucleo = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    cerradoimag = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, nucleo)
    cannybord = cv2.Canny(cerradoimag, 200, 300)
    return (cannybord,cerradoimag)


def hacedordeMSER(imagenColor):
    # imagen oscura 20 y imagen clara 100
    imageUint8 = ((imagenColor > 100) * 255).astype(np.uint8)
    # MSER
    arrayCeros = np.zeros((imageUint8.shape[0], imageUint8.shape[1], 3), dtype=np.uint8)
    mser = cv2.MSER_create(_delta=5, _max_variation=0.5, _max_area=20000)
    polygons = mser.detectRegions(imageUint8)
    for polygon in polygons[0]:
        colorRGB = hsv_to_rgb(random(), 1, 1)
        colorRGB = tuple(int(color * 255) for color in colorRGB)
        salidaMSER = cv2.fillPoly(arrayCeros, [polygon], colorRGB)

    return salidaMSER

def hacedorDeCachitosYMascaraSennales(contornosimagenentrada,res,res2,imgorigin,originario):
    i = 0
    imagenvariableretornoposiciones=None
    variableretornoposiciones=None
    for con in contornosimagenentrada:
        rect = cv2.minAreaRect(con)
        box = np.int0(cv2.boxPoints(rect))

        distancia1 = rect[1][0]
        distancia2 = rect[1][1]

        if (abs(distancia1 - distancia2) < 30 and distancia1>25):

            cv2.drawContours(res, [box], -1, (0, 0, 255), 2)
            cv2.drawContours(res2, [box], -1, (0, 0, 255), 2)

            h1 = max([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
            h2 = min([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
            l1 = max([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
            l2 = min([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])

            aux = 0
            if h1 - h2 > 0 and l1 - l2 > 0:
                # Aqui recortamos la imagen encontrada como contorno
                temp = imgorigin[h2:h1, l2:l1]
                imagenvariableretornoposiciones=(temp)
                variableretornoposiciones=(h1,h2,l1,l2)
                i = i + 1
                cv2.imshow('sign' + str(i), temp)
                aux = temp
                # aux = cv2.cvtColor(aux,cv2.COLOR_BGR2GRAY)

                if aux is not None:
                    # redimensionamos imagen de la señal filtrada a 25*25
                    dim = (25, 25)
                    redimensionado = cv2.resize(aux, dim, interpolation=cv2.INTER_AREA)

                    #redimensionado=mascararojo(redimensionado)





















                    cv2.imshow('redimensionado', redimensionado)

                    '''Ahora la imagen en byn'''

                    (auxiliarsumamascarastop, auxiliarsumamascaraprohibido,
                     auxiliarsumamascarapeligro, auxiliarsumamascarapeligro45) = correlarm_aplicarmascarasennal(
                        redimensionado)


                    '''   print("auxiliarsumamascarastop")
                    print(auxiliarsumamascarastop)

                    print("auxiliarsumamascarapeligro")
                    print(auxiliarsumamascarapeligro)
                    print("auxiliarsumamascarapeligro45")
                    print(auxiliarsumamascarapeligro45)

                    print("auxiliarsumamascaraprohibido")
                    print(auxiliarsumamascaraprohibido)'''
                    # Aqui comparamos la imagen redimensionada con las mascaras que tenemos de las señales
                    # Y lo guardamos en una variable segun su situacion y señal que es
                    # Tambien guardaremos la imagen en una carpeta o en 3 carpetas una para cada señal
                    # Si es rgb

                    '''
                    variablesennal=4
                    if auxiliarsumamascarastop > auxiliarsumamascarapeligro and auxiliarsumamascarastop > auxiliarsumamascaraprohibido and auxiliarsumamascarastop > auxiliarsumamascarapeligro45:
                        print("stop rgb")
                        variablesennal =0
                    elif auxiliarsumamascaraprohibido > auxiliarsumamascarapeligro and auxiliarsumamascaraprohibido > auxiliarsumamascarapeligro45 and auxiliarsumamascaraprohibido > auxiliarsumamascarastop:
                        print("prohibido rgb")
                        variablesennal =1
                    elif (auxiliarsumamascarapeligro > auxiliarsumamascarastop and auxiliarsumamascarapeligro > auxiliarsumamascaraprohibido) or (auxiliarsumamascarapeligro45 > auxiliarsumamascarastop and auxiliarsumamascarapeligro45> auxiliarsumamascaraprohibido):
                        print("peligro rgb")
                        variablesennal =2
                    else:
                        print("stop2 rgb")
                        variablesennal =3
                    '''
                    
                    variablesennal=4
                    if auxiliarsumamascarastop[0] > auxiliarsumamascarapeligro[0] and auxiliarsumamascarastop[0] > auxiliarsumamascaraprohibido[0] and auxiliarsumamascarastop[0] > auxiliarsumamascarapeligro45[0]:
                        print("stop rgb")
                        variablesennal =3
                    elif auxiliarsumamascaraprohibido[0] > auxiliarsumamascarapeligro[0] and auxiliarsumamascaraprohibido[0] > auxiliarsumamascarapeligro45[0] and auxiliarsumamascaraprohibido[0] > auxiliarsumamascarastop[0]:
                        print("prohibido rgb")
                        variablesennal =1
                    elif (auxiliarsumamascarapeligro[0] > auxiliarsumamascarastop[0] and auxiliarsumamascarapeligro[0] > auxiliarsumamascaraprohibido[0]) or (auxiliarsumamascarapeligro45[0] > auxiliarsumamascarastop[0] and auxiliarsumamascarapeligro45[0] > auxiliarsumamascaraprohibido[0]):
                        print("peligro rgb")
                        variablesennal =2
                    else:
                        variablesennal =0

                    '''# si es bgr
                    if auxiliarsumamascarastop[2] > auxiliarsumamascarapeligro[2] and auxiliarsumamascarastop[2] > \
                            auxiliarsumamascaraprohibido[2] and auxiliarsumamascarastop[2] > \
                            auxiliarsumamascarapeligro45[2]:
                        print("stop  bgr")
                    elif auxiliarsumamascaraprohibido[2] > auxiliarsumamascarapeligro[2] and \
                            auxiliarsumamascaraprohibido[2] > auxiliarsumamascarapeligro45[2] and \
                            auxiliarsumamascaraprohibido[2] > auxiliarsumamascarastop[2]:
                        print("prohibido bgr")
                    elif (auxiliarsumamascarapeligro[2] > auxiliarsumamascarastop[2] and auxiliarsumamascarapeligro[2] >
                          auxiliarsumamascaraprohibido[2]) or (
                            auxiliarsumamascarapeligro45[2] > auxiliarsumamascarastop[2] and
                            auxiliarsumamascarapeligro45[2] > auxiliarsumamascaraprohibido[2]):
                        print("peligro bgr")'''
                    guardarcarpetasyfichero(h1,h2,l1,l2,variablesennal)
                    guardarimagencarpeta(redimensionado,variablesennal,originario)

    cv2.imshow('res', res)
    cv2.imshow('res2', res2)
    cv2.waitKey(0)
    return ()


