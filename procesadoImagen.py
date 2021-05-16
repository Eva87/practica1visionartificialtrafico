# Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
import cv2
from random import random
from colorsys import hsv_to_rgb
from guardarSalida import *
from signalMask import *

tamannoredimension = (25, 25)


def mascararojo(imagenHSV):
    rojo_bajo = np.array([0, 80, 40])
    rojo_alto = np.array([10, 255, 255])
    rojo_bajo2 = np.array([160, 50, 45])
    rojo_alto2 = np.array([186, 255, 255])
    mascara1 = cv2.inRange(imagenHSV, rojo_bajo, rojo_alto)
    mascara2 = cv2.inRange(imagenHSV, rojo_bajo2, rojo_alto2)
    mascaraFinal = cv2.add(mascara1, mascara2)
    blurdifuminarrojo = cv2.blur(mascaraFinal, (9, 9))
    retderecho, binario = cv2.threshold(blurdifuminarrojo, 127, 255, cv2.THRESH_BINARY)
    return retderecho, binario


def filtradorojoDifuminarNucleoCerradoCanny(entimagenHSV):
    retdere, binary = mascararojo(entimagenHSV)
    nucleo = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    cerradoimag = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, nucleo)
    cannybord = cv2.Canny(cerradoimag, 200, 300)
    return (cannybord, cerradoimag)


def hacedordeMSER(imagenColor):
    # imagen oscura 20 y imagen clara 100
    imageUint8 = ((imagenColor > 100) * 255).astype(np.uint8)
    # MSER
    arrayCeros = np.zeros((imageUint8.shape[0], imageUint8.shape[1], 3), dtype=np.uint8)
    mser = cv2.MSER_create(_delta=5, _max_variation=0.5, _max_area=20000, _min_area=200)
    polygons = mser.detectRegions(imageUint8)
    salidaMSER = None
    for polygon in polygons[0]:
        colorRGB = hsv_to_rgb(random(), 1, 1)
        colorRGB = tuple(int(color * 255) for color in colorRGB)
        salidaMSER = cv2.fillPoly(arrayCeros, [polygon], colorRGB)
    return salidaMSER, polygons


def recorteCorrelarSignals(contornosimagenentrada, imagenCopia, imgorigin, funcionoriginaria, nombreimageent):
    i=0
    for con in contornosimagenentrada:
        if funcionoriginaria == "AlternativaMSER":
            rect = cv2.minAreaRect(con)
            box = np.int0(cv2.boxPoints(rect))
            distancia1 = rect[1][0]
            distancia2 = rect[1][1]
            if (abs(distancia1 - distancia2) < 30 and distancia1 > 10):
                cv2.drawContours(imagenCopia, [box], -1, (0, 0, 255), 2)
                x1 = max([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
                x2 = min([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
                y1 = max([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
                y2 = min([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
                x1 = x1 - 5
                x2 = x2 + 5
                y1 = y1 - 5
                y2 = y2 + 5
                if x1 - x2 > 0 and y1 - y2 > 0:
                    # Aqui recortamos la imagen encontrada como contorno
                    imagenAuxiliar = imgorigin[x2:x1, y2:y1]
                    try:
                        # cv2.imshow(nombreimageent+'sign' + str(i), imagenAuxiliar)
                        if imagenAuxiliar is not None:
                            # redimensionamos imagen de la señal filtrada a 25*25
                            redimensionado = cv2.resize(imagenAuxiliar, tamannoredimension,
                                                        interpolation=cv2.INTER_AREA)
                            (puntos, variablesen) = correlarMascara(redimensionado)
                            guardarcarpetasyfichero(nombreimageent + "  " + funcionoriginaria, x1, x2, y1, y2,
                                                    variablesen, puntos)
                            guardarimagencarpeta(redimensionado, variablesen, funcionoriginaria, nombreimageent)
                    except:
                        print(nombreimageent + " la imagen no funciona")
        else:
            x, y, w, h = cv2.boundingRect(con)
            x = x - 5
            y = y - 5
            w = w + 5
            h = h + 5
            if (abs(w - h) < 30 and w > 10):
                cv2.rectangle(imagenCopia, (x, y), (x + w, y + h), (0, 255, 0), 2)
                if w > 0 and h > 0:
                    # Aqui recortamos la imagen encontrada como contorno
                    imagenAuxiliar = imgorigin[y:(y + h), x:(x + w)]
                    try:
                        # cv2.imshow(nombreimageent+'sign' + str(i), imagenAuxiliar)
                        if imagenAuxiliar is not None:
                            # redimensionamos imagen de la señal filtrada a 25*25
                            redimensionado = cv2.resize(imagenAuxiliar, tamannoredimension,
                                                        interpolation=cv2.INTER_AREA)
                            (puntos, variablesen) = correlarMascara(redimensionado)
                            guardarcarpetasyfichero(nombreimageent + "  " + funcionoriginaria, x, x + w, y, y + h,
                                                    variablesen, puntos)
                            guardarimagencarpeta(redimensionado, variablesen, funcionoriginaria, nombreimageent)
                    except:
                        print(nombreimageent + " la imagen no funciona")

    cv2.imshow("imagenCopia"+nombreimageent,imagenCopia )
    return ()
