#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín

#pip install opencv-contrib-python

import cv2
import sklearn
from matplotlib import pyplot as plt
import numpy as np
#img=cv2.imread("./test/00401.jpg") # No se ve un pimiento, es super oscura ¿aclararla?
#img=cv2.imread("./test/00423.jpg")
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#plt.show()
#esto aclara la imagen
#m_power_law_transformation = cv2.pow (im, 0.6)
#cv2.imshow ('Original Image', img)
#cv2.imshow ('Power Transformación de ley ', im)
#cv2.waitKey (0)
# aqui buscaremos color rojo
# un color no es un unico numero asique vamos a poner un rango 100, 200 .... cuantos
#RGB rojo el primero pero el rango tiene que incluir parte de verde y azul, pq tb hay rojos con parte de estos
# pero cuanto
#https://omes-va.com/deteccion-de-colores/
#en esa pagina si no lo saco viene
#rango_parte_inferior_bajo = np.array([0,100,20], np.uint8)
#rango_parte_superior_bajo =  np.array([8,255,255], np.uint8)
#rango_parte_inferior_alto =  np.array([175,100,20], np.uint8)
#rango_parte_superior_alto = np.array([179,255,255], np.uint8)
#Establecemos el rango mínimo y máximo de (Blue, Green, Red):
#OpenCV utiliza el espacio de color BGR en vez de RGB (es decir, invierte el orden de las componentes R y B)
#rojo_bajos = np.array([0,111,255])
#rojo_altos = np.array([0, 0, 113])
# Detectamos los píxeles que estén dentro del rango que hemos establecido:
#mask = cv2.inRange(im, rojo_bajos, rojo_altos)
#Mostramos la imagen original y la máscara:
#cv2.imshow("Original", im)
#cv2.imshow("Rojo", mask)
from random import random
from colorsys import hsv_to_rgb
from matplotlib import pyplot as plt
from PIL import Image
img=cv2.imread("./test/00482.jpg", 0)
#inicializamos la imagen RGB a niveles de gris
img2 = cv2.imread("./test/00482.jpg", cv2.IMREAD_GRAYSCALE)

imagencolor = cv2.imread("./train_recortadas/01/00411.jpg")
imagenbyn = cv2.imread("./train_recortadas/01/00411.jpg", cv2.IMREAD_GRAYSCALE)

'''
imagencolor = cv2.imread("./test/00482.jpg", cv2.IMREAD_COLOR)
imagenbyn = cv2.imread("./test/00482.jpg", cv2.IMREAD_GRAYSCALE)
''''''
imagencolor = cv2.imread("./test/00400.jpg", cv2.IMREAD_COLOR)
#inicializamos la imagen RGB a niveles de gris
imagenbyn = cv2.imread("./test/00400.jpg", cv2.IMREAD_GRAYSCALE)
'''

#inicializamos la imagen sin cambios incluyendo el canal alfa
imagensincambios = cv2.imread("./test/00482.jpg", cv2.IMREAD_UNCHANGED)
imgsinparametros = cv2.imread("./test/00482.jpg")

imagenengris=cv2.cvtColor(imagencolor,cv2.COLOR_RGB2GRAY)
yuvimagen=cv2.cvtColor(imagencolor, cv2.COLOR_BGR2YUV)
hsvimagen=cv2.cvtColor(imagencolor, cv2.COLOR_BGR2HSV)
y,u,v = cv2.split(yuvimagen)



'''b=u+y
r=u+y
g=(y-0.2992-(0.114*b))/0.587'''
'''r=(v/0.877)+y
b=(u/0.492)+y
g=(y-(0.299*r)-(0.114*b))/0.587'''
'''
b=(1.164*(y-16))+(2.018*(u-128))
g=(1.164*(y-16))-(0.813*(v-128))-(0.391*(u-128))
r=(1.164*(y-16))+(1.596*(v-128))'''



b=(y+u)/2.029
r=(y+v)
g=y-(0.396*u)-(0.581*v)



