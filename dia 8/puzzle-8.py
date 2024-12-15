# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 19:13:22 2024

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
    aux = []
    for t in txt:
        aux.append(list(t))
    mapa = pd.DataFrame(aux)
    return mapa

def ubicar_elemento(mapa, elemento):
    filas, columnas = (mapa == elemento).to_numpy().nonzero()
    locs = [(mapa.index[idx], mapa.columns[col]) for idx, col in zip(filas, columnas)]
    return locs, elemento

def extraer_valores_unicos(txt):
    valores_unicos = set()
    for linea in txt:
        valores_unicos.update(linea)  # Agrega los caracteres únicos de cada línea
    return sorted(valores_unicos)  # Ordenar los valores únicos (opcional)
    
def ubicar_antinodo(antenas):
    '''
    Dada una lista de dos tuplas que representan la ubicación de 
    dos antenas, devuelve una lista de tuplas con la ubicación de los antinodos.    
    '''
    antena1 = antenas[0]
    antena2 = antenas[1]
    vector = tuple(map(lambda x ,y: x - y, antena1, antena2)) 
    antinodos = [tuple(map(lambda x ,y: x + y, antena1, vector)),# primer antinodo
                 tuple(map(lambda x ,y: x - y, antena2, vector))]# segundo antinodo
    return antinodos

def calcular_antinodos(antenas):
    '''
    Dada una entrada que contiene una lista de ubicaciones de antenas y una etiqueta,
    calcula todas las combinaciones posibles de antinodos generados entre pares de antenas.
    Devuelve una lista de tuplas donde cada tupla contiene:
      - La ubicación del antinodo
    '''
    # Extraer la lista de antenas si están encapsuladas junto con una etiqueta
    if isinstance(antenas, tuple) and len(antenas) == 2:
        antenas, etiqueta = antenas  # Extraemos la lista de coordenadas y la etiqueta
    else:
        etiqueta = None  # No hay etiqueta

    # Verificar que hay suficientes antenas
    if len(antenas) < 2:
        return [], etiqueta  # No se pueden generar antinodos si hay menos de dos antenas

    # Función recursiva para calcular las combinaciones de antenas
    def generar_antinodos(indices, start):
        if len(indices) == 2:  # Condición base: se tienen dos índices seleccionados
            a, b = indices
            antena1 = antenas[a]
            antena2 = antenas[b]

            # Calcular los antinodos entre estas dos antenas usando la función ubicar_antinodo
            antinodos_generados = ubicar_antinodo([antena1, antena2])

            # Agregar antinodos a la lista con sus descripciones
            for antinodo in antinodos_generados:
                antinodos.append(antinodo)
            return

        # Recursivamente intentar agregar más índices
        for i in range(start, len(antenas)):
            generar_antinodos(indices + [i], i + 1)

    # Lista para almacenar los antinodos generados
    antinodos = []

    # Iniciar la recursión para generar combinaciones
    generar_antinodos([], 0)

    return antinodos, etiqueta

def encontrar_antinodos_mapa(mapa, elementos):
    mapa_antinodos = mapa.copy()
    limite_x = len(mapa.columns)
    limite_y = len(mapa)
    antenas = []
    for elemento in elementos:
        antena = ubicar_elemento(mapa, elemento)
        antenas.append(antena)
    lista_anti = []
    for antena in antenas:
        if antena[1] != ".":
            antinodo, elemento = calcular_antinodos(antena)
            lista_anti.append(antinodo)
    
    antinodos = antinodos_unicos(lista_anti)
    contador_antinodo = 0
    for anti in antinodos:
        x, y = anti
        if -1 < x < limite_x and -1 < y < limite_y:
            contador_antinodo += 1
            if mapa_antinodos.loc[x, y] == ".":
                mapa_antinodos.loc[x, y] = "#"
    return mapa_antinodos, contador_antinodo

def antinodos_unicos(lista_antinodos):
    antinodos = set()
    for lista in lista_antinodos:
        antinodos.update(lista)
    return list(antinodos)


