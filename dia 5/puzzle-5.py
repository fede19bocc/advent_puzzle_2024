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
    '''
    devuelve una tupla con una lista de reglas en forma de tuplas y 
    una lista de paginas que contiene un listado de numeros cada una
    '''
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
    '''
    Toma las reglas y crea un diccionario donde la clave es un numero de pagina
    los valores es un listado de paginas que deben ir despues que la clave.
    '''
    mapa_reglas = {}
    for regla in reglas:
        if regla[0] not in mapa_reglas.keys():
            mapa_reglas[regla[0]] = [regla[1]]
        else:
            mapa_reglas[regla[0]].append(regla[1])
            
    return mapa_reglas

def procesar_paginas(paginas, mapa_reglas):
    '''
    Chequea cuales paginas cumples con las condiciones del mapa_reglas
    Devuelve un listado de booleanos
    '''
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
    '''
    Imprime la suma de las paginas del medio del listado de updates que esten correctos
    '''
    suma = []
    for i, orden in enumerate(updates):
        if orden:
            aux = paginas[i]
            suma.append(aux[len(aux)//2])

    print(sum(suma))
    
def ordenar_updates(paginas, updates, mapa_reglas):
    '''
    Para las paginas que no cumplen con el mapa de reglas, las reordena y devuelve un 
    listado con las paginas reordenadas.
    '''
    paginas_reordenadas = []
    for i, pagina in enumerate(paginas):
        if not updates[i]:
            for i, u in enumerate(pagina):
                if procesar_paginas([pagina], mapa_reglas)[0]:
                    continue
                else:
                    if u in mapa_reglas.keys():
                        for j in range(0, i):
                            if pagina[j] in mapa_reglas[u]:
                                rotar_elementos(pagina, i, j)
                    else:
                        mover_al_final(pagina, i)
            paginas_reordenadas.append(pagina)
    return paginas_reordenadas

def mover_al_final(lista, indice):
    # Verifica que el índice sea válido
    if 0 <= indice < len(lista):
        elemento = lista.pop(indice)  # Extrae el elemento seleccionado
        lista.append(elemento)       # Agrega el elemento al final
    return lista

def rotar_elementos(lista, i, j):
    if 0 <= i < len(lista) - 1:  # Verifica que el índice sea válido
        lista[i], lista[j] = lista[j], lista[i]
    return lista

def suma_updates_reordenados(paginas_reordenadas):
    '''
    Suma el elemento del medio de cada lista de paginas reordenadas
    '''
    suma = []
    for p in paginas_reordenadas:
        aux = p
        suma.append(aux[len(aux)//2])

    return sum(suma)
            
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


paginas_ordenadas = ordenar_updates(paginas, updates, mapa_reglas)
print("La suma de las paginas reordenadas es: ", suma_updates_reordenados(paginas_ordenadas))
#%% parte 1
txt = leer_txt("input.txt")
reglas, paginas = procesar_txt(txt)
mapa_reglas = procesar_reglas(reglas)
updates = procesar_paginas(paginas, mapa_reglas)
suma_updates_correctos(updates, paginas)

paginas_ordenadas = ordenar_updates(paginas, updates, mapa_reglas)
print("La suma de las paginas reordenadas es: ", suma_updates_reordenados(paginas_ordenadas))