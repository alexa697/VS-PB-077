#Actividad 9
#Generar una lista de números pares e impares hasta un líımite dado.
print ("Lista")
limite = int(input("Ingresa el límite: "))
pares = [i for i in range(limite + 1) if i % 2 == 0]
impares = [i for i in range(limite + 1) if i % 2 != 0]
print("Números pares:", pares)
print("Números impares:", impares)
print("Fin de la lista")