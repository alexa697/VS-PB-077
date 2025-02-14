Lista = []
print(bool(Lista))
#el enumerate es el unico dato complejo que siempre es true

list #listas
tuple #Variable que no cambia de valor
set #conjunto de datos 
dict #izquierda concepto, derecho significado
saludos = dict()

saludos["español"] = "Hola Mundo"
saludos["english"]= "Hello world"
saludos["fracais"]= "Bonjour mondieu"
saludos["japones"] = "Ohayo warudo"
saludos["portugues"]= "Saludo al macaco"

for (idioma, saludo) in saludos.items():
    print(idioma,saludo)

#for control in objetoiterable

primos = [1,2,3,5,7,11]

for num in range (1,1100):
    if num in primos:
        print(num)

