# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# puzzle dia 4
import pandas as pd

def leer_txt(archivo):
    '''
    Devuelve una lista con listas de numeros por reporte
    '''
    lista = []
    with open(archivo, "r") as f:
        for line in f.readlines():
            lista.append(line)
    return lista

def procesar_datos(datos):
    copia = datos.copy()
    aux = []
    for c in copia:
        for i in c:
            aux.append(list(i))
    return pd.DataFrame(aux)

def vertical(datos):
    XMAS = 0
    for columna in datos:
        x = False
        m = False
        a = False
        s = False
        for celda in datos[columna]:
            if celda == "X" and not x:
                x = True
            if celda == "M" and not m and x:
                m = True
            if celda == "A" and not a and x and m:
                a = True
            if celda == "S" and not s and x and m and a:
                s = True
            if x and m and a and s:
                XMAS += 1
                x = False
                m = False
                a = False
                s = False
    return XMAS

def horizontal(datos): # cuenta de mas cuadno la palabra es XAMAS, hay que resetear los bool cuando la siguiente no es la que corresponde
    XMAS = 0
    for fila in range(len(datos)):
        x = False
        m = False
        a = False
        s = False
        for celda in datos.iloc[fila]:
            if celda == "X" and not x:
                x = True
            if celda == "M" and not m and x:
                m = True
            if celda == "A" and not a and x and m:
                a = True
            if celda == "S" and not s and x and m and a:
                s = True
            if x and m and a and s:
                XMAS += 1
                x = False
                m = False
                a = False
                s = False
    return XMAS

#%% datos de prueba
test = [["MMMSXMASM"],
        ["MSAMXMSMSA"],
        ["AMXSXMAAMM"],
        ["MSAMASMSMX"],
        ["XMASAMXAMM"],
        ["XXAMMXXAMA"],
        ["SMSMSASXSS"],
        ["SAXAMASAAA"],
        ["MAMMMXMMMM"],
        ["MXMXAXMASX"]]

datos_test = procesar_datos(test)
print(vertical(datos_test))
print(horizontal(datos_test))
#%% input del puzzle
txt = leer_txt(".\input.txt")
datos = procesar_datos(txt)


#%%
# DataFrame de ejemplo
df = pd.DataFrame({
    "Nombre": ["Ana", "Luis", "Juan"],
    "Edad": [25, 30, 35],
    "Ciudad": ["Madrid", "Barcelona", "Valencia"]
})


for i in range(len(df)):
    print(f"Fila {i}: {df.iloc[i].to_dict()}")
