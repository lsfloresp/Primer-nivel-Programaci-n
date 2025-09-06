# Universidad Estatal Amazónica
# Iteración de arreglos multidimensionales con bucles anidados
# Luis Flores
# 07/09/2025

#Lista de ciudades
ciudades = ["Latacunga", "Ambato", "Quito"]

# Suponiendo 2 semanas de datos, 7 días por semana
# Estructura: temperaturas[ciudad][semana][dia]
temperaturas = [
    [  # Latacunga
        [20, 22, 21, 19, 18, 10, 11],  # Semana 1
        [19, 20, 20, 18, 17, 16, 18]   # Semana 2
    ],
    [  # Ambato
        [15, 16, 17, 18, 19, 20, 21],  # Semana 1
        [21, 20, 19, 18, 17, 16, 15]   # Semana 2
    ],
    [  # Quito
        [20, 21, 19, 18, 22, 23, 24],  # Semana 1
        [24, 23, 22, 21, 20, 19, 18]   # Semana 2
    ]
]

# Calcular y mostrar promedio de temperaturas por ciudad y semana
for i in range(len(ciudades)):
    print(f"\nPromedios para {ciudades[i]}:")
    for semana in range(len(temperaturas[i])):
        suma = sum(temperaturas[i][semana])
        promedio = suma / len(temperaturas[i][semana])
        print(f"  Semana {semana + 1}: {promedio:.2f} °C")