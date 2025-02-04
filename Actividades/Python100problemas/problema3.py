#Problema 3
#Calcula el factorial de un numero, donde "n" es el numero dado, e "i" el número de iteraciones a multiplicar
n = int(input("Inserte el número a calcular su factorial: "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print("El facorial de",n,"es: ",fact)
