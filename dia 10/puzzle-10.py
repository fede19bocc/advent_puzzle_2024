# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:03:58 2024

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
                lista.append(line.strip())
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

#%%

txt = ["0123",
       "1234",
       "8765",
       "9876"]

mapa = procesar_txt(txt)
ceros = ubicar_elemento(mapa, "0")

#%%

txt = leer_txt("input.txt")
mapa = procesar_txt(txt)