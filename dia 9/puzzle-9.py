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
    espacios_libres = []
    id_mem = 0
    for idx, valor in enumerate(datos):
        if idx == 0 or idx % 2 == 0:
            memoria.append((str(id_mem), int(valor)))
            id_mem += 1
        else:
            espacios_libres.append(int(valor))
    return memoria, espacios_libres

def generar_disco(memoria, espacios_libres):
    aux = []

    for idx, cantidad in memoria:
        aux.append(idx*cantidad)
    for e in range(len(espacios_libres)):
        aux.insert(2*e + 1, "." * espacios_libres[e])
    return aux        

def ordenar_disco(disco):
    disco_aux = list((d for d in disco))
    for i, bloque in reversed(list(enumerate(disco_aux))):
        if bloque != ".":
            for j, mem_libre in enumerate(disco_aux):
                if mem_libre == "." and j < i:
                    disco_aux[j] = bloque
                    disco_aux[i] = "."
                    break
    return disco_aux

# solucion aportada por chatgtp que disminuye la complejidad de mi metodo
def ordenar_disco_optimizado(disco):
    disco_aux = [d for d in disco]
    ultimo_libre = 0  # Posición del último espacio libre encontrado
    
    for i, bloque in reversed(list(enumerate(disco_aux))):
        if i < ultimo_libre:
            break
        if bloque != ".":  # Si encontramos un bloque de datos
            while ultimo_libre < len(disco_aux) and disco_aux[ultimo_libre] != ".":
                ultimo_libre += 1  # Encontrar el siguiente espacio libre
            if ultimo_libre < len(disco_aux) and ultimo_libre < i:  
                disco_aux[ultimo_libre] = bloque
                disco_aux[i] = "."
                ultimo_libre += 1
    
    disco_ordenado = "".join(disco_aux)
    return disco_ordenado


def checksum(disco_ordenado):
    disco_aux = list((d for d in disco_ordenado))
    suma = 0
    for i, valor in enumerate(disco_aux):
        if valor != ".":
            suma += i*int(valor)
    return suma
#%% test
# txt = ["12345"]
txt = ["233313312141413140211"] # checksum()= 2132
memoria, espacios_libres = procesar_txt(txt)
disco = generar_disco(memoria, espacios_libres)
# disco_ordenado = ordenar_disco(disco)
# disco_ordenado = ordenar_disco_optimizado(disco)
# suma = checksum(disco_ordenado)
#%% parte 1
txt = leer_txt("input.txt")
memoria, espacios_libres = procesar_txt(txt)
disco = generar_disco(memoria, espacios_libres)
# cuando los id son de dos o mas digitos los procesa mal
disco_ordenado = ordenar_disco_optimizado(disco)
suma = checksum(disco_ordenado)
'''
That's not the right answer; your answer is too low. If you're stuck, make sure
you're using the full input data; there are also some general tips on the about
page, or you can ask for hints on the subreddit. Please wait one minute before 
trying again. 
'''