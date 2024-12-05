# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# puzzle dia 4
import pandas as pd
import numpy as np

def leer_txt(archivo):
    '''
    Devuelve una lista con listas de numeros por reporte
    '''
    lista = []
    with open(archivo, "r") as f:
        for line in f.readlines():
            lista.append([line])
    return lista

def procesar_datos(datos):
    copia = datos.copy()
    aux = []
    for c in copia:
        for i in c:
            aux.append(list(i))
    return pd.DataFrame(aux)

def invertir_columnas(df):
    df_invertido_columnas = df.iloc[:, ::-1]
    return df_invertido_columnas

def invertir_filas(df):
    df_invertido_filas = df.iloc[::-1].reset_index(drop=True)
    return df_invertido_filas

def diagonal(datos):
    datos_inv = invertir_filas(datos)
    diagonal = []
    for i in range(len(datos)):
        if i == 0:
            diagonal.append(np.diag(datos))
            diagonal.append(np.diag(datos_inv))
        else:
            diagonal.append(np.diag(datos, i))
            diagonal.append(np.diag(datos, -i))
            diagonal.append(np.diag(datos_inv, i))
            diagonal.append(np.diag(datos_inv, -i))
    return diagonal

def vertical(datos, invertir = False):
    if invertir:
        datos = invertir_filas(datos)
    XMAS = 0
    for columna in datos:
        x = m = a = False
        for celda in datos[columna]:
            if celda == "X":
                x = True
                m = a = False
            elif celda == "M" and x and not m:
                m = True
                a = False
            elif celda == "A" and x and m and not a:
                a = True
            elif celda == "S" and x and m and a:
                XMAS += 1
                x = m = a = False 
            else:
                x = m = a = False 
    return XMAS

def horizontal(datos, invertir = False):
    if invertir:
        datos = invertir_columnas(datos)
    XMAS = 0
    for fila in range(len(datos)):
        x = m = a = False
        for celda in datos.iloc[fila]:
            if celda == "X":
                x = True
                m = a = False
            elif celda == "M" and x and not m:
                m = True
                a = False
            elif celda == "A" and x and m and not a:
                a = True
            elif celda == "S" and x and m and a:
                XMAS += 1
                x = m = a = False 
            else:
                x = m = a = False 
    return XMAS

def horizontal_MAS(datos, invertir = False):
    if invertir:
        datos = invertir_columnas(datos)
    MAS = 0
    for fila in range(len(datos)):
        m = a = False
        for celda in datos.iloc[fila]:
            if celda == "M":
                m = True
                a = False
            elif celda == "A" and m and not a:
                a = True
            elif celda == "S" and m and a:
                MAS += 1
                m = a = False 
            else:
                m = a = False 
    return MAS
#%% datos de prueba
test = [["MMMSXXMASM"],
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
# print("Verticales de arriba a abajo: ", vertical(datos_test))
# print("Verticales de abajo a arriba: ", vertical(datos_test, True))
# print("Horizontales de izq a der: ", horizontal(datos_test))
# print("Horizontales de der a izq: ", horizontal(datos_test, True))
# print("Diagonales hacia abajo: ", diagonal(datos_test))
diag = pd.DataFrame(diagonal(datos_test))

suma = [vertical(datos_test), 
        vertical(datos_test, True),
        horizontal(datos_test),
        horizontal(datos_test, True),
        horizontal(diag),
        horizontal(diag, True)]

print("XMAS totales: ", sum(suma))

print(horizontal_MAS(diag))
print(horizontal_MAS(diag, True))


#%% input del puzzle
txt = leer_txt("input.txt")
datos = procesar_datos(txt)
diag = pd.DataFrame(diagonal(datos))

suma = [vertical(datos), 
        vertical(datos, True),
        horizontal(datos),
        horizontal(datos, True),
        horizontal(diag),
        horizontal(diag, True)]
print("XMAS totales: ", sum(suma))

#%% solucion hecha por wleftwich
# https://github.com/wleftwich
import re

with open("input.txt") as fh:
    data = fh.read()
    
grid = {}
for y, line in enumerate(data.splitlines()):
    for x, c in enumerate(line):
        grid[complex(x, y)] = c
        
def count_xmas(point, grid=grid):
    if grid.get(point) != "X":
        return 0
    counter = 0
    for drxn in [1 + 0j, 1 + 1j, 0 + 1j, -1 + 1j, -1 + 0j, -1 - 1j, 0 - 1j, 1 - 1j]:
        pts = (point + n * drxn for n in [1, 2, 3])
        if [grid.get(pt) for pt in pts] == ["M", "A", "S"]:
            counter += 1
    return counter

sum(count_xmas(point) for point in grid)

def is_masx(point, grid=grid):
    if grid.get(point) != "A":
        return False
    a = {grid.get(point + drxn) for drxn in [(1 + 1j), (-1 - 1j)]}
    b = {grid.get(point + drxn) for drxn in [(-1 + 1j), (1 - 1j)]}
    if a == b == {"M", "S"}:
        return True
    return False

sum(is_masx(point) for point in grid)
