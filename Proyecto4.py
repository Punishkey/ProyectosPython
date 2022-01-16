'''
Información de la biografía

Pregunte a un usuario su información personal en una sola ronda de preguntas. Luego hay que verificar que la
información que se ha ingresado sea válida. Finalmente, se imprime un resumen de toda la información que ha sido ingresada.

Por ejemplo: ¿Cuál es su nombre? Si el usuario ingresa *, hay que indicar que la entrada es incorrecta y se pide que se
ingrese correctamente un nombre válido.

Cuando se introduce todo correctamente, se muestra un resumen como el que aparece a continuación:

- Nombre: John Doe
- Fecha de nacimiento: Jan 1, 1954
- Dirección: 24 fifth Ave, NY
- Metas personales: To be the best programmer there ever was.
'''
import re

print("Bienvenido al sistema de información de la biografía.")
print("Por favor, responda a las siguientes preguntas:")

count = 0
while True:
        name = input("¿Cual es su nombre?: ")
        for i in range(len(name)):
            if re.match("[+*]", name[i]) or re.match("[0-9]", name[i]):
                count = 1
        if count == 0:
            birthday = input("Introduce tu fecha de cumpleaños: ")
            street = input("Introduce tu dirección: ")
            personalGoals = input("Introduce tu meta personal: ")
            break
        if count == 1:
            print("Error, no introduzcas carácteres especiales en el nombre, ni números")
            count = 0

print(" - Nombre: " + name + "\n" +
      " - Fecha de nacimiento: " + birthday + "\n" +
      " - Dirección: " + street + "\n" +
      " - Metas personales: " + personalGoals)
