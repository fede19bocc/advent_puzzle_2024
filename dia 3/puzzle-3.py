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

def memoriaDañada(datos, regex):
    dañado = []
    for memoria in datos:
        aux = re.split(regex, memoria)
        dañado.append(aux)
    return dañado

#%%

datos = leer_txt('input.txt')
# regex1 = '(?i)(mul\([0-9]*\,[0-9]*\))+' # agrupaba dos mul()mul() juntos
regex2 = '(?i)mul\([0-9]*\,[0-9]*\)' #separa individualmente cada mul()
# multiplicaciones1 = interpretar(datos, regex1)
multiplicaciones2 = interpretar(datos, regex2)
# for i in range(len(multiplicaciones1)):
#     print(i)
#     for mem in multiplicaciones2[i]:
#         if mem not in multiplicaciones1[i]:
#             print(mem)
formato = '[0-9]+'

valores = multiplicarYsumar(multiplicaciones2, formato)

dañado = memoriaDañada(datos, regex2)

print(sum(valores))