# Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
# pip install opencv-contrib-python
import glob
import cv2
import procesadoImagen
import numpy as np


class alternativaMSER:

    def AlternativaMSER(strinentradaimg):
        imagen = cv2.imread(strinentradaimg)
        contrast_img = cv2.addWeighted(imagen, 2.5, np.zeros(imagen.shape, imagen.dtype), 0, 0)
        imagenhsv = cv2.cvtColor(contrast_img, cv2.COLOR_BGR2HSV)
        (cannybordes, cerradoimagen) = procesadoImagen.filtradorojoDifuminarNucleoCerradoCanny(imagenhsv)
        contornos, jerarquia = cv2.findContours(cannybordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contornos) > 0:
            salMSER = procesadoImagen.hacedordeMSER(cannybordes)
            if salMSER is not None:
                procesadoImagen.recorteCorrelarSignals(contornos, imagen.copy(), imagen, "AlternativaMSER", strinentradaimg)

        # cv2.waitKey(0)

        return ()
