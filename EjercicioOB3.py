'''
Enunciado: Crea una función que calcule los números primos entre 1 y N, siendo N el parámetro que recibe la función.

Objetivo:

- Uso de bucles anidados
- El uso de colecciones

'''

num1 = int(input("Introduce un número mayor a 1: "))


def primo(num):
    try:
        if num == 1:
            raise ValueError
        for n in range(2, num):
            if num % n == 0:
                return False
        print(str(num) + " es primo")
    except ValueError:
        print("el 1 por convenio no se considera primo")


for i in range(1, num1):
    primo(i)
