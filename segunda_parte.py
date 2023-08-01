"""
PRÁCTICO SEGUNDO - CURSO GIT ESSENTIALS
Ocaña Jeremias; Sabio Santiago
"""

# SEGUNDA PARTE
# VECTORES

# Importamos numpy para poder generar vectores aleatorios
import numpy as np

# Definimos nuestra funcion producto escalar
def producto_escalar(v1, v2):
    # En caso de que nuestros vectores no sean de la misma longitud
    # nos dara como resultado None
    if len(v1) != len(v2):
        print("Los vectores deben tener la misma longitud.")
        return None
    
    # En caso de que nuestros vectores sean de la misma longitud
    # sumaremos los productos de las componentes correspondientes de los vectores
    # y devolveremos ese valor
    producto = sum(v1[i] * v2[i] for i in range(len(v1)))
    return producto


# utilizamos numpy para generar vectores aleatorios de tres componentes
# en este caso de que sus valores sean entre 1 y 9
vector1 = np.random.randint(1, 10, size=3)
vector2 = np.random.randint(1, 10, size=3)

# imprimimos en pantalla los vectores que se generaron
print("Vector 1:", vector1)
print("Vector 2:", vector2)

# y en caso de que los vectores sean de la misma cantidad de componentes
# mostraremos en pantalla el resultado
resultado = producto_escalar(vector1, vector2)
if resultado is not None:
    print("El producto escalar de los vectores es:", resultado)
