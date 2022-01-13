'''
Par o impar

Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000

Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos el mensaje con el resultado.

Ejemplo:

    Mensaje que se muestra: ¿En qué número estás pensando?
    Entrada: 25
    Salida: ¡Es un número impar! ¿Puedes añadir otro?

No te olvides de capturar las excepciones y de probar el programa hasta que esté a prueba de errores.
'''
import sys

print("Bienvenido a Par o Impar")

try:
    num = (int(input("Dame un número entre el 1 y el 1000: ")))
except ValueError:
    sys.exit("No has introducido un número!! Saliendo del programa!")
while True:
    while 0 < num <= 1000:
        print("Has introducido el número " + str(num))
        if num % 2 == 0:
            print("!Es un número par!")
        else:
            print("!Es un número impar!")
        num = 0
        intentar = input("¿Deseas probar otro número? Escribe si, si quieres seguir, o no, si quieres salir: ").lower()
    try:
        if intentar == "no":
            sys.exit("¡Hasta luego!")
        elif intentar == "si":
            num = (int(input("Dame un número entre el 1 y el 1000: ")))
        else:
            sys.exit("No has escrito bien tu decisión asique... Saliendo del programa!!")
    except NameError:
        sys.exit("Valor no reconocido. Saliendo del programa!!")
