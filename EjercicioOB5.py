'''
Convierte un Excel a CSV

Objetivo:


    Aprender a trabajar con ficheros

    Usar la librería pandas de Python


'''

import pandas as pd

# read a excel

read_file = pd.read_excel("pruebas.xlsx")

# dataframe csv

read_file.to_csv("pruebas.csv", index=None, header=True)

# convert

df = pd.DataFrame(pd.read_csv("pruebas.csv"))

# finish

print(df)

