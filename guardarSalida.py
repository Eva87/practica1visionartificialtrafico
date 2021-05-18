from datetime import datetime
import cv2


def guardarcarpetasyfichero(nomiment,orig, p1, p2, p3, p4, sennal, puntuacion):
    ficherosalida = open(orig+"salida.txt", "a", encoding="utf-8")
    ficherosalida.write(str(nomiment) + ";" + str(p1) + ";" + str(p2) + ";" + str(p3) + ";" + str(p4) + ";" + str(
        sennal) + ";" + str(puntuacion) + "\n")
    ficherosalida.close()
    return ()


def guardarimagencarpeta(imagensalida, variablesenl, orig, nomimageent,imagenCopy):
    cadenasalidaimagen = str(datetime.now().strftime("%d%m%Y%H%M%S%f"))
    #nomsal = nomimageent[7:12]
    '''nomsal = nomimageent.replace("/", "")
    nomsal = nomsal.replace("\\", "")
    nomsal = nomsal.replace(".", "")'''
    if variablesenl == 3:
        cadenasalidaimagen = "./stop"+orig+"/" + nomimageent + "stop" + cadenasalidaimagen + ".jpg"
    elif variablesenl == 1:
        cadenasalidaimagen = "./prohibido"+orig+"/" + nomimageent + "prohibido" + cadenasalidaimagen + ".jpg"
    elif variablesenl == 2:
        cadenasalidaimagen = "./peligro"+orig+"/" + nomimageent + "peligro" + cadenasalidaimagen + ".jpg"
    else:
        cadenasalidaimagen = "./otros"+orig+"/" + nomimageent + "otros" + cadenasalidaimagen + ".jpg"
    cv2.imwrite(cadenasalidaimagen, imagensalida)
    cv2.imwrite("./"+orig+"/"+nomimageent + ".jpg",imagenCopy)
    return
