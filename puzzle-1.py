
def leer_txt(archivo):
    '''
    Devuelve el texto adentro del archivo
    '''
    lista_1 = []
    lista_2 = []
    with open(archivo, "r") as f:
        for line in f.readlines():
            # print(line)
            aux = line.strip().split()
            # print(aux)
            if len(aux) >= 2:
                lista_1.append(int(aux[0]))
                lista_2.append(int(aux[1]))
        return lista_1, lista_2

def distancia_entre_listas(lista_1, lista_2):
    a = lista_1.copy()
    b = lista_2.copy()
    distancias = []

    for i in range(len(lista_1)):
        distancia = abs(min(a) - min(b))
        distancias.append(distancia)
        a.remove(min(a))
        b.remove(min(b))
    
    return sum(distancias)

def puntaje_de_similitud(lista_1, lista_2):
    puntaje = []
    cantidades_lista_2 = dicc_contar_num(lista_2)

    for i in lista_1:
        if i not in cantidades_lista_2:
            puntaje.append(0)
        else:
            puntaje.append(cantidades_lista_2[i] * i)
    return sum(puntaje)

def dicc_contar_num(lista):
    contar = {}
    for i in lista:
        if i not in contar:
            contar[i] = 1
        else:
            contar[i] += 1
    return contar

# lista ejemplos
a = [3,4,2,1,3,3]
b = [4,3,5,3,9,3]

# listas input
lista_1, lista_2 = leer_txt("input.txt")

dicc = dicc_contar_num(lista_2)
# for i in lista_1:
#     if i in dicc:
#         print(dicc[i])

print(lista_1)

print("distancia entre listas" , distancia_entre_listas(lista_1, lista_2))
print("puntaje de similitud: " , puntaje_de_similitud(lista_1, lista_2))