# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 08:31:34 2024

@author: federico.boccazzi
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
    datos = [t for t in txt[0]]
    memoria = []
    espacios_libres = []
    for idx, valor in enumerate(datos):
        if idx == 0 or idx % 2 == 0:
            memoria.append(int(valor))
        else:
            espacios_libres.append(int(valor))
    return memoria, espacios_libres

def generar_disco(memoria, espacios_libres):
    idx = 0
    disco = []
    while idx < len(memoria):
        mem_disco = [memoria[idx] for m in range(memoria[idx])]
        if idx < len(espacios_libres):
            esp_disco = ["." for e in range(espacios_libres[idx])]
        disco.extend(mem_disco)
        disco.extend(esp_disco)
        idx += 1
    
    return disco
        
#%% test
txt = ["12345"]
memoria, espacios_libres = procesar_txt(txt)
disco = generar_disco(memoria, espacios_libres)

#%% parte 1
txt = leer_txt("input.txt")