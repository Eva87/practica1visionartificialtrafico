import datetime
import cv2
import os


def guardarcarpetasyfichero(nomiment, orig, p1, p2, p3, p4, sennal, puntuacion):
    ficherosalida = open(orig + "salida.txt", "a", encoding="utf-8")
    ficherosalida.write(str(nomiment) + ";" + str(p1) + ";" + str(p2) + ";" + str(p3) + ";" + str(p4) + ";" + str(
        sennal) + ";" + str(puntuacion) + "\n")
    ficherosalida.close()
    if orig=="MSER":
        orig="mser"
    elif orig == "Alternativa":
        orig="alter"
    else:
        orig="altermser"

    if sennal==1:
        ficherosalidamser1 = open(orig + "salida"+orig+"prohibido.txt", "a", encoding="utf-8")
        ficherosalidamser1.write(str(nomiment) + ";" + str(p1) + ";" + str(p2) + ";" + str(p3) + ";" + str(p4) + ";" + str(
                sennal) + ";" + str(puntuacion) + "\n")
        ficherosalidamser1.close()
    elif sennal==2:
        ficherosalidamser2 = open(orig + "salida"+orig+"peligro.txt", "a", encoding="utf-8")
        ficherosalidamser2.write(str(nomiment) + ";" + str(p1) + ";" + str(p2) + ";" + str(p3) + ";" + str(p4) + ";" + str(
                sennal) + ";" + str(puntuacion) + "\n")
        ficherosalidamser2.close()
    elif sennal==3:
        ficherosalidamser3 = open(orig + "salida"+orig+"stop.txt", "a", encoding="utf-8")
        ficherosalidamser3.write(str(nomiment) + ";" + str(p1) + ";" + str(p2) + ";" + str(p3) + ";" + str(p4) + ";" + str(
                sennal) + ";" + str(puntuacion) + "\n")
        ficherosalidamser3.close()
    return ()


def guardarimagencarpeta(orig, nomimageent, imagenCopy):
    #st = "./resultado_imgs" + "/" + orig + "/"
    st = "./resultado_imgs/"
    try:
        os.mkdir(st)
        print()
    except:
        # print("ya esta creado")
        print()
    cv2.imwrite(st + nomimageent, imagenCopy)
    return


'''def guardarimagencarpeta(imagensalida, variablesenl, orig, nomimageent, imagenCopy):
    cadenasalidaimagen = str(datetime.datetime.now().strftime("%d%m%Y%H%M%S%f"))
    # nomsal = nomimageent[7:12]
    nomsal = nomimageent.replace("/", "")
    nomsal = nomsal.replace("\\", "")
    nomsal = nomsal.replace(".", "")
    if variablesenl == 3:
        cadenasalidaimagen = "./stop" + orig + "/" + nomimageent + "stop" + cadenasalidaimagen + ".jpg"
    elif variablesenl == 1:
        cadenasalidaimagen = "./prohibido" + orig + "/" + nomimageent + "prohibido" + cadenasalidaimagen + ".jpg"
    elif variablesenl == 2:
        cadenasalidaimagen = "./peligro" + orig + "/" + nomimageent + "peligro" + cadenasalidaimagen + ".jpg"
    else:
        cadenasalidaimagen = "./otros" + orig + "/" + nomimageent + "otros" + cadenasalidaimagen + ".jpg"
    cv2.imwrite(cadenasalidaimagen, imagensalida)
    cv2.imwrite("./" + orig + "/" + nomimageent + ".jpg", imagenCopy)
    return'''
