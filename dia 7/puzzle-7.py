# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:56:19 2024

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
    datos = []
    for line in txt: 
        aux = line.replace(": ", " ")
        aux = aux.split(" ")
        aux = [int(a) for a in aux]
        datos.append((aux[0], aux[1::]))
    return datos

def aplicar_operaciones(datos):
    ecuaciones_ok = []
    for d in datos:
        es_ecuacion = False
        resultado = d[0]
        numeros = d[1]
        resultados = calcular_combinaciones(numeros)
        for r in resultados:
            if r[0] == resultado:
                es_ecuacion = True
        ecuaciones_ok.append(es_ecuacion)
    return ecuaciones_ok

def calcular_combinaciones(nums):
    def combinar(idx, acumulado, expresion):
        if idx == len(nums):
            resultados.append((acumulado, expresion))
            return
        
        # Suma el siguiente número
        combinar(idx + 1, acumulado + nums[idx], f"({expresion} + {nums[idx]})")
        
        # Multiplica el siguiente número
        combinar(idx + 1, acumulado * nums[idx], f"({expresion} * {nums[idx]})")
        
        # Une el siguiente numero
        combinar(idx + 1, int(str(acumulado) + str(nums[idx])), f"({expresion}{nums[idx]})")
    
    resultados = []
    if nums:  # Asegurarse de que la lista no esté vacía
        combinar(1, nums[0], str(nums[0]))
    return resultados
    
def calcular_suma_ecuaciones(datos, ecuaciones_ok):
    suma = 0
    for i, ec in enumerate(ecuaciones_ok):
        if ec:
            suma += datos[i][0]
    return suma
            
#%% test
txt = ["190: 10 19",        # 10 * 19 = 190
       "3267: 81 40 27",    # 81 + 40 * 27 = 3267 o 81 * 40 + 27 = 3267
       "83: 17 5",
       "156: 15 6",
       "7290: 6 8 6 15",
       "161011: 16 10 13",
       "192: 17 8 14",
       "21037: 9 7 18 13",
       "292: 11 6 16 20"]   # 11 + 6 * 16 + 20

datos = procesar_txt(txt)
ecuaciones_ok = aplicar_operaciones(datos)
suma = calcular_suma_ecuaciones(datos, ecuaciones_ok)
print(f"El resultado total de las calibraciones es :{suma}")

#%%
txt = leer_txt("input.txt")
datos = procesar_txt(txt)
ecuaciones_ok = aplicar_operaciones(datos)
suma = calcular_suma_ecuaciones(datos, ecuaciones_ok)
print(f"El resultado total de las calibraciones es :{suma}")