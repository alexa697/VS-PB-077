#Problema 10
#leer, escribir y modificar un archivo
# Método 1: con la palabra reservada with

with open("Holiiiii.py","w") as variable1:
    print("Payaso = 1", file=variable1)
    


# Método 2: con variable

variable2 = open("holi.txt","w")

#Si se hace con el método 2, es necesario cerrar la variable
print("Hola mundo desde North Korea", file=variable2)

variable2.close()