'''
arraytamanio25=[]
filas=25
columnas=25
for i in range (filas):
    fila=[]
    for j in range(columnas):
        fila.append(j)
    arraytamanio25.append(fila)
print(arraytamanio25)

rango_parte_inferior_bajo = np.array([0,0,50], np.uint8)
print(rango_parte_inferior_bajo)
rango_parte_superior_bajo = np.array([10,255,255], np.uint8)
rango_parte_inferior_alto = np.array([150,0,50], np.uint8)
rango_parte_superior_alto = np.array([200,255,255], np.uint8)
maskrojo1=cv2.inRange(hsvimagen, rango_parte_inferior_bajo, rango_parte_inferior_alto)
maskrojo2=cv2.inRange(hsvimagen, rango_parte_superior_bajo, rango_parte_superior_alto)
mascararojo=cv2.add(maskrojo1,maskrojo2)
mascararojovis=cv2.bitwise_and(imagencolor,imagencolor,mask=mascararojo)
cv2.imshow('mascararojo', mascararojo)
cv2.imshow('mascararojovis', mascararojovis)


pil_imagen=Image.fromarray(imagencolor)
plt.imshow(pil_imagen)'''



'''r=imagencolor[:,:,1]=0
g=imagencolor[:,:,2]=0
b=imagencolor[:,:,0]=0'''



'''
plt.subplot(2,2,1)
plt.imshow(imagencolor[:,:,0],vmin=0,vmax=0)
plt.subplot(2,2,2)
plt.imshow(imagencolor[:,:,1],vmin=0,vmax=0)
plt.subplot(2,2,3)
plt.imshow(imagencolor[:,:,2],vmin=0,vmax=0)
plt.show()'''



'''
histograma=cv2.calcHist([imagenbyn],[0], None,[256],[0,256])
plt.plot(histograma, color='gray')
plt.xlabel('intendidad de la iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()
'''



'''color = ('b','g','r')
#recorrido por cada canal
for i, c in enumerate(color):
    '''  '''
    cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]
    1.-images: imagen de estrada, puede ser a escala de grises o colores.
    2- channels: índice de canal para el cual deseamos calcular el histograma,
    en una imagen a escala de grises [0],
    si la imagen es a colores podemos indicar [0], [1], [2] para los canales B,
    G, R respectivamente.
    3.-mask: mascara que dene la región sobre la que deseamos calcular el histograma,
    es opcional.
    4.-histSize: intensidad máxima, para nosotros [256].
    5.-ranges: nuestro rango de valores, usaremos [0, 256]
    '''  '''
    hist = cv2.calcHist([imagencolor], [i], None, [256], [0, 256])
    #color = c
    plt.plot(hist, color = c)
    #establece límites x de los ejes actuales
    plt.xlim([0,256])
#muestra el histograma
plt.show()'''
'''
img = cv2.equalizeHist(img)
cv2.imshow('Histogramas', img)
cv2.waitKey()
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
'''



#Los histogramas por color y el histograma en blanco y negro
bhist = cv2.calcHist([imagencolor], [0], None, [256], [0, 256])
ghist = cv2.calcHist([imagencolor], [1], None, [256], [0, 256])
rhist = cv2.calcHist([imagencolor], [2], None, [256], [0, 256])
khist = cv2.equalizeHist(imagenbyn-5)
plt.subplot(3,2,1)
plt.plot(ghist, color = 'g')
plt.subplot(3,2,2)
plt.plot(rhist, color = 'r')
plt.subplot(3,2,3)
plt.plot(bhist, color = 'b')
plt.subplot(3,2,4)
plt.plot(khist, color = 'k')
plt.show()




image2 = np.uint8(255.0 * (img - img.min()) / (img.max() - img.min()))
print('nivel de brillo máximo = ', img.max())
print('nivel de brillo mìnimo = ', img.min())
# umbralización
# imagen oscura 20 y imagen clara 100
#if img.max()
imu = ((img2 >100)*255).astype(np.uint8)
#MSER
output = np.zeros((imu.shape[0],imu.shape[1],3),dtype=np.uint8)
mser = cv2.MSER_create(_delta=5,_max_variation=0.5,_max_area=20000)
polygons = mser.detectRegions(imu)
for polygon in polygons[0]:
    colorRGB = hsv_to_rgb(random(),1,1)
    colorRGB = tuple(int(color*255) for color in colorRGB)
    output = cv2.fillPoly(output,[polygon],colorRGB)



#cv2.imshow("foto", image2,  vmin=0, vmax=255)
'''cv2.imshow("y=0.2992+0.587G+0.114B", y)
cv2.imshow("u=B-Y", u)
cv2.imshow("v=R-Y", v)

cv2.imshow("b", b)
cv2.imshow("r", r)
cv2.imshow("g", g)

cv2.imshow("foto2", imu)
cv2.imshow("foto3", output)'''
cv2.waitKey(0)