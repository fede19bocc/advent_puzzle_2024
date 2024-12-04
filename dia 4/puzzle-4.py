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

def diagonalizar(df):
    df_diagonal = pd.DataFrame(".", index=range(len(df)), columns=range(len(df.columns)))
    contador_f = 0
    contador_c = 0
    
    for j in range(len(df.columns)):  
        for i in range(len(df)):
            if i >= j:
                df_diagonal.iloc[i, j] = df.iloc[i, j]
            if i < j:
                df_diagonal.iloc[i+1, j] = df.iloc[i, j]
    return df_diagonal
        
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
