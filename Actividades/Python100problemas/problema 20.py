#problema 20
#Implementar b´usqueda binaria y lineal

def busqueda_lineal(lista, valor):
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return i
    return -1

# Ejemplo
lista = [1, 3, 5, 7, 9]
resultado = busqueda_lineal(lista, 5)
print(f'Índice: {resultado}')  # 2

def busqueda_binaria(lista, valor):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Ejemplo
lista = [1, 3, 5, 7, 9]
resultado = busqueda_binaria(lista, 5)
print(f'Índice: {resultado}')  # 2