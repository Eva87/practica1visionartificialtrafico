#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
#pip install opencv-contrib-python
import glob
from procesadoImagen import *


for strinentradaimg in sorted (glob.glob("./train_10_ejemplos/*")):
    finnombre = strinentradaimg[-3:]
    for strinentradaim in sorted(glob.glob(strinentradaimg)):
        if finnombre !="txt" and (finnombre=="jpg" or finnombre=="ppm"):
            imagen = cv2.imread(strinentradaimg)
            contrast_img = cv2.addWeighted(imagen, 2.5, np.zeros(imagen.shape, imagen.dtype), 0, 0)
            imagenhsv = cv2.cvtColor(contrast_img, cv2.COLOR_BGR2HSV)
            (cannybordes, cerradoimagen) = filtradorojoDifuminarNucleoCerradoCanny(imagenhsv)
            contornos, jerarquia = cv2.findContours(cannybordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(contornos) > 0:
                salMSER = hacedordeMSER(cannybordes)
                if salMSER is not None:
                    recorteCorrelarSignals(contornos,imagen.copy(), imagen, "AlternativaMSER", strinentradaimg)



#cv2.waitKey(0)
'''
como usar el main.py
            
preguntar profe si que en la salida ponemos de que algoritmo sale para las imagenes
'''