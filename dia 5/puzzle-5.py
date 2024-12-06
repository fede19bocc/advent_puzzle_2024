# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 15:00:37 2024

@author: Fede
"""
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
    reglas = []
    paginas =[]
    corte = False
    for t in txt:
        if not corte and t != "":
            aux = t.split("|")
            for i, dato in enumerate(aux):
                aux[i] = int(dato)
            reglas.append(tuple(aux))
        elif corte and t != "":
            aux = t.split(",")
            for i, dato in enumerate(aux):
                aux[i] = int(dato)
            paginas.append(aux)
        if t == "":
            corte = True
            continue
    return reglas, paginas

def procesar_reglas(reglas):
    mapa_reglas = {}
    for regla in reglas:
        if regla[0] not in mapa_reglas.keys():
            mapa_reglas[regla[0]] = [regla[1]]
        else:
            mapa_reglas[regla[0]].append(regla[1])
            
    return mapa_reglas

def procesar_paginas(paginas, mapa_reglas):
    update_ok = []
    for update in paginas:
        orden = True
        for i, u in reversed(list(enumerate(update))):
            if u in mapa_reglas.keys():
                if i-1 > -1 and update[i-1] in mapa_reglas[u]:
                    orden = False               
        update_ok.append(orden)
    
    return update_ok

def suma_updates_correctos(updates, paginas):
    suma = []
    for i, orden in enumerate(updates):
        if orden:
            aux = paginas[i]
            suma.append(aux[len(aux)//2])

    print(sum(suma))
            
#%%

txt = ["47|53",
"97|13",
"97|61",
"97|47",
"75|29",
"61|13",
"75|53",
"29|13",
"97|29",
"53|29",
"61|53",
"97|53",
"61|29",
"47|13",
"75|47",
"97|75",
"47|61",
"75|61",
"47|29",
"75|13",
"53|13",
"",
"75,47,61,53,29", 
"97,61,53,29,13",
"75,29,13",
"75,97,47,61,53",
"61,13,29",
"97,13,75,29,47"]

reglas, paginas = procesar_txt(txt)
mapa_reglas = procesar_reglas(reglas)
updates = procesar_paginas(paginas, mapa_reglas)
suma_updates_correctos(updates, paginas)
        
#%% parte 1
txt = leer_txt("input.txt")
reglas, paginas = procesar_txt(txt)
mapa_reglas = procesar_reglas(reglas)
updates = procesar_paginas(paginas, mapa_reglas)
suma_updates_correctos(updates, paginas)