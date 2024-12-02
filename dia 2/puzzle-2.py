# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 08:52:43 2024

@author: Fede
"""

def leer_txt(archivo):
    '''
    Devuelve una lista con listas de numeros por reporte
    '''
    lista = []
    with open(archivo, "r") as f:
        for line in f.readlines():
            # print(line)
            aux = line.strip().split()
            for i, dato in enumerate(aux):
                aux[i] = int(dato)
            lista.append(aux)
    return lista

def procesar_reportes(datos):
    lista_saltos = saltos_nivel(datos)
    lista_cumple = decrece_o_crece(datos, lista_saltos)
    return lista_cumple

def saltos_nivel(lista):
    lista_cumple = []
    for reporte in lista:
        lista_cumple.append(no_salta(reporte))
    return lista_cumple

def no_salta(reporte):
    cumple = False
    for i, dato in enumerate(reporte):
        if i+1 < len(reporte):
            diferencia = abs(dato - reporte[i+1])
            if diferencia > 0 and diferencia <= 3:
                cumple = True
            else:
                cumple = False
                break
    return cumple

def decrece_o_crece(lista, lista_cumple):
    lista_crece_decrece = lista_cumple.copy()
    for i, reporte in enumerate(lista):
        cumple = False
        if lista_cumple[i]:
            cumple = decrece(reporte)
            if not cumple:
                cumple = crece(reporte)
        lista_crece_decrece[i] = cumple
    return lista_crece_decrece

def decrece(reporte):
    return all(i < j for i, j in zip(reporte, reporte[1:]))

def crece(reporte):
    return all(i > j for i, j in zip(reporte, reporte[1:]))

def remover_nivel(datos, lista_cumple):
    lista_remover = lista_cumple.copy()
    for i, reporte in enumerate(datos):
        if not lista_remover[i]:
            for j in range(len(reporte)):  # Iterar sobre los índices de niveles en reporte
                # Crear una copia del reporte y eliminar el nivel en la posición j
                reporte_modificado = reporte[:j] + reporte[j+1:]
                
                # Verificar las condiciones sobre la lista modificada
                if no_salta(reporte_modificado):
                    if decrece(reporte_modificado) or crece(reporte_modificado):
                        lista_remover[i] = True
                        break  # Terminar el bucle interno al encontrar un caso válido
    return lista_remover
        
#%%
test = [[7,6,7,4,2,1], [1,2,7,8,9], [9,7,6,2,1], [1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9,]]   

lista_saltos = saltos_nivel(test)
lista_crece_decrece = decrece_o_crece(test, lista_saltos)
lista_remover = remover_nivel(test, lista_crece_decrece)

#%%
datos = leer_txt("input-2.txt")
# datos_procesados = procesar_reportes(datos)
# print(sum(datos_procesados))
# datos_procesados_atenuados = remover_nivel(datos, datos_procesados)
# print(sum(datos_procesados_atenuados))
ls = saltos_nivel(datos)
lc = decrece_o_crece(datos, ls)
lr = remover_nivel(datos, lc)
print(sum(lc))
print(sum(lr))
