#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
from procesadoImagen import *
import glob


for strinentradaimg in sorted (glob.glob("./train_10_ejemplos/*")):
    finnombre = strinentradaimg[-3:]
    for strinentradaim in sorted(glob.glob(strinentradaimg)):
        if finnombre !="txt" and (finnombre=="jpg" or finnombre=="ppm"):
            imagen = cv2.imread(strinentradaimg)

            img_to_yuv = cv2.cvtColor(imagen, cv2.COLOR_BGR2YUV)
            img_to_yuv[:, :, 0] = cv2.equalizeHist(img_to_yuv[:, :, 0])
            hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
            equGris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
            imagenhsv = cv2.cvtColor(hist_equalization_result, cv2.COLOR_BGR2HSV)
            (cannybordes, cerradoimagen) = filtradorojoDifuminarNucleoCerradoCanny(imagenhsv)
            contornos, jerarquia = cv2.findContours(cannybordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(contornos) > 0:
                salMSER = hacedordeMSER(cannybordes)
                if salMSER is not None:
                    recorteCorrelarSignals(contornos, imagen.copy(), imagen, "MSER", strinentradaimg)



#cv2.waitKey(0)