# Universidad Estatal Amazónica
# Archivos de Texto en Python
# Luis Flores
# 05/10/2025

# Escritura de Archivo

# Abrimos (o creamos si no existe) el archivo 'my_notes.txt' en modo escritura ('w')
# El modo 'w' sobrescribe el contenido si el archivo ya existe
archivo = open("my_notes.txt", "w")  # open() crea un objeto archivo; 'w' indica escritura

# Escribimos tres notas personales en el archivo usando write()
# Cada nota termina con '\n' para que aparezca en una línea distinta
archivo.write("Nota 1: Estudiar Python todos los días.\n")  # Escribe la primera nota con salto de línea
archivo.write("Nota 2: Generar ordenes de trabajo.\n")  # Escribe la segunda nota con salto de línea
archivo.write("Nota 3: Cambiar de aceite al auto.\n")  # Escribe la tercera nota con salto de línea

# Cerramos el archivo para guardar los cambios
archivo.close()  # Cierra el archivo y asegura que se guarden los datos escritos


# Lectura de Archivo


# Abrimos el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")  # 'r' indica que abrimos el archivo solo para leer

# Leemos línea por línea utilizando readline()
# Cada llamada a readline() devuelve la siguiente línea del archivo
print("Contenido del archivo:\n")  # Muestra un título antes de imprimir las líneas

linea = archivo.readline()   # Lee la primera línea del archivo
while linea:                 # Bucle que se ejecuta mientras haya contenido en 'linea'
    print(linea.strip())     # Imprime la línea sin espacios ni saltos de línea extra
    linea = archivo.readline()   # Lee la siguiente línea del archivo

# Cerramos el archivo después de leer
archivo.close()  # Cierra el archivo de lectura para liberar recursos
