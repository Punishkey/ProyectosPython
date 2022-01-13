'''
Juego del Mad Lib

Pedimos al usuario que introduzca varias entradas con varias preguntas.

Puede ser cualquier cosa, como un nombre, un adjetivo, un pronombre o incluso una acción.
Una vez que se obtiene la entrada, se puede reorganizar para construir su propia historia.

'''

# adjetivo
# nombre
# accion
# pronombre
import time

adjetivo = input("Introduce un adjetivo: "). lower()
nombre = input("Introduce un nombre propio: "). lower()
accion = input("Introduce una acción: "). lower()
pronombre = input("Introduce un pronombre: ").lower()

print("Construyendo tu historia...")
time.sleep(5)
print("No seas impaciente!!")
time.sleep(5)
print("Listo! Historia construida. Mostrando!")
time.sleep(3)

print("Pues " + nombre + " estaba en su casa jugando al ordenador")
time.sleep(3)
print("había mucho silencio, pues no tenía un ordenador muy rápido para ejecutar los juegos a velocidad " + adjetivo)
time.sleep(3)
print(nombre + " arto de la lentitud, cogió el teléfono y se dispuso a " + accion)
time.sleep(3)
print("No queda otra cosa que hacer. " + pronombre + "! vaya mierda de historia, no tienes ni puta idea de hacerlas.")
time.sleep(3)
print("Hasta luego!")
