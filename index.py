import cv2
import random
from random import randint

while True:
    photo=str(random.randint(1,3))
    imagen=cv2.imread('./img/'+photo+'.png')
    """ cv2.imshow('img', imagen) """
    sup=imagen[300,253]
    med=imagen[433,253]
    inf=imagen[800,253]

    if sup[0]!=77:
        print('Semáforo en rojo - DETENGASE!!!')

    elif med[0]!=77:
        print('Semáforo en amarillo - ESPEREEE!!!')

    else:
        print('Semáforo en verde - AVANZE!!!')

    # Redimensiona la imagen y muestra durante 5 segundos
    img_redimention = cv2.resize(imagen, (150, 220))
    cv2.imshow('Semáforo ', img_redimention)
    cv2.waitKey(2500)#Milisegundos
    cv2.destroyAllWindows()