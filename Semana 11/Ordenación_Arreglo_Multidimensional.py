# Universidad Estatal Amazónica
# Búsqueda en arreglo multidimensional
# Luis Flores
# 28/08/2025

# Definimos la matriz 3x3
numero = [
    [31, 10, 15],
    [9, 15, 30],
    [13, 6, 80]
]
# Mostrar la matriz original
print("Matriz original:")
for fila in numero:
    print(fila)

# Pedir al usuario qué fila quiere ordenar
fila = int(input("\nIngrese el número de fila a ordenar (0, 1 o 2): "))

# Pedir si quiere ascendente o descendente
orden = input("¿Desea ordenar ascendente (A) o descendente (D)? ").strip().upper()

# Ordenar usando sort()
if orden == "A":
    numero[fila].sort()   # ascendente
else:
    numero[fila].sort(reverse=True)  # descendente

# Mostrar la matriz después del ordenamiento
print("\nMatriz después de ordenar la fila", fila, ":")
for fila in numero:
    print(fila)