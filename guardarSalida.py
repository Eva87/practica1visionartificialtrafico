from datetime import datetime
import cv2


def guardarcarpetasyfichero(nomiment, p1, p2, p3, p4, sennal, puntuacion):
    ficherosalida = open("salida.txt", "a", encoding="utf-8")
    ficherosalida.write(str(nomiment) + ", " + str(p1) + ", " + str(p2) + ", " + str(p3) + ", " + str(p4) + ", " + str(
        sennal) + ", " + str(puntuacion) + "\n")
    ficherosalida.close()
    return ()


def guardarimagencarpeta(imagensalida, variablesenl, orig, nomimageent):
    cadenasalidaimagen = str(datetime.now().strftime("%d%m%Y%H%M%S%f"))
    nomsal = nomimageent[7:12]
    if variablesenl == 3:
        cadenasalidaimagen = "./stop/" + orig + nomsal + "stop" + cadenasalidaimagen + ".jpg"
    elif variablesenl == 1:
        cadenasalidaimagen = "./prohibido/" + orig + nomsal + "prohibido" + cadenasalidaimagen + ".jpg"
    elif variablesenl == 2:
        cadenasalidaimagen = "./peligro/" + orig + nomsal + "peligro" + cadenasalidaimagen + ".jpg"
    else:
        cadenasalidaimagen = "./otros/" + orig + nomsal + "otros" + cadenasalidaimagen + ".jpg"
    cv2.imwrite(cadenasalidaimagen, imagensalida)
    return
