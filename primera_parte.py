"""
PRÁCTICO SEGUNDO - CURSO GIT ESSENTIALS
Ocaña Jeremias; Sabio Santiago
"""

# PRIMERA PARTE
# Ejercicio N° 2: Suma de Riemann para una función de una variable independiente

import math as m

# Funciones
def f(x):
    y = m.sqrt(1 - x**2)
    return y

def g(x):
    y = x**2 - 4
    return y

# Intervalos
fi = -1
ff = 1
gi = -2
gf = 3

# N° de rectángulos
n = 20

# f(x): Cálculo de área (punto medio)
area = 0
dx = (ff - fi) / n  # Base de los recángulos

for i in range(n):
    # base_i = fi + dx*i
    altura_i = f(((fi + dx*i) + (fi + dx*(i + 1)))/2)
    area_i = altura_i * dx
    area += area_i
print("El área de f(x) por punto medio es:", area)

# g(x): Cálculo de área (punto medio)
area = 0
dx = (gf - gi) / n  # Base de los recángulos

for i in range(n):
    # base_i = fi + dx*i
    altura_i = g(((gi + dx*i) + (gi + dx*(i + 1)))/2)
    area_i = altura_i * dx
    area += area_i
print("El área de g(x) por punto medio es:", area)

