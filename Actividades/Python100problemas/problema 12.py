#problema 12
#Encontrar el mayor entre tres n´umeros dados.

n1=int(input("coloque el primer numero: "))
n2=int(input("coloque el segundo numero: "))
n3=int(input("coloque el tercer numero: "))
may=0

if n1>n2:
    may=n1
else:    
    may=n2
if n3>may:
    may=n3

print("el número mayor encontrado es:", may)
