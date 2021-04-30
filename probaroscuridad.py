
import cv2
import numpy as np

# el modulo pyplot de matplotlib (que llamaremos plt) nos permite mostrar imagenes
import matplotlib.pyplot as plt
#el modulo matplotlib.colors nos permite transformar el espacio de color de una imagen
import matplotlib.colors

#mmmm https://unipython.com/umbralizacion-una-imagen/ aqui quizas aparezca algo

imagenoscura = cv2.imread("./test/00400.jpg",1)
imagenclara = cv2.imread("./test/00482.jpg",1)

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
    plt.xticks([]), plt.yticks([])

plt.show()