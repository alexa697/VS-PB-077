#problema 17

#Implementar estructuras de datos b´asicas: pila, cola y lista enlazada.

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def agregar(self, item):
        self.items.append(item)

    def quitar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def tamaño(self):
        return len(self.items)


from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()

    def esta_vacia(self):
        return len(self.items) == 0

    def agregar(self, item):
        self.items.append(item)

    def quitar(self):
        if not self.esta_vacia():
            return self.items.popleft()
        return None

    def tamaño(self):
        return len(self.items)


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

