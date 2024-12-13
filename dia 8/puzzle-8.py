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
    locs = tuple((mapa.index[idx], mapa.columns[col]) for idx, col in zip(filas, columnas))
    return locs

def extraer_valores_unicos(txt):
    valores_unicos = set()
    for linea in txt:
        valores_unicos.update(linea)  # Agrega los caracteres únicos de cada línea
    return sorted(valores_unicos)  # Ordenar los valores únicos (opcional)

def ubicar_antinodo(mapa, antenas):
    '''
    Dado un mapa (DataFrame) y una lista de dos tuplas que representan la ubicacion de 
    dos antenas en el mapa.
    Devuelve una lista de tuplas con la ubicacion de los antinodos    
    '''
    antena1 = antenas[0]
    antena2 = antenas[1]
    vector = tuple(map(lambda x ,y: abs(x - y), antena1, antena2))#falta 
    antinodos = [tuple(map(lambda x ,y: abs(x - y), antena1, antena2)), antena2 + vector]
    return antinodos
    

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
ceros = ubicar_elemento(mapa, "0")
a = ubicar_elemento(mapa, "A")

antinodos = ubicar_antinodo(mapa,[a[1], a[2]])

#%% input

txt = leer_txt("input.txt")