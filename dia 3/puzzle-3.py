# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 08:51:16 2024

@author: federico.boccazzi
"""

import re

def leer_txt(archivo):
    '''
    Devuelve una lista con listas de numeros por reporte
    '''
    lista = []
    with open(archivo, "r") as f:
        for line in f.readlines():
            lista.append(line)
    return lista

def interpretar(memorias, regex):
    multiplicaciones = []
    for memoria in memorias:
        aux = re.findall(regex, memoria)
        multiplicaciones.append(aux)
    return multiplicaciones

def multiplicarYsumar(multiplicaciones, formato):
    valores = []
    for lista in multiplicaciones:
        for l in lista:
           aux = re.findall(formato, l)
           valores.append(int(aux[0])*int(aux[1]))
    return valores

#%%

datos = leer_txt('input.txt')
regex = '(?i)(mul\([0-9]*\,[0-9]*\))+'
multiplicaciones = interpretar(datos, regex)

formato = '[0-9]+'

valores = multiplicarYsumar(multiplicaciones, formato)

print(sum(valores))