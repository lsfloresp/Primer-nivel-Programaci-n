# Universidad Estatal Amazónica
# Desarrollo de funciones para el calculo de temperaturas
# Luis Flores
# 14/09/2025


# Función principal para calcular promedios

def mostrar_temp():

    # Lista de ciudades
    ciudades = ["Latacunga", "Ambato", "Quito"]

    # Matriz tridimensional de temperaturas: [ciudad][semana][día]
    temperaturas = [
        [  # Latacunga
            [20, 22, 21, 19, 18, 10, 11],  # Semana 1
            [19, 20, 20, 18, 17, 16, 18],  # Semana 2
            [21, 20, 22, 19, 18, 17, 20],  # Semana 3
            [18, 19, 20, 21, 22, 20, 19]   # Semana 4
        ],
        [  # Ambato
            [15, 16, 17, 18, 19, 20, 21],  # Semana 1
            [21, 20, 19, 18, 17, 16, 15],  # Semana 2
            [18, 18, 19, 19, 20, 20, 21],  # Semana 3
            [22, 21, 20, 19, 18, 17, 16]   # Semana 4
        ],
        [  # Quito
            [20, 21, 19, 18, 22, 23, 24],  # Semana 1
            [24, 23, 22, 21, 20, 19, 18],  # Semana 2
            [19, 20, 21, 22, 23, 24, 25],  # Semana 3
            [25, 24, 23, 22, 21, 20, 19]   # Semana 4
        ]
    ]

    # Bucle para recorrer cada ciudad
    for i in range(len(ciudades)):
        print(f"\nPromedios para {ciudades[i]}:")  # Imprime el nombre de la ciudad

        # Bucle para recorrer cada semana dentro de la ciudad
        for semana in range(len(temperaturas[i])):
            suma = sum(temperaturas[i][semana])  # Suma de las temperaturas de la semana
            promedio = suma / len(temperaturas[i][semana])  # Promedio semanal
            print(f"  Semana {semana + 1}: {promedio:.2f} °C")  # Imprime el promedio



# Llamada a la función
mostrar_temp()

