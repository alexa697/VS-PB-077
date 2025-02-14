#Problema 14
#Implementar distintos m´etodos de ordenamiento.
# Inicializamos una lista vacía
lista_dinamica = []
print("Escribe 'fin' cuando quieras terminar.")

# Bucle para agregar elementos
while True:
    # Pedimos al usuario que ingrese un elemento
    elemento = input("Ingresa un valor (o escribe 'fin' para terminar): ")

    # Si el usuario escribe 'fin', terminamos el bucle
    if elemento.lower() == 'fin':
        break
    
    # Intentamos agregar el elemento a la lista
    # Si el elemento es un número, lo convertimos a entero
    try:
        elemento = int(elemento)
    except ValueError:
        pass  # Si no es un número, lo dejamos como un string

    # Añadimos el elemento a la lista
    lista_dinamica.append(elemento)

#TIPOS DE ORDENAMIENTOS
    
# Ordenamiento por burbuja (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Ordenamiento por inserción (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and clave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr

# Ordenamiento por selección (Selection Sort)
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ordenamiento rápido (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Función principal para probar los métodos de ordenamiento
def probar_metodos_ordenamiento():
    # Crear una lista de ejemplo
    print("Lista original:", lista_dinamica)
    
    # Probar el método de burbuja
    lista_bubble = lista_dinamica.copy()
    print("Ordenamiento por burbuja:", bubble_sort(lista_bubble))
    
    # Probar el método de inserción
    lista_insertion = lista_dinamica.copy()
    print("Ordenamiento por inserción:", insertion_sort(lista_insertion))
    
    # Probar el método de selección
    lista_selection = lista_dinamica.copy()
    print("Ordenamiento por selección:", selection_sort(lista_selection))
    
    # Probar el método rápido
    lista_quick = lista_dinamica.copy()
    print("Ordenamiento rápido:", quick_sort(lista_quick))

# Llamada a la función principal
probar_metodos_ordenamiento()