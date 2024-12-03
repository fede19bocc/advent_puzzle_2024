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

def multiplicarYsumar(listas, formato):
    valores = []
    condicion = True
    for lista in listas:
        for l in lista:
            #si aparece don't anula la multiplicacion
            if l == "don't()":
                condicion = False
            elif l == "do()":
                condicion = True
            # si esta habilitada la multipicacion y no son don' o do 
            if condicion and l != "don't()" and l != "do()": 
                aux = re.findall(formato, l)
                valores.append(int(aux[0])*int(aux[1]))
    return valores

#%%

datos = leer_txt('input.txt')
# regex1 = '(?i)(mul\([0-9]*\,[0-9]*\))+' # agrupaba dos mul()mul() juntos
regex = '(?i)mul\([0-9]*\,[0-9]*\)' #separa individualmente cada mul()
multiplicaciones = interpretar(datos, regex)

formato = '[0-9]+'
valores = multiplicarYsumar(multiplicaciones, formato)
print("Valores: ", sum(valores))
#%%
regex_cond = 'mul\([0-9]*\,[0-9]*\)|do\(\)|don\'t\(\)'
mult_cond = interpretar(datos, regex_cond)
valores_cond = multiplicarYsumar(mult_cond, formato)
print("Valores con condicionales: ", sum(valores_cond))
