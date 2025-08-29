# Universidad Estatal Amazónica
# Búsqueda en arreglo multidimensional
# Luis Flores
# 28/08/2025

# Definimos la matriz 3x3
numero = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mostrar la matriz
print("Matriz:")
for fila in numero:
    print(fila)

# Pedir el valor a buscar
valor = int(input("\nIngrese el número que desea buscar en la matriz: "))

# Variable para saber si se encontró
encontrado = False

# Recorrer cada fila
for i, fila in enumerate(numero):
    if valor in fila:
        j = fila.index(valor)  # obtenemos el índice de la columna
        print(f"El valor {valor} se encontró en la posición: fila {i}, columna {j}")
        encontrado = True
        break  # si solo queremos la primera coincidencia

# Si no se encontró
if not encontrado:
    print(f"El valor {valor} no se encontró en la matriz")