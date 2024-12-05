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

def invertir_columnas(df):
    df_invertido_columnas = df.iloc[:, ::-1]
    return df_invertido_columnas

def invertir_filas(df):
    df_invertido_filas = df.iloc[::-1].reset_index(drop=True)
    return df_invertido_filas

def diagonal(df):
  
    XMAS = 0
    for columna in datos:
        x = m = a = False
        for celda in datos[columna]:
            if celda == "X":
                x = True
                m = a = False
                continue
            elif celda == "M" and x:
                m = True
                a = False
                continue
            elif celda == "A" and x and m:
                a = True
                continue
            elif celda == "S" and x and m and a:
                XMAS += 1
                x = m = a = False
                continue
            else:
                x = m = a = False
                continue
    return XMAS
        
    pass
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
            elif celda == "M" and x:
                m = True
                a = False
            elif celda == "A" and x and m:
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
            elif celda == "M" and x:
                m = True
                a = False
            elif celda == "A" and x and m:
                a = True
            elif celda == "S" and x and m and a:
                XMAS += 1
                x = m = a = False 
            else:
                x = m = a = False 
    return XMAS

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
print("Verticales de arriba a abajo: ", vertical(datos_test))
print("Verticales de abajo a arriba: ", vertical(datos_test, True))
print("Horizontales de izq a der: ", horizontal(datos_test))
print("Horizontales de der a izq: ", horizontal(datos_test, True))
print("Diagonales hacia abajo: ", diagonal(datos_test))

#%% input del puzzle
txt = leer_txt(".\input.txt")
datos = procesar_datos(txt)


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
