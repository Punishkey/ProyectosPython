'''
Crea una agenda de teléfonos que se gestione por consola, que te permita:

1) Añadir a cualquier persona, indicando nombre y después teléfono
2) Buscar el teléfono de una persona
Objetivo:
- Aprender a manejar la entrada y la salida por consola.
- El uso de colecciones (array o diccionario)


Ampliación:

- Al buscar a una persona, que te muestre todas aquellas que comiencen por el texto que has introducido. Ejemplo:
   Introduce un nombre: Pep
   Resultados:
   - Pepe 659331013
   - Pepe Martín 633743551

'''

# It's not the prettiest, but it's working
# hahahah yes, now its more pretty...

import string


def addShedule():
    addName = str(input("Introduce nombre y apellidos: "))
    addTlfno = int(input("Introduce teléfono: "))
    upAddName = string.capwords(addName)
    if upAddName in shedule:
        print("¡Ya está ese contacto en la agenda!")
    else:
        shedule.setdefault(upAddName, addTlfno)
        print("¡Contacto agregado!")


def searchShedule():
    try:
        print("SELECCIONA QUE ES LO QUE QUIERES HACER: \n \n"
              " 1 - BUSCAR POR TELÉFONO \n"
              " 2 - BUSCAR POR EL NOMBRE DE LA PERSONA \n"
              " 3 - VOLVER AL MENÚ")

        selector = int(input("Escribe el número para seleccionar: "))
        if selector == 1:
            searchTlfno = int(input("Ingrese el teléfono a buscar: "))
            for name, tlfno in shedule.items():
                if str(searchTlfno) in str(tlfno):
                    searchList.setdefault(name, tlfno)
            viewShedule(searchList)
        if selector == 2:
            searchName = str(input("Ingrese el nombre de la persona: "))
            upSearchName = string.capwords(searchName)
            for name, tlfno in shedule.items():
                if upSearchName in name:
                    searchList.setdefault(name, tlfno)
            viewShedule(searchList)
        if selector == 3:
            ini()
    except ValueError:
        print("Valor no válido! Por favor no introduzcas valores alfabéticos ni caracteres especiales.")

def delShedule():
    try:
        selectName = str(input("Escribe el nombre de la persona para eliminar: "))
        upSearchName = string.capwords(selectName)
        for name, tlfno in shedule.items():
            if upSearchName in name:
                shedule.pop(upSearchName)
                print("Usuario eliminado de la agenda.")
                break
            else:
                raise KeyError
    except KeyError:
        print("¡Error! No existe esa persona en la agenda.")

def viewShedule(param):
    print(f"\n \n################### SUPERAGENDA ####################")
    for name, tlfno in param.items():
        print(f"Nombre:  {name} \n"
              f"Teléfono: {tlfno} \n")
    print(f"#################################################### \n \n \n")
    ini()


print("########## AGENDA DE TELÉFONOS ##########")

shedule = {}
searchList = {}


def ini():
    try:
        print("SELECCIONA QUE ES LO QUE QUIERES HACER: \n \n"
              " 1 - AÑADIR PERSONA Y TELÉFONO \n"
              " 2 - BUSCAR EL TELÉFONO INTRODUCIENDO EL NOMBRE DE LA PERSONA \n"
              " 3 - VER AGENDA \n"
              " 4 - ELIMINAR CONTACTOS EN AGENDA \n"
              " 5 - SALIR")

        selector = int(input("Escribe el número para seleccionar: "))

        if selector == 1:
            addShedule()
        if selector == 2:
            searchShedule()
        if selector == 3:
            viewShedule(shedule)
        if selector == 4:
            delShedule()
        if selector == 5:
            exit("Adios! Gracias por usar la agenda.")
        else:
            ini()
    except ValueError:
        print("Valor no válido! Por favor no introduzcas valores alfabéticos ni caracteres especiales.")
        ini()


ini()
