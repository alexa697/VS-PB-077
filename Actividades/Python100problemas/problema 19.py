#problema 19
#Generar n´umeros aleatorios con distintas distribuciones.

import random
import numpy as np # type: ignore

# Distribución uniforme
uniforme = random.uniform(0, 10)
print(f"Uniforme: {uniforme}")

# Distribución normal
normal = np.random.normal(loc=0, scale=1, size=5)
print(f"Normal: {normal}")

# Distribución binomial
binomial = np.random.binomial(n=10, p=0.5, size=5)
print(f"Binomial: {binomial}")
