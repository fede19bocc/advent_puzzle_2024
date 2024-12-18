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

# parte 2

def ordenar_bloque_enteros(memoria):
    memoria_ordenada = memoria.copy()
    ultimo_libre = 0  # Posición del último espacio libre encontrado
    
    for i, bloque in reversed(list(enumerate(memoria))):
        if i < ultimo_libre:
            break
        if type(bloque) == tuple:  # Si encontramos un bloque de datos
            while ultimo_libre < len(memoria) and type(memoria_ordenada[ultimo_libre]) == tuple:
                ultimo_libre += 1  # Encontrar el siguiente espacio libre
            if ultimo_libre < len(memoria) and ultimo_libre < i:
                ultimo_libre_entero = ultimo_libre #asigo el espacio libre al espacio libre entero.
                # busco un espacio libre donde entre un bloque entero.
                if memoria_ordenada[ultimo_libre_entero] < memoria[i][1]:
                    continuar= True
                    while ultimo_libre_entero < len(memoria) and continuar:
                        if type(memoria_ordenada[ultimo_libre_entero])==int and memoria_ordenada[ultimo_libre_entero] >= memoria[i][1]:
                            continuar = False
                        else:
                            ultimo_libre_entero += 1
                if ultimo_libre_entero < len(memoria) and memoria_ordenada[ultimo_libre_entero] >= memoria[i][1]:
                    espacio_libre = memoria_ordenada[ultimo_libre_entero] 
                    memoria_ordenada[ultimo_libre_entero] = espacio_libre - memoria[i][1]
                    memoria_ordenada.remove(memoria[i])
                    memoria_ordenada.insert(ultimo_libre_entero, memoria[i])
                    memoria_ordenada.insert(i, espacio_libre)
                    # if memoria_ordenada[ultimo_libre] != 0:
                    #     ultimo_libre += 1
    
    return memoria_ordenada

#%% test
# txt = ["13412111"]
txt = ["2333133121414131402"] # checksum()= 2132
memoria = procesar_txt(txt)
disco = generar_disco(memoria)

disco_ordenado = ordenar_disco(disco) # para cadenas cortar sirve
# disco_ordenado = ordenar_disco_optimizado(disco)
suma = checksum(disco_ordenado)
# parte 2
memoria_ordenada = ordenar_bloque_enteros(memoria)
disco_ordenado_por_bloques = generar_disco(memoria_ordenada)
suma_orden_bloques = checksum(disco_ordenado_por_bloques)
#%% parte 1
txt = leer_txt("input.txt")
memoria = procesar_txt(txt)
disco = generar_disco(memoria)
# tardo mas de 10 min y no llego a procesar
# disco_ordenado = ordenar_disco(disco)
disco_ordenado = ordenar_disco_optimizado(disco)
suma = checksum(disco_ordenado)
