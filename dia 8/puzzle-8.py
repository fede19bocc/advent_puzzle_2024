# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 19:13:22 2024

@author: Fede
"""
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

def procesar_txt(txt):
    aux = []
    for t in txt:
        aux.append(list(t))
    mapa = pd.DataFrame(aux)
    return mapa

def ubicar_elemento(mapa, elemento):
    filas, columnas = (mapa == elemento).to_numpy().nonzero()
    locs = [(mapa.index[idx], mapa.columns[col]) for idx, col in zip(filas, columnas)]
    return locs, elemento

def extraer_valores_unicos(txt):
    valores_unicos = set()
    for linea in txt:
        valores_unicos.update(linea)  # Agrega los caracteres únicos de cada línea
    return sorted(valores_unicos)  # Ordenar los valores únicos (opcional)
    


def ubicar_antinodo(antenas):
    '''
    Dada una lista de dos tuplas que representan la ubicación de 
    dos antenas, devuelve una lista de tuplas con la ubicación de los antinodos.    
    '''
    antena1 = antenas[0]
    antena2 = antenas[1]
    vector = tuple(map(lambda x ,y: abs(x - y), antena1, antena2)) 
    antinodos = [tuple(map(lambda x ,y: abs(x - y), antena1, vector)),# primer antinodo
                 tuple(map(lambda x ,y: abs(x + y), antena2, vector))]# segundo antinodo
    return antinodos

def calcular_combinaciones(antenas):
    '''
    Dada una entrada que contiene una lista de ubicaciones de antenas y una etiqueta,
    calcula todas las combinaciones posibles de antinodos generados entre pares consecutivos de antenas.
    Devuelve una lista de tuplas donde cada tupla contiene:
      - La ubicación del antinodo
      - Una descripción de cómo se generó
    '''
    # Extraer la lista de antenas si están encapsuladas junto con una etiqueta
    if isinstance(antenas, tuple) and len(antenas) == 2:
        antenas, etiqueta = antenas  # Extraemos la lista de coordenadas y la etiqueta
    else:
        etiqueta = None  # No hay etiqueta
        
    def combinar(idx):
        # Caso base: no hay más pares para procesar
        if idx >= len(antenas) - 1:
            return

        # Calcular antinodos para el par actual
        antinodo_actual = ubicar_antinodo([antenas[idx], antenas[idx + 1]])

        # Guardar resultados con expresiones descriptivas
        antinodos.append(antinodo_actual[0])
        antinodos.append(antinodo_actual[1])

        # Continuar con el siguiente par
        combinar(idx + 1)

    # Inicializar la lista de antinodos
    antinodos = []
    
    # Comenzar el cálculo recursivo
    if len(antenas) >= 2:
        combinar(0)

    return antinodos, etiqueta

def encontrar_antinodos_mapa(mapa, elementos):
    mapa_antinodos = mapa.copy()
    limite_x = len(mapa.columns)
    limite_y = len(mapa)
    antenas = []
    for elemento in elementos:
        antena = ubicar_elemento(mapa, elemento)
        antenas.append(antena)
    lista_anti = []
    for antena in antenas:
        if antena[1] != ".":
            antinodo, elemento = calcular_combinaciones(antena)
            lista_anti.append(antinodo)
    antinodos = []
    for sublista in lista_anti:
        antinodos.extend(sublista)
    
    for anti in antinodos:
        x, y = anti
        if -1 < x < limite_x and -1 < y < limite_y:
            if mapa_antinodos.loc[x, y] == ".":
                mapa_antinodos.loc[x, y] = "#"
        
    return mapa_antinodos

def contar_antinodo(mapa):
    letra = "#"
    conteo = mapa.map(lambda x: str(x).count(letra)).sum().sum()
    return conteo

#%% test
txt = ["............",
       "........0...",
       ".....0......",
       ".......0....",
       "....0.......",
       "......A.....",
       "............",
       "............",
       "........A...",
       ".........A..",
       "............",
       "............"]

mapa = procesar_txt(txt)
elementos = extraer_valores_unicos(txt)
# ceros = ubicar_elemento(mapa, "0")
# a = ubicar_elemento(mapa, "A")

# antinodos = calcular_combinaciones(ceros)
mapa_antinodos = encontrar_antinodos_mapa(mapa, elementos)
conteo =contar_antinodo(mapa_antinodos)
#%%
u = ubicar_antinodo([ceros[0][1], ceros[0][0]])

#%% input

txt = leer_txt("input.txt")