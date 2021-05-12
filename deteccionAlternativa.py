import cv2
import numpy as np
from mascarasdelasformasdelassennales import *
from mejoradeimagen import *
imagen = cv2.imread("./train/00141.ppm")
imagen = cv2.imread("./test/00575.jpg")
imagenH = cv2.imread("./train/00141.ppm",cv2.IMREAD_GRAYSCALE)
imagen = cv2.imread("./test/00411.jpg")
imagen = cv2.imread("./test/00420.jpg")
imagen = cv2.imread("./test/00403.jpg")
imagen = cv2.imread("./test/00482.jpg")
imagen = cv2.imread("./test/00434.jpg") # Funciona
imagen = cv2.imread("./test/00482.jpg", cv2.IMREAD_COLOR)


#contrast_img = cv2.addWeighted(imagen, 2.5, np.zeros(imagen.shape, imagen.dtype), 0, 0)
imagenhsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)


(cannybordes, cerradoimagen)=filtradorojoDifuminarNucleoCerradoCanny(imagenhsv)
#erode = cv2.erode(closed, None, iterations=4)
#dilate = cv2.dilate(erode, None, iterations=4)

contours, hierarchy = cv2.findContours(cerradoimagen.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.findContours(cerradoimagen.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('number', len(contours))

i = 0
res = imagen.copy()
for con in contours:
    rect = cv2.minAreaRect(con)
    box = np.int0(cv2.boxPoints(rect))
    cv2.drawContours(res, [box], -1, (0, 0, 255), 2)
    print([box])




h1 = max([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
h2 = min([box][0][0][1], [box][0][1][1], [box][0][2][1], [box][0][3][1])
l1 = max([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
l2 = min([box][0][0][0], [box][0][1][0], [box][0][2][0], [box][0][3][0])
print('h1', h1)
print('h2', h2)
print('l1', l1)
print('l2', l2)

aux = None

if h1 - h2 > 0 and l1 - l2 > 0:
    temp = imagen[h2:h1, l2:l1]
    i = i + 1
    cv2.imshow('sign' + str(i), temp)
    aux = temp
    aux = cv2.cvtColor(aux,cv2.COLOR_BGR2GRAY)



#redimensionamos imagen de la señal filtrada a 25*25
dim = (25, 25)
resized = cv2.resize(aux, dim, interpolation = cv2.INTER_AREA)



(auxiliarsumamascarastop,auxiliarsumamascaraprohibido,auxiliarsumamascarapeligro) = correlarm_aplicarmascarasennal(redimensionado)





cv2.imshow('res', res)
cv2.imshow('hsv', imagenhsv)
cv2.imshow('closed', cerradoimagen)
cv2.imshow('resized', resized)
#cv2.imshow('erode', erode)
#cv2.imshow('dilate', dilate)
cv2.waitKey(0)



#Ideas
# 1-pasar a hsv
# 2-threshold
# 3-redthreshold
# 4-canny
# 5-findcontours
# 6-detectar si es triangulo....¿?
# 7-sacar los puntos de la ubicacion