import cv2
import numpy as np
imagen = cv2.imread("./train/00141.ppm")
imagen = cv2.imread("./test/00575.jpg")
imagenH = cv2.imread("./train/00141.ppm",cv2.IMREAD_GRAYSCALE)
imagen = cv2.imread("./test/00411.jpg")
imagen = cv2.imread("./test/00420.jpg")
imagen = cv2.imread("./test/00403.jpg")
imagen = cv2.imread("./test/00482.jpg")
imagen = cv2.imread("./test/00434.jpg") # Funciona


contrast_img = cv2.addWeighted(imagen, 2.5, np.zeros(imagen.shape, imagen.dtype), 0, 0)
imagenhsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
cv2.imshow('original',imagen)
cv2.imshow('conContraste',contrast_img)
cannyImagen2 = cv2.Canny(imagen,200,300)
cv2.imshow('COriginal',cannyImagen2)

rojo_bajo = np.array([0, 80, 40])
rojo_alto = np.array([10, 255, 255])
rojo_bajo2 = np.array([160, 50, 45])
rojo_alto2 = np.array([186, 255, 255])

mascara1 = cv2.inRange(imagenhsv, rojo_bajo, rojo_alto)
mascara2 = cv2.inRange(imagenhsv, rojo_bajo2, rojo_alto2)
mascaraFinal = cv2.add(mascara1,mascara2)

blurred = cv2.blur(mascaraFinal, (9, 9))

ret, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
canny = cv2.Canny(closed,200,300)
#erode = cv2.erode(closed, None, iterations=4)
#dilate = cv2.dilate(erode, None, iterations=4)

contours, hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
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



##Prueba circulos
cimg = imagen.copy()
circulo = cv2.HoughCircles(binary,cv2.HOUGH_GRADIENT,2,30,param1=80,param2=20,minRadius=10,maxRadius=40)
circuloA = cv2.HoughCircles
circulo = np.uint16(np.around(circulo))
for i in circulo[0,:]:
    # Dibuja la circusnferencia del círculo
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # dibuja el centro del círculo
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('circulos',cimg)
cv2.imshow('res', res)
cv2.imshow('hsv', imagenhsv)
cv2.imshow('threshold',binary)
cv2.imshow('closed', closed)
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