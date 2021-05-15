#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
import glob
from mejoradeimagen import *

for strinentradaimg in sorted (glob.glob("./train_10_ejemplos/*")):
    #for strinentradai in strinentradaimg(sorted(glob.glob("./train_10_ejemplos/*")):

    finnombre = strinentradaimg[-3:]
    if finnombre !="txt" and (finnombre=="jpg" or finnombre=="ppm"):
        imagen = cv2.imread(strinentradaimg)
        contrast_img = cv2.addWeighted(imagen, 2.5, np.zeros(imagen.shape, imagen.dtype), 0, 0)
        imagenhsv = cv2.cvtColor(contrast_img, cv2.COLOR_BGR2HSV)

        (cannybordes, cerradoimagen)=filtradorojoDifuminarNucleoCerradoCanny(imagenhsv)

        contornos, hierarchy = cv2.findContours(cerradoimagen.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        image = cv2.findContours(cerradoimagen.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contornos) > 0:
            result2 = imagen.copy()
            recorteCorrelarSignals(contornos, result2, result2, imagen, "Alternativa", strinentradaimg)
