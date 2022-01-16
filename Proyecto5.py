'''
¿Cuál es mi acrónimo?

Vamos a pedir al usuario que ingrese el significado completo de una organización o concepto y con ello
como resultado obtendremos el acrónimo. Por ejemplo:

    Entrada -> As Soon As Possible. Salida -> ASAP.
    Entrada -> World Health Organization. Salida -> WHO.
    Entrada -> Absent Without Leave. Salida -> AWOL.
'''

character = ""

entrada = input("Escribe un significado completo de una organización o concepto. Ejemplo: \n"
                    "As Soon As Possible --> ASAP y te daré el acrónimo:  ").lower().split()
for i in entrada:
        character += i[0].upper()

print(character)
