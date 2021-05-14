#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
from mejoradeimagen import *

imagen = cv2.imread("./train_recortadas/01/00000.ppm")
imagen = cv2.imread("./train_10_ejemplos/00003.ppm")
imagen = cv2.imread("./test/00431.jpg")
imagen = cv2.imread("./20201003121440748.jpg")



#imagen=cv2.medianBlur(imagen,5)
contrast_img = cv2.addWeighted(imagen, 2.5, np.zeros(imagen.shape, imagen.dtype), 0, 0)

imagenhsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
redDer, imagenBinaria = mascararojo(imagenhsv)


salMSER = hacedordeMSER(imagenBinaria)
if salMSER is not None:
    result = salMSER.copy()
    result2 = imagen.copy()
    cv2.imshow("MSER",salMSER)

    contornos, jerarquia = cv2.findContours(imagenBinaria.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print( len(contornos))
    if len(contornos) > 0:

        recorteCorrelarSignals(contornos, result, result2, imagen,"mser")






