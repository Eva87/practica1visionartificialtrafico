import cv2
import numpy as np

imagen = cv2.imread("./test/00575.jpg")
imagen = cv2.imread("./test/00411.jpg")
imagen = cv2.imread("./test/00420.jpg")
imagen = cv2.imread("./test/00403.jpg")
imagen = cv2.imread("./test/00482.jpg")


imagenhsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)



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
erode = cv2.erode(closed, None, iterations=4)
dilate = cv2.dilate(erode, None, iterations=4)




cv2.imshow('hsv', imagenhsv)
cv2.imshow('closed', closed)
cv2.imshow('erode', erode)
cv2.imshow('dilate', dilate)
cv2.waitKey(0)

#Ideas
# 1-pasar a hsv
# 2-threshold
# 3-redthreshold
# 4-canny
# 5-findcontours
# 6-detectar si es triangulo....¿?
# 7-sacar los puntos de la ubicacion