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
    datos = list((t for t in txt[0]))
    memoria = []
    id_mem = 0
    for idx, valor in enumerate(datos):
        if idx == 0 or idx % 2 == 0:
            memoria.append((str(id_mem), int(valor)))
            id_mem += 1
        else:
            memoria.append(int(valor))
    return memoria

def generar_disco(memoria):
    aux = {}
    n = 0
    for elemento in memoria:
        if type(elemento) == tuple:
            idx, cantidad = elemento
            for c in range(cantidad):
                aux[n] = idx
                n += 1
        else:
            for e in range(elemento):
                aux[n] = "."
                n += 1
    return aux        

# mi solucion, al cambiar listas por diccionarios no hubo diferencia en la optimizacion
# por ende toma demasiado tiempo procesarla. Utilice chatgtp para mejorar los tiempos.
def ordenar_disco(disco):
    disco_ordenado = disco.copy()
    for i, bloque in reversed(disco.items()):
        if bloque != ".":
            for j, mem_libre in disco_ordenado.items():
                if mem_libre == "." and j < i:
                    disco_ordenado[j] = bloque
                    disco_ordenado[i] = "."
                    break
    return disco_ordenado

# solucion aportada por chatgtp que disminuye la complejidad de mi metodo
def ordenar_disco_optimizado(disco):
    disco_ordenado = disco.copy()
    ultimo_libre = 0  # Posición del último espacio libre encontrado
    
    for i, bloque in reversed(disco.items()):
        if i < ultimo_libre:
            break
        if bloque != ".":  # Si encontramos un bloque de datos
            while ultimo_libre < len(disco) and disco[ultimo_libre] != ".":
                ultimo_libre += 1  # Encontrar el siguiente espacio libre
            if ultimo_libre < len(disco) and ultimo_libre < i:  
                disco_ordenado[ultimo_libre] = bloque
                disco_ordenado[i] = "."
                ultimo_libre += 1
    
    return disco_ordenado


def checksum(disco_ordenado):
    suma = 0
    for i, valor in disco_ordenado.items():
        if valor != ".":
            suma += i*int(valor)
    return suma
#%% test
# txt = ["12345"]
txt = ["233313312141413140211"] # checksum()= 2132
memoria = procesar_txt(txt)
disco = generar_disco(memoria)

disco_ordenado = ordenar_disco(disco) # para cadenas cortar sirve
# disco_ordenado = ordenar_disco_optimizado(disco)
suma = checksum(disco_ordenado)
#%% parte 1
txt = leer_txt("input.txt")
memoria = procesar_txt(txt)
disco = generar_disco(memoria)
# tardo mas de 10 min y no llego a procesar
# disco_ordenado = ordenar_disco(disco)
disco_ordenado = ordenar_disco_optimizado(disco)
suma = checksum(disco_ordenado)
