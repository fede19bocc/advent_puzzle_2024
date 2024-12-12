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

#%% input

txt = leer_txt("input.txt")