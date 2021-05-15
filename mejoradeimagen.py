#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
import cv2
from random import random
from colorsys import hsv_to_rgb
from guardarficherosennalessalida import *
from signalMask import *

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
    mser = cv2.MSER_create(_delta=5, _max_variation=0.5, _max_area=20000, _min_area=200)
    polygons = mser.detectRegions(imageUint8)
    salidaMSER=None
    for polygon in polygons[0]:
        colorRGB = hsv_to_rgb(random(), 1, 1)
        colorRGB = tuple(int(color * 255) for color in colorRGB)
        salidaMSER = cv2.fillPoly(arrayCeros, [polygon], colorRGB)
    return salidaMSER

def recorteCorrelarSignals(contornosimagenentrada,res,res2,imgorigin,originario,nombreimageent):

    for con in contornosimagenentrada:
        rect = cv2.minAreaRect(con)
        box = np.int0(cv2.boxPoints(rect))
        distancia1 = rect[1][0]
        distancia2 = rect[1][1]
        if (abs(distancia1 - distancia2) < 30 and distancia1>10):

            cv2.drawContours(res, [box], -1, (0, 0, 255), 2)
            cv2.drawContours(res2, [box], -1, (0, 0, 255), 2)

            x1 = max([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
            x2 = min([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
            y1 = max([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
            y2 = min([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])

            if x1 - x2 > 0 and y1 - y2 > 0:
                # Aqui recortamos la imagen encontrada como contorno
                temp = imgorigin[x2:x1, y2:y1]


                try:
                    #cv2.imshow(nombreimageent+'sign' + str(i), temp)
                    if temp is not None:
                        # redimensionamos imagen de la señal filtrada a 25*25
                        dim = (25, 25)
                        redimensionado = cv2.resize(temp, dim, interpolation=cv2.INTER_AREA)

                        (puntos,variablesen) = correlarMascara(redimensionado)

                        '''
                        si la imagen es en byn o escala de gris hacer la mascara de correlacion nuevamente
                        para estos parametros indicando que la imagen es gris o como masamos en nombreimageent, 
                        que es la funcion que esta llamando que lo determine ella
                        '''

                        guardarcarpetasyfichero(nombreimageent+"  "+originario,x1,x2,y1,y2,variablesen,puntos)
                        guardarimagencarpeta(redimensionado,variablesen,originario,nombreimageent)
                except:
                    print(nombreimageent+" la imagen no funciona")

    '''cv2.imshow('res', res)
    cv2.imshow('res2', res2)
    cv2.waitKey(0)'''
    return ()


