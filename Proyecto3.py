'''
Preguntamos al usuario en que está pensando. Cuando se introduce la respuesta, realizará el conteo de palabras en la
sentencia e imprimimos en la salida el resultado.

Ejemplo:

    Pregunta: ¿En qué estás pensando?
    Entrada: Bien, hoy es el día en el que me voy a crear un desarrollador experto
    Salida: ¡Muy bien, tu me has mostrado tu pensamiento en 15 palabras!

Para llevar esto a cabo, vamos a crear un fichero de texto y añadimos una unas frases, y contamos cuántas palabras
tiene y lo imprimimos.
Tambien podemos hacerlo por consola.
'''

print("Bienvenido al sistema de piensa y yo te digo de cuantas palabras se compone tu pensamiento... o algo asi")

print("¿En qué estás pensando?")

textoEntrada = len(input("Introduce la frase que estás pensando: ").split(" "))

print(f"¡Muy bien, tú me has mostrado tu pensamiento en {textoEntrada} palabras")

### AHORA LEYENDO UN TXT CON 1 LINEA DE TEXTO###

with open("hola.txt", "r") as file:
    lines = file.readline()
    separate = lines.split(" ")
    count = len(separate)
file.close()

print(f"¡Muy bien, tú me has mostrado tu pensamiento en {count} palabras")

### AHORA LEYENDO UN TXT CON VARIAS LINEAS DE TEXTO###

with open("hola.txt", "r") as file:
    readFile = file.readlines()
    count = 0
    for line in readFile:
        separate = len(line.split(" "))
        count += 1
        print("En la fila " + str(count) + " hay " + str(separate) + " palabras")

##COMPRIMIENDO AL MAXIMO###

print("¡Muy bien, tú me has mostrado tu pensamiento en " + str(len(open("hola.txt").read().split())) + " palabras.")
