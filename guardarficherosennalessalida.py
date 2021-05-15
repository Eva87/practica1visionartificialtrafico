
import os
import io
from datetime import date, datetime

import cv2

def guardarcarpetasyfichero(nomiment,p1,p2,p3,p4,sennal,puntuacion):

    '''Comprobar como lo pide el profe si 0 1 2 para cada 1 si se cambia cambiar la de abajo'''

    ficherosalida = open ( "salida.txt", "a", encoding="utf-8")
    ficherosalida.write(str(nomiment)+", "+str(p1)+", "+str(p2)+", "+str(p3)+", "+str(p4)+", "+str(sennal)+", "+ str(puntuacion)+ "\n")
    ficherosalida.close()

    return ()

def guardarimagencarpeta(imagensalida,variablesenl,orig):
    #0 stop 1 prohibido 2 peligro # otros
    '''Aqui hay que hacer que se llame segun el fichero de entrada'''
    '''Quizas ponerlo en una carpeta distinta para cada uno'''

    cadenasalidaimagen=str(datetime.now().strftime("%d%m%Y%H%M%S%f"))
    if variablesenl==3:
        cadenasalidaimagen="./stop/"+orig+"stop"+cadenasalidaimagen+".jpg"
    elif variablesenl==1:
        cadenasalidaimagen="./prohibido/"+orig+"prohibido"+cadenasalidaimagen+".jpg"
    elif variablesenl==2:
        cadenasalidaimagen="./peligro/"+orig+"peligro"+cadenasalidaimagen+".jpg"
    else:
        cadenasalidaimagen="./otros/"+orig+"otros"+cadenasalidaimagen+".jpg"

    cv2.imwrite(cadenasalidaimagen, imagensalida)
    return