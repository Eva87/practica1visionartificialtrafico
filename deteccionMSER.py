#Proyecto creado por Eva María Hoyo de la Cruz, TongTong Xu y Antonio Francisco Roldan Martín
from mejoradeimagen import *
import glob

for strinentradaimg in sorted (glob.glob("./test2/*")):
    finnombre = strinentradaimg[-3:]
    for strinentradaim in sorted(glob.glob(strinentradaimg)):
        if finnombre !="txt" and (finnombre=="jpg" or finnombre=="ppm"):
            imagen = cv2.imread(strinentradaimg)

            img_to_yuv = cv2.cvtColor(imagen, cv2.COLOR_BGR2YUV)
            img_to_yuv[:, :, 0] = cv2.equalizeHist(img_to_yuv[:, :, 0])
            hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
            cv2.imshow("Equalizada",hist_equalization_result)
            equGris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
            cv2.imshow("Gris",equGris)

            salMSER, poligono = hacedordeMSER(equGris)
            '''# MSER
            output = np.zeros((equGris.shape[0], equGris.shape[1], 3), dtype=np.uint8)
            mser = cv2.MSER_create(_delta=5, _max_variation=0.50, _max_area=2000,_min_area=200)
            polygons = mser.detectRegions(equGris)
            for polygon in polygons[0]:
                colorRGB = hsv_to_rgb(random(), 1, 1)
                colorRGB = tuple(int(color * 255) for color in colorRGB)
                output = cv2.fillPoly(output, [polygon], colorRGB)'''

            imagenhsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
            (cannybordes, cerradoimagen) = filtradorojoDifuminarNucleoCerradoCanny(salMSER)
            contornos, jerarquia = cv2.findContours(cannybordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(contornos) > 0:
                if salMSER is not None:
                    result = salMSER.copy()
                    result2 = imagen.copy()
                    recorteCorrelarSignals(contornos, result, result2, imagen, "MSER", strinentradaimg)



