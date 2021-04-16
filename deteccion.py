#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín

import cv2
import scipy
from matplotlib import pyplot as plt
import numpy as np
img=cv2.imread("./test/00401.jpg") # No se ve un pimiento, es super oscura ¿aclararla?
#img=cv2.imread("./test/00423.jpg")
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#plt.show()
#esto aclara la imagen
im=img/64.0
m_power_law_transformation = cv2.pow (im, 0.6)
#cv2.imshow ('Original Image', im)
#cv2.imshow ('Power Transformación de ley ', im)
#cv2.waitKey (0)


# aqui buscaremos color rojo
# un color no es un unico numero asique vamos a poner un rango 100, 200 .... cuantos
#RGB rojo el primero pero el rango tiene que incluir parte de verde y azul, pq tb hay rojos con parte de estos
# pero cuanto
#https://omes-va.com/deteccion-de-colores/
#en esa pagina si no lo saco viene
rango_parte_inferior_bajo = np.array([0,100,20], np.uint8)
rango_parte_superior_bajo =  np.array([8,255,255], np.uint8)
rango_parte_inferior_alto =  np.array([175,100,20], np.uint8)
rango_parte_superior_alto = np.array([179,255,255], np.uint8)

