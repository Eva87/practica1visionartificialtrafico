# Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
import cv2
import random
import colorsys
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
        colorRGB = colorsys.hsv_to_rgb(random.random(), 1, 1)
        colorRGB = tuple(int(color * 255) for color in colorRGB)
        salidaMSER = cv2.fillPoly(arrayCeros, [polygon], colorRGB)
    return salidaMSER, polygons


def recorteCorrelarSignals(contornosimagenentrada, imagenCopia, imgorigin, funcionoriginaria, nombreimageent):
    yk, xk, canales = imagenCopia.shape
    for con in contornosimagenentrada:
        if funcionoriginaria == "AlternativaMSER":
            rect = cv2.minAreaRect(con)
            box = np.int0(cv2.boxPoints(rect))
            distancia1 = rect[1][0]
            distancia2 = rect[1][1]
            if (abs(distancia1 - distancia2) < 30 and distancia1 > 10):
                x1 = max([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
                x2 = min([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
                y1 = max([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
                y2 = min([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
                x1 = x1 - 5
                x2 = x2 + 5
                y1 = y1 - 5
                y2 = y2 + 5
                if x1 < 0:
                    x1 = 0
                if y1 < 0:
                    y1 = 0
                if x2 > xk:
                    x2 = xk
                if y2 > yk:
                    y2 = yk
                if x1 - x2 > 0 and y1 - y2 > 0:
                    # Aqui recortamos la imagen encontrada como contorno
                    imagenAuxiliar = imgorigin[x2:x1, y2:y1]
                    imagenCopia=guardados(imagenAuxiliar, nombreimageent, funcionoriginaria, x1, x2, y1, y2, imagenCopia)
        else:
            x, y, w, h = cv2.boundingRect(con)
            x = x - 5
            y = y - 5
            x2 = x + w + 5
            y2 = y + h + 5
            if x < 0:
                x = 0
            if y < 0:
                y = 0
            if x2 > xk:
                x2 = xk
            if y2 > yk:
                y2 = yk
            if (abs(w - h) < 30 and w > 10):
                if w > 0 and h > 0:
                    # Aqui recortamos la imagen encontrada con rectangulo
                    imagenAuxiliar = imgorigin[y:y2, x:x2]
                    imagenCopia=guardados(imagenAuxiliar, nombreimageent, funcionoriginaria, x, x2, y, y2, imagenCopia)
    return ()


def guardados(imagenAuxil, nombreimagee, funcionoriginar, x11, x22, y11, y22, imagenCopi):
    try:
        if imagenAuxil is not None:
            # redimensionamos imagen de la señal filtrada a 25*25
            redimensionado = cv2.resize(imagenAuxil, tamannoredimension, interpolation=cv2.INTER_AREA)
            (puntos, variablesen) = correlarMascara(redimensionado)
            nombreimagee = nombreimagee[-9:]
            if variablesen != 4:
                cv2.rectangle(imagenCopi, (x11, y11), (x22, y22), (0, 0, 255), 2)
            guardarcarpetasyfichero(nombreimagee, funcionoriginar, x11, x22, y11, y22, variablesen, puntos)
            guardarimagencarpeta(funcionoriginar, nombreimagee, imagenCopi)
    except:
        print(nombreimagee + " la imagen no funciona")
    return (imagenCopi)
