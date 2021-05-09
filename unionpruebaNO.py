import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import random
from colorsys import hsv_to_rgb

imagen = cv2.imread("./train/00141.ppm")
imagen = cv2.imread("./test/00575.jpg")
imagenH = cv2.imread("./train/00141.ppm", cv2.IMREAD_GRAYSCALE)
imagen = cv2.imread("./test/00411.jpg")
imagen = cv2.imread("./test/00420.jpg")
imagen = cv2.imread("./test/00403.jpg")
imagen = cv2.imread("./test/00482.jpg")
imagen = cv2.imread("./test/00434.jpg")  # Funciona

imagenescalagrises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

##Prueba circulos
cimg = imagen.copy()
circulo = cv2.HoughCircles(imagenescalagrises, cv2.HOUGH_GRADIENT, 2, 30, param1=80, param2=20, minRadius=10,
                           maxRadius=40)
circuloA = cv2.HoughCircles
circulo = np.uint16(np.around(circulo))
for i in circulo[0, :]:
    # Dibuja la circusnferencia del círculo
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # dibuja el centro del círculo
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

ret, binary = cv2.threshold(cimg, 127, 255, cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
canny = cv2.Canny(closed, 200, 300)

'''
    imu = ((canny > 100) * 255).astype(np.uint8)
    # MSER
    output = np.zeros((imu.shape[0], imu.shape[1], 3), dtype=np.uint8)
    mser = cv2.MSER_create(_delta=5, _max_variation=0.5, _max_area=20000)
    polygons = mser.detectRegions(imu)
    for polygon in polygons[0]:
        colorRGB = hsv_to_rgb(random(), 1, 1)
        colorRGB = tuple(int(color * 255) for color in colorRGB)
        output = cv2.fillPoly(output, [polygon], colorRGB)

    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)  # Convertimos la imagen a escala de grises.
    keypoints = mser.detect(gray, None)
    for keypoint in keypoints:
        radius = int(0.5 * keypoint.size)
        x, y = np.int64(keypoint.pt)
        cv2.circle(imagen, (x, y), radius, (0, 255, 255), 2)



rojo_bajo = np.array([0, 80, 40])
rojo_alto = np.array([10, 255, 255])
rojo_bajo2 = np.array([160, 50, 45])
rojo_alto2 = np.array([186, 255, 255])

mascara1 = cv2.inRange(output, rojo_bajo, rojo_alto)
mascara2 = cv2.inRange(output, rojo_bajo2, rojo_alto2)
mascaraFinal = cv2.add(mascara1, mascara2)

blurred = cv2.blur(mascaraFinal, (9, 9))

'''

arrayprohibido = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 0, 0, 0, 0, 0],
                          [0, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 0, 0, 0, 0],
                          [0, 0, 0, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 0, 0, 0],
                          [0, 0, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0],
                          [0, 0, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 0, 0],
                          [0, 0, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0],
                          [0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0],
                          [0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0],
                          [0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0],
                          [0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0],
                          [0, 0, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 0, 0],
                          [0, 0, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 0, 0],
                          [0, 0, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 0, 0, 0],
                          [0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 0],
                          [0, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0],
                          [0, 0, 0, 0, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

cv2.imshow('circulos', canny)
cv2.imshow('imagen', imagen)
cv2.waitKey(0)
