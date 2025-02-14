#problema 18
#Resolver ecuaciones cuadr´aticas.

import cmath

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a)
    return raiz1, raiz2

a, b, c = int(input("ingrese a: ")), int(input("ingrese b: ")), int(input("ingrese c: "))
raiz1, raiz2 = resolver_ecuacion_cuadratica(a, b, c)
print(f"Raíces: {raiz1}, {raiz2}")