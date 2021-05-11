
import cv2
import numpy as np
from random import random
from colorsys import hsv_to_rgb
from matplotlib import pyplot as plt

# el modulo pyplot de matplotlib (que llamaremos plt) nos permite mostrar imagenes
import matplotlib.pyplot as plt
#el modulo matplotlib.colors nos permite transformar el espacio de color de una imagen
import matplotlib.colors

#mmmm https://unipython.com/umbralizacion-una-imagen/ aqui quizas aparezca algo

imagenoscura = cv2.imread("./test/00400.jpg",1)
imagenclara = cv2.imread("./test/00597.jpg",1)
imagenclara = cv2.imread("./test/00464.jpg",1)
imagenclara = cv2.imread("./test/00482.jpg",1)
imagenclarabyn = cv2.imread("./test/00482.jpg", cv2.IMREAD_GRAYSCALE)
imagenoscurabyn = cv2.imread("./test/00400.jpg", cv2.IMREAD_GRAYSCALE)




img_med = cv2.adaptiveThreshold(imagenclarabyn,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,15)
img_gauss = cv2.adaptiveThreshold(imagenclarabyn,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,15)
plt.imshow(imagenclarabyn,'gray');plt.title("Original");plt.show()
plt.imshow(img_med,'gray');plt.title("Adaptativo 21 media-15");plt.show()
plt.imshow(img_gauss,'gray');plt.title("Adaptativo 21 Gausiana-15");plt.show()




cv2.imshow(cv2.circle(imagenclara, None, None, "red"))



cv2.waitKey(0)






'''import argparse

max_value = 255
max_value_H = 360 // 2
low_H = 0
low_S = 0
low_V = 0
high_H = max_value_H
high_S = max_value
high_V = max_value
window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'


def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H - 1, low_H)
    cv2.setTrackbarPos(low_H_name, window_detection_name, low_H)


def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H + 1)
    cv2.setTrackbarPos(high_H_name, window_detection_name, high_H)


def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S - 1, low_S)
    cv2.setTrackbarPos(low_S_name, window_detection_name, low_S)


def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S + 1)
    cv2.setTrackbarPos(high_S_name, window_detection_name, high_S)


def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V - 1, low_V)
    cv2.setTrackbarPos(low_V_name, window_detection_name, low_V)


def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V + 1)
    cv2.setTrackbarPos(high_V_name, window_detection_name, high_V)


parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
args = parser.parse_args()
cap = cv2.VideoCapture(args.camera)
cv2.namedWindow(window_capture_name)
cv2.namedWindow(window_detection_name)
cv2.createTrackbar(low_H_name, window_detection_name, low_H, max_value_H, on_low_H_thresh_trackbar)
cv2.createTrackbar(high_H_name, window_detection_name, high_H, max_value_H, on_high_H_thresh_trackbar)
cv2.createTrackbar(low_S_name, window_detection_name, low_S, max_value, on_low_S_thresh_trackbar)
cv2.createTrackbar(high_S_name, window_detection_name, high_S, max_value, on_high_S_thresh_trackbar)
cv2.createTrackbar(low_V_name, window_detection_name, low_V, max_value, on_low_V_thresh_trackbar)
cv2.createTrackbar(high_V_name, window_detection_name, high_V, max_value, on_high_V_thresh_trackbar)
while True:

    ret, frame = cap.read()
    if frame is None:
        break
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_threshold = cv2.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))

    cv2.imshow(window_capture_name, frame)
    cv2.imshow(window_detection_name, frame_threshold)

    key = cv2.waitKey(30)
    if key == ord('q') or key == 27:
        break



cv2.waitKey(0)


'''





















'''
histogramaoscuro=cv2.calcHist([imagenoscura],[0], None,[256],[0,256])
histogramaclaro=cv2.calcHist([imagenclara],[0], None,[256],[0,256])

plt.subplot(2, 2, 1)
plt.plot(histogramaoscuro, 'gray')
plt.subplot(2, 2, 3)
plt.plot(histogramaclaro, 'gray')'''










'''imagenclarahsv=cv2.cvtColor(imagenclara, cv2.COLOR_BGR2HSV)
hclara,sclara,vclara=cv2.split(imagenclarahsv)

imagenoscurahsv=cv2.cvtColor(imagenoscura, cv2.COLOR_BGR2HSV)
hoscura,oscura,voscura=cv2.split(imagenoscurahsv)

print("VCLARA", vclara)
print("VOSCURA", voscura)'''
'''
if cv2.countNonZero(imagenoscura) == 0:
    print ("imagenoscura is black")
else:
    print ("Colored imagenoscura")

if cv2.countNonZero(imagenclara) == 0:
    print ("imagenclara is black")
else:
    print ("Colored imagenclara")'''



'''
from matplotlib import pyplot as plt

ret, thresh1 = cv2.threshold(imagenclara, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(imagenclara, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(imagenclara, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(imagenclara, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(imagenclara, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [imagenclara, thresh1, thresh2, thresh3, thresh4, thresh5]
miArray = np.arange(6)
for i in miArray:
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()


ret1, thresh11 = cv2.threshold(imagenoscura, 127, 255, cv2.THRESH_BINARY)
ret1, thresh12 = cv2.threshold(imagenoscura, 127, 255, cv2.THRESH_BINARY_INV)
ret1, thresh13 = cv2.threshold(imagenoscura, 127, 255, cv2.THRESH_TRUNC)
ret1, thresh14 = cv2.threshold(imagenoscura, 127, 255, cv2.THRESH_TOZERO)
ret1, thresh15 = cv2.threshold(imagenoscura, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [imagenoscura, thresh11, thresh12, thresh13, thresh14, thresh15]
miArray = np.arange(6)
for i in miArray:
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])'''

plt.show()