# metodos parte 2
def calcular_antinodos_full(antenas, mapa):
    '''
    Dada una entrada que contiene una lista de ubicaciones de antenas y una etiqueta,
    calcula todas las combinaciones posibles de antinodos generados entre pares de antenas.
    Devuelve una lista de tuplas donde cada tupla contiene:
      - La ubicación del antinodo
    '''
    # Extraer la lista de antenas si están encapsuladas junto con una etiqueta
    if isinstance(antenas, tuple) and len(antenas) == 2:
        antenas, etiqueta = antenas  # Extraemos la lista de coordenadas y la etiqueta
    else:
        etiqueta = None  # No hay etiqueta

    # Verificar que hay suficientes antenas
    if len(antenas) < 2:
        return [], etiqueta  # No se pueden generar antinodos si hay menos de dos antenas

    # Función recursiva para calcular las combinaciones de antenas
    def generar_antinodos(indices, start):
        if len(indices) == 2:  # Condición base: se tienen dos índices seleccionados
            a, b = indices
            antena1 = antenas[a]
            antena2 = antenas[b]

            # Calcular los antinodos entre estas dos antenas usando la función ubicar_antinodo
            antinodos_generados = ubicar_antinodo_full([antena1, antena2], mapa)

            # Agregar antinodos a la lista con sus descripciones
            for antinodo in antinodos_generados:
                antinodos.append(antinodo)
            return

        # Recursivamente intentar agregar más índices
        for i in range(start, len(antenas)):
            generar_antinodos(indices + [i], i + 1)

    # Lista para almacenar los antinodos generados
    antinodos = []

    # Iniciar la recursión para generar combinaciones
    generar_antinodos([], 0)

    return antinodos, etiqueta
def ubicar_antinodo_full(antenas, mapa):
    '''
    Dada una lista de dos tuplas que representan la ubicación de 
    dos antenas, devuelve una lista de tuplas con la ubicación de los antinodos
    hasta completar todo el limite del mapa. Incluye a las dos antenas como antinodos.    
    '''
    antena1 = antenas[0]
    antena2 = antenas[1]
    vector = tuple(map(lambda x ,y: x - y, antena1, antena2))
    limite_x = len(mapa.columns)
    limite_y = len(mapa)
    n = 1
    antinodos = [antena1, antena2]
    
    #el while no corta
    while n < limite_x and n < limite_y:
        a1 = tuple(map(lambda x ,y: x + y*n, antena1, vector)) # primer antinodo
        a2 = tuple(map(lambda x ,y: x - y*n, antena2, vector)) # segundo antinodo
        antinodos.append(a1)
        antinodos.append(a2)
        n += 1
    return antinodos

def encontrar_antinodos_mapa_full(mapa, elementos):
    mapa_antinodos = mapa.copy()
    limite_x = len(mapa.columns)
    limite_y = len(mapa)
    antenas = []
    for elemento in elementos:
        antena = ubicar_elemento(mapa, elemento)
        antenas.append(antena)
    lista_anti = []
    for antena in antenas:
        if antena[1] != ".":
            antinodo, elemento = calcular_antinodos_full(antena, mapa)
            lista_anti.append(antinodo)
    
    antinodos = antinodos_unicos(lista_anti)
    contador_antinodo = 0
    for anti in antinodos:
        x, y = anti
        if -1 < x < limite_x and -1 < y < limite_y:
            contador_antinodo += 1
            if mapa_antinodos.loc[x, y] == ".":
                mapa_antinodos.loc[x, y] = "#"
    return mapa_antinodos, contador_antinodo

#%% test1
txt = ["............",
       "........0...",
       ".....0......",
       ".......0....",
       "....0.......",
       "......A.....",
       "............",
       "............",
       "........A...",
       ".........A..",
       "............",
       "............"]

mapa = procesar_txt(txt)
elementos = extraer_valores_unicos(txt)
#%%

mapa_antinodos, contador_antinodo = encontrar_antinodos_mapa(mapa, elementos)
 # =contar_antinodo(mapa_antinodos)
#%%test1
ceros = ubicar_elemento(mapa, "0")
a = ubicar_elemento(mapa, "A")

anti_a = calcular_antinodos(a)
anti_c = calcular_antinodos(ceros)

anti1=ceros[0][3]
anti2=ceros[0][0]
u = ubicar_antinodo([anti1, anti2])
#%% test2
# a = ubicar_elemento(mapa, "A")
# anti1=a[0][1]
# anti2=a[0][2]
# u = ubicar_antinodo_full([anti1, anti2], mapa)
anti_full, contar = encontrar_antinodos_mapa_full(mapa, elementos)
#%% input

txt = leer_txt("input.txt")
mapa = procesar_txt(txt)
elementos = extraer_valores_unicos(txt)

# solucion parte 1
mapa_antinodos, contar_parte1 = encontrar_antinodos_mapa(mapa, elementos)
# solucion parte 2
anti_full, contar_parte2 = encontrar_antinodos_mapa_full(mapa, elementos)