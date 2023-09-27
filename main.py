import cv2
import os
import time



# Directorio que contiene las imágenes
directorio_de_imagenes = './img/'

# Enumera los archivos en el directorio
archivos_de_imagen = os.listdir(directorio_de_imagenes)

# Itera a través de los archivos de imagen y cárgalos uno por uno
for archivo in archivos_de_imagen:
    # Construye la ruta completa del archivo de imagen
    ruta_de_imagen = os.path.join(directorio_de_imagenes, archivo)

    # Lee la imagen desde el archivo especificado
    img = cv2.imread(ruta_de_imagen)

    # Comprueba si la imagen se ha cargado correctamente
    if img is not None:
        # Muestra la imagen en una ventana con el título del nombre del archivo
        img = cv2.resize(img, (100, 150))
        cv2.imshow(archivo, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Espera a que el usuario presione una tecla y luego cierra todas las ventanas

