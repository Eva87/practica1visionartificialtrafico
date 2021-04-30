# comando de Jupyter para que las imagenes se muestren automaticamente
#%matplotlib inline

#numpy es la libreria de arreglos de python (la llamaremos np)
import cv2
import numpy as np

# el modulo pyplot de matplotlib (que llamaremos plt) nos permite mostrar imagenes
import matplotlib.pyplot as plt
#el modulo matplotlib.colors nos permite transformar el espacio de color de una imagen
import matplotlib.colors
# el mapa de color para las imágenes escala de grises es el gris
plt.rcParams['image.cmap'] = 'gray'


#el modulo io de skimage sirve para cargar y guardar imagenes
from skimage import io

# leemos la imagen desde un archivo, y la almacenamos en memoria en un arreglo
image = io.imread("./test/00400.jpg")
#image = plt.imread("00002.ppm")


image33 = cv2.imread("./test/00400.jpg", 0)
if cv2.countNonZero(image33) == 0:
    print ("Image is black")
else:
    print ("Colored image")




#Esto aclara la imagen

hist,bins=np.histogram(image.flatten(),256,[0,256])
cdf=hist.cumsum()

# Enmascara los valores iguales a cero
cdf_m = np.ma.masked_equal(cdf, 0)

# Aplica la transformación de ecualización
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())

# Rellena los valores previamente enmascarados con ceros
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

# Aplica la ecualización a los píxeles de la imagen original
img2 = cdf[image]

# Grafica la imagen resultante de aplicar la ecualización del histograma
cv2.imshow('image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

image=img2




#Esto es el del tio de las manos indice.jpg









# Convertimos la imagen de entero a flotante, y además convertimos el rango de los pixeles
# de 0-255 (entero) al rango 0-1 (flotante)
image=image/255.

#imprimimos las tres dimensiones del arreglo: las dos primeras corresponden al alto y ancho,
#la última a los canales de color (3 canales, por defecto RGB)
print("Dimensiones de la imagen: %s" % str(image.shape))

#guardamos las dimensiones en tres variables para usar en las celdas más abajo
h,w,c=image.shape

#mostramos el tipo de los elementos del arreglo (debería ser flotante!)
print("Tipo de los elementos de la imagen: %s" % str(image.dtype))

#visualizamos la imagen
plt.imshow(image)
#plt.show()

#Vemos los canales individuales de RGB.
#El fondo blanco activa los 4 canales (R,G y B)
# El buzo y el pelo, al ser negro oscuro, no se activan en ningún canal
# Por otro lado, el guante rojo se activa en el canal rojo y no en los otros dos
# Y el guante verde se activa en los canales verde (mayormente) y azul

#Anulo los canales rojo y azul para ver solo el verde
green=np.copy(image)
green[:,:,0]=0
green[:,:,2]=0
plt.figure()
plt.imshow(green)
#plt.show()

#Anulo los canales azul y verde para ver solo el rojo
red=np.copy(image)
red[:,:,1:3]=0
plt.figure()
plt.imshow(red)
#plt.show()

#Anulo los canales rojo y verde para ver solo el azul
blue=np.copy(image)
blue[:,:,0:2]=0
plt.figure()
plt.imshow(blue)
#plt.show()

# Convertir a modelo HSV
image_hsv=matplotlib.colors.rgb_to_hsv(image)
#image_hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

print("El pixel de la posición (100,100) se codifica en RGB como %s " % str(image[100,100,:]))
print("El pixel de la posición (100,100) se codifica en HSV como %s " % str(image_hsv[100,100,:]))





#Vemos los canales individuales de HSV.

plt.figure()
plt.imshow(image_hsv[:,:,0])
plt.colorbar()

plt.figure()
plt.imshow(image_hsv[:,:,1])
plt.colorbar()

plt.figure()
plt.imshow(image_hsv[:,:,2])
plt.colorbar()



#Rango de colores a utilizar

#guante rojo
h_min,h_max=(230/255,250/255)
s_min,s_max=(100/255,230/255)
v_min,v_max=(50/255,170/255)




# Filtrar por color para buscar el guante

h,w,c=image_hsv.shape
segmentation_mask=np.zeros((h,w))

for i in range(h):#evitamos los bordes
    for j in range(w): #evitamos los bordes
        h_val,s_val,v_val=image_hsv[i,j,:]
        #IMPLEMENTAR
        #Si los valores están en rango, poner en 1 la coordenada (i,j) de la máscara de segm


plt.imshow(segmentation_mask,vmin=0,vmax=1)





eroded_mask=np.zeros(segmentation_mask.shape) # creamos otra imagen con la misma forma que la mascara de seg.

# erosionar la mascara
for i in range(1,h-1):#evitamos los bordes
    for j in range(1,w-1): #evitamos los bordes
        #IMPLEMENTAR
        #Contar cuantos pixeles blancos hay entre entre el pixel (i,j)
        #y sus vecinos inmediatos
        pass

plt.imshow(eroded_mask,vmin=0,vmax=1)


# erosionar la mascara de filtro
coordinate_sum=np.array([0,0])
count=0
for i in range(h):
    for j in range(w):
        # IMPLEMENTAR
        # Si el pixel (i,j) pertenece al guante, sumar dicha coordenada a la suma total
        pass

red_glove_position=np.array([0,0]) # IMPLEMENTAR
print("Las coordenadas del centro de la mano con el guante rojo son:")
print(red_glove_position)




import matplotlib.patches as patches

def dibujar_cuadrado(position):
    size=70
    canvas = plt.gca()
    size_x,size_y=(size,size)
    position_reversed=(position[1]-size_y/2,position[0]-size_x/2)
    rectangle=patches.Rectangle(position_reversed, size_x,size_y, fill=True)
    canvas.add_patch(rectangle)

plt.imshow(image)
dibujar_cuadrado(red_glove_position)


def erode(segmentation_mask):
    # IMPLEMENTAR
    return 0  # retornar mascara de segmentacion erosionada


def segment_by_color(image_hsv, h_min, h_max, s_min, s_max, v_min, v_max):
    # IMPLEMENTAR
    return 0  # retornar mascara de segmentacion


def calculate_mass_center(segmentation_mask):
    # IMPLEMENTAR
    return np.array([0, 0])  # retornar posicion


def locate_object(image_rgb, h_min, h_max, s_min, s_max, v_min, v_max):
    # convertir la imagen de rgb a hsv
    # IMPLEMENTAR

    # generar la máscara de segmentación en base al color
    # IMPLEMENTAR

    # erosionar la máscara
    # IMPLEMENTAR

    # calcular centro de masa de la máscara para encontrar la posición del objeto
    # IMPLEMENTAR

    return np.array([0, 0])  # retornar posición


h_min, h_max = (0 / 255, 0 / 255)
s_min, s_max = (0 / 255, 0 / 255)
v_min, v_max = (0 / 255, 0 / 255)

green_glove_position = locate_object(image, h_min, h_max, s_min, s_max, v_min, v_max)
print(green_glove_position)  # debería imprimir algo similar a [1150,580]
plt.imshow(image)
dibujar_cuadrado(green_glove_position)



plt.show()