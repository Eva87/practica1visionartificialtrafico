
import os
import io
import cv2

def guardarcarpetasyfichero(p1,p2,p3,p4,sennal):

    '''Comprobar como lo pide el profe si 0 1 2 para cada 1 si se cambia cambiar la de abajo'''

    ficherosalida = open ( "salida.txt", "a", encoding="utf-8")
    ficherosalida.write(str(p1)+", "+str(p2)+", "+str(p3)+", "+str(p4)+", "+str(sennal)+"\n")
    ficherosalida.close()

    return ()

def guardarimagencarpeta(imagensalida,variablesenl):
    #0 stop 1 prohibido 2 peligro # otros
    '''Aqui hay que hacer que se llame segun el fichero de entrada'''
    '''Quizas ponerlo en una carpeta distinta para cada uno'''

    if variablesenl==0:
        cv2.imwrite ("stop.jpg" , imagensalida)
    elif variablesenl==1:
        cv2.imwrite ("prohibido.jpg" , imagensalida)
    elif variablesenl==2:
        cv2.imwrite ("peligro.jpg" , imagensalida)
    else:
        cv2.imwrite ("otros.jpg" , imagensalida)

    return