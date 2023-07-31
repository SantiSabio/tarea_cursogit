"""
PRÁCTICO SEGUNDO - CURSO GIT ESSENTIALS
Ocaña Jeremias; Sabio Santiago
"""

# SEGUNDA PARTE
# VECTORES

import math as m
import numpy as np

# Función para calcular la norma del vector ingresado
def calcular_norma(vector):
    norma = 0
    # Se interpreta el vector como un arreglo de longitud n (permite calcular la norma de un vector de cualquier dimensión)
    for i in vector:
        # Se suman los cuadrados de las componentes del vector y se calcula su raíz
        norma += i**2
    norma = m.sqrt(norma)
    return norma

# Se genera un vector aleatorio, en este caso de 3 dimensiones
vector = np.random.randint(1, 100, size = 3)
print("Vector generado:", vector)

print("La norma del vector es:", calcular_norma(vector))




