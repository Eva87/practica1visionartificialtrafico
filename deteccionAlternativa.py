#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
from mejoradeimagen import *


for i in range (500,550):
    strinentradaimg="./test/00"+str(i)+".jpg"
    imagen = cv2.imread(strinentradaimg)
    #contrast_img = cv2.addWeighted(imagen, 2.5, np.zeros(imagen.shape, imagen.dtype), 0, 0)
    imagenhsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

    (cannybordes, cerradoimagen)=filtradorojoDifuminarNucleoCerradoCanny(imagenhsv)

    contornos, hierarchy = cv2.findContours(cerradoimagen.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    image = cv2.findContours(cerradoimagen.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contornos) > 0:
        result2 = imagen.copy()
        recorteCorrelarSignals(contornos, result2, result2, imagen, "Alternativa", strinentradaimg)



