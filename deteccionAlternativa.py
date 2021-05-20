# Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
import glob
import cv2
import procesadoImagen
import numpy as np


class alternativa:

    def Alternativa(strinentradaimg):
        imagen = cv2.imread(strinentradaimg)
        contrast_img = cv2.addWeighted(imagen, 2.5, np.zeros(imagen.shape, imagen.dtype), 0, 0)
        imagenhsv = cv2.cvtColor(contrast_img, cv2.COLOR_BGR2HSV)
        (cannybordes, cerradoimagen) = procesadoImagen.filtradorojoDifuminarNucleoCerradoCanny(imagenhsv)
        contornos, hierarchy = cv2.findContours(cerradoimagen.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contornos) > 0:
            procesadoImagen.recorteCorrelarSignals(contornos, imagen.copy(), imagen, "Alternativa", strinentradaimg)
        # cv2.waitKey(0)

        return ()
