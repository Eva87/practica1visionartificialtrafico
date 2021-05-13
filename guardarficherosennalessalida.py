
import os
import io
import cv2

def guardarcarpetasyfichero(p1,p2,p3,p4,sennal):

    ficherosalida = open ( "/salida.txt", "w" , encoding="utf-8")
    ficherosalida.write(p1 + ", " + p2 + ", " + p3 + ", " + p4 + ", " + sennal)
    ficherosalida.close()

    return ()

def guardarimagencarpeta(imagensalida,variablesenl):
    #0 stop 1 prohibido 2 peligro # otros
    if variablesenl==0:
        cv2.imwrite ("/stop/" + imagensalida + ".jpg" , imagensalida)
    elif variablesenl==1:
        cv2.imwrite ("/prohibido/" + imagensalida + ".jpg" , imagensalida)
    elif variablesenl==2:
        cv2.imwrite ("/peligro/" + imagensalida + ".jpg" , imagensalida)
    else:
        cv2.imwrite ("/otros/" + imagensalida + ".jpg" , imagensalida)

    return