#problema 13
#Convertir una temperatura entre distintas escalas.

def convertir_temperatura():
    print("Conversión de Temperaturas")
    print("1. Celsius a Fahrenheit")
    print("2. Celsius a Kelvin")
    print("3. Fahrenheit a Celsius")
    print("4. Fahrenheit a Kelvin")
    print("5. Kelvin a Celsius")
    print("6. Kelvin a Fahrenheit")
    
    # Solicitar opción de conversión
    opcion = int(input("Selecciona una opción (1-6): "))
    
    # Solicitar temperatura a convertir
    temperatura = float(input("Introduce la temperatura a convertir: "))

    if opcion == 1:
        # Celsius a Fahrenheit
        resultado = (temperatura * 9/5) + 32
        print(f"{temperatura} °C es igual a {resultado} °F")
    
    elif opcion == 2:
        # Celsius a Kelvin
        resultado = temperatura + 273.15
        print(f"{temperatura} °C es igual a {resultado} K")
    
    elif opcion == 3:
        # Fahrenheit a Celsius
        resultado = (temperatura - 32) * 5/9
        print(f"{temperatura} °F es igual a {resultado} °C")
    
    elif opcion == 4:
        # Fahrenheit a Kelvin
        celsius = (temperatura - 32) * 5/9
        resultado = celsius + 273.15
        print(f"{temperatura} °F es igual a {resultado} K")
    
    elif opcion == 5:
        # Kelvin a Celsius
        resultado = temperatura - 273.15
        print(f"{temperatura} K es igual a {resultado} °C")
    
    elif opcion == 6:
        # Kelvin a Fahrenheit
        celsius = temperatura - 273.15
        resultado = (celsius * 9/5) + 32
        print(f"{temperatura} K es igual a {resultado} °F")
    
    else:
        print("Opción inválida. Por favor, selecciona un número entre 1 y 6.")

# Llamada a la función
convertir_temperatura()