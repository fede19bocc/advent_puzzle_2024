# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:12:11 2024

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
    locs = tuple((mapa.index[idx], mapa.columns[col]) for idx, col in zip(filas, columnas))
    return locs

def ubicar_guardia(mapa):
    for guardia in ["<", ">", "^", "v"]:
        posicion = ubicar_elemento(mapa, guardia)
        if posicion != ():
            return posicion[0], guardia
    return None

def recorrer_mapa(mapa):
    obstaculos = ubicar_elemento(mapa, "#")
    inicio, guardia = ubicar_guardia(mapa)
    # recorro hacia arriba
    mapa.loc[inicio[0], inicio[1]] ="X"
    dentro_del_mapa = True
    while dentro_del_mapa:
        inicio = arriba(mapa, inicio, obstaculos)
        if inicio[0] == 0 or inicio[1] == 0:
            dentro_del_mapa = False
        else:
            inicio = derecha(mapa, inicio, obstaculos)
        if inicio[0] == 0 or inicio[1] == 0:
            dentro_del_mapa = False
        else:
            inicio = abajo(mapa, inicio, obstaculos)
        if inicio[0] == 0 or inicio[1] == 0:
            dentro_del_mapa = False
        else:
            inicio = izquierda(mapa, inicio, obstaculos)
        if inicio[0] == 0 or inicio[1] == 0:
            dentro_del_mapa = False
        

def arriba(mapa, inicio, obstaculos):
    for i in reversed(range(inicio[0])):
        for o in obstaculos:
            if o == (i, inicio[1]):
                fila, col = o 
                return (fila + 1, col)  
            elif mapa.loc[i, inicio[1]] == ".":
                mapa.loc[i, inicio[1]] = "X"
    return (0,0)
                
def abajo(mapa, inicio, obstaculos):
    for i in range(inicio[0], len(mapa)):
        for o in obstaculos:
            if o == (i, inicio[1]):
                fila, col = o 
                return (fila - 1, col) 
            elif mapa.loc[i, inicio[1]] == ".":
                mapa.loc[i, inicio[1]] = "X"
    return (0,0)

def derecha(mapa, inicio, obstaculos):
    for i in range(inicio[1], len(mapa)):
        for o in obstaculos:
            if o == (inicio[0], i):
                fila, col = o 
                return (fila, col - 1) 
            elif mapa.loc[inicio[0], i] == ".":
                mapa.loc[inicio[0], i] = "X"
    return (0,0)

def izquierda(mapa, inicio, obstaculos):
    for i in reversed(range(inicio[1])):
        for o in obstaculos:
            if o == (inicio[0], i):
                fila, col = o 
                return (fila, col + 1)
            elif mapa.loc[inicio[0], i] == ".":
                mapa.loc[inicio[0], i] = "X"
    return (0,0)

def contar_X(mapa):
    letra = "X"
    conteo = mapa.map(lambda x: str(x).count(letra)).sum().sum()
    return conteo

# parte 2
# cuando tengo un loop se van a repetir siempre 4 posiciones de inicio
# entonces si se vuelven a repetir las 4 ultimas posiciones estoy en un loop
def loop():
    pass

# para generar un loop tengo que poner un obstaculo de forma que me genere un rectangulo
def nuevo_obstaculo():
    pass
#%% test
txt = ["....#.....",
       ".........#",
       "..........",
       "..#.......",
       ".......#..",
       "..........",
       ".#..^.....",
       "........#.",
       "#.........",
       "......#..."]

mapa = procesar_txt(txt)
# obstaculos = ubicar_elemento(mapa, "#")
# posicion, guardia = ubicar_guardia(mapa)

recorrer_mapa(mapa)
conteo = contar_X(mapa)
print(f"El guardia visita {conteo} posiciones")
#%% parte 1
txt = leer_txt("input.txt")
mapa = procesar_txt(txt)
recorrer_mapa(mapa)
conteo = contar_X(mapa)
print(f"El guardia visita {conteo} posiciones")