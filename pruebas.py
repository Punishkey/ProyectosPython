diccionario={}
capital=[]
while True:

    pais = input("Introduce un país: ")
    if pais=="salir":
        break

    ciudad = input("Introduce una ciudad: ")
    capital.append(ciudad)
    diccionario[pais]=capital

print(diccionario)