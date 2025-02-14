#problema 15
#Determinar si un a˜no es bisiesto.

def es_bisiesto(año):
    # Si el año es divisible por 4 y no es divisible por 100, o si es divisible por 400, es bisiesto
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

año = int(input("Introduce un año para saber si es bisiesto: "))

if es_bisiesto(año):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")