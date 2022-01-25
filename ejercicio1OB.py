'''
Ejercicio 1
Enunciado: Imprime todos los ficheros existentes en tu carpeta de Descargas
Objetivo:
- Aprender a utilizar librerías sencillas (en este caso, os) y sus funciones.
- Aprender a utilizar los bucles y los condicionales.

El algoritmo del ejercicio es el siguiente:
- Obtén todos los ficheros y directorios de un directorio en concreto. Para ello necesitas una función existente en la librería os (Sistema Operativo) de Python.
- Recorre todos los resultados obtenidos por la función anterior. Lo puedes hacer, por ejemplo, con un bucle for.
- Imprime por pantalla solo aquellos resultados que sean ficheros (para ello también necesitas una función existente en os.


 Lista los tamaños de los ficheros en formato humano.
- Recorre de manera recursiva todos los directorios desde tu carpeta personal y muestra los ficheros de cada directorio y su tamaño.

'''

import os
from os.path import getsize, join

path = 'C:/Users/Punishkey/pruebas'
# create variable for directory
directory = os.scandir(path)

kilobyte = 1024
size = 0
# We get all the list of files in the folder, i use scandir, python recommended.
# os.scandir(directory)

# we go through the directory file by file and print what we get with its name

for i in directory:
    # print(i.name)     # Holy shit! a lot of files
    # use a file variable for store files, non directory`s

    file = []

    if i.is_file():
        stat = os.path.getsize(i)
        file.append(i)
        print(file, round(stat / kilobyte, 2), "kb")

directory.close()
# mmm recursive?
# os.walk(directory)

# testing if with walk it is recursive, I need another variable
# change everything. reed more about os and see examples.


for root, dire, files in os.walk(path):
    for name in files:
        size = getsize(join(root, name))
        print(f"Ruta: {root} \n "
              f"Archivo: {files} - Peso: {round(size / kilobyte, 2)} kb")


