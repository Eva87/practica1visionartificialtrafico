#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
#pip install opencv-contrib-python
import glob
import cv2
from mejoradeimagen import *

for strinentradaimg in sorted (glob.glob("./train_10_ejemplos/*")):
    #for strinentradai in strinentradaimg(sorted(glob.glob("./train_10_ejemplos/*")):

    finnombre = strinentradaimg[-3:]
    #if finnombre !="txt" or finnombre!="jpg"or finnombre!="ppm":

    for strinentradaim in sorted(glob.glob(strinentradaimg)):
        if finnombre !="txt" and (finnombre=="jpg" or finnombre=="ppm"):
            imagen = cv2.imread(strinentradaimg)



            '''
            quizas se pueda probar en alguno 
            img_med = cv2.adaptiveThreshold(imagenclarabyn, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 15)
            img_gauss = cv2.adaptiveThreshold(imagenclarabyn, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21,
                                              15)
            '''





            imagenhsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
            (cannybordes, cerradoimagen) = filtradorojoDifuminarNucleoCerradoCanny(imagenhsv)
            contornos, jerarquia = cv2.findContours(cannybordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(contornos) > 0:
                salMSER = hacedordeMSER(cannybordes)
                if salMSER is not None:
                    result = salMSER.copy()
                    result2 = imagen.copy()
                    recorteCorrelarSignals(contornos, result, result2, imagen, "Alternativa con MSER", strinentradaimg)

            '''
            como usar el main.py
            '''

cv2.waitKey(0)