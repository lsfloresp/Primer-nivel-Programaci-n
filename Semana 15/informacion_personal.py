# Universidad Estatal Amazónica
# Diccionario información_personal
# Luis Flores
# 28/09/2025

# Paso 1: Crear un diccionario


# Creamos un diccionario llamado 'informacion_personal'
informacion_personal = {
    "nombre": "Luis Flores",   # Clave "nombre" con valor "Luis Flores"
    "edad": 36,                 # Clave "edad" con valor 36
    "ciudad": "Latacunga",          # Clave "ciudad" con valor "Latacunga"
    "profesion": "Estudiante"   # Clave "profesion" con valor "Estudiante"
}

# Imprimimos el diccionario inicial para ver cómo empieza
print("Diccionario inicial:")
print(informacion_personal)
print()  # Línea en blanco para separar salidas



# Paso 2: Acceder y modificar valores


# Mostramos el valor actual de la clave "ciudad"
print("Ciudad actual (antes):", informacion_personal["ciudad"])

# Modificamos el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Quito"  # Latacunga -> Quito

# Mostramos el nuevo valor de la clave "ciudad"
print("Ciudad modificada (después):", informacion_personal["ciudad"])
print()



# Paso 3: Agregar nueva clave-valor


# Agregamos una nueva clave llamada "profesion_detalle"
informacion_personal["profesion_detalle"] = "Ingeniero Tecnologías de la Información"

# Imprimimos el diccionario para verificar que la nueva clave se agregó
print("Diccionario después de agregar 'profesion_detalle':")
print(informacion_personal)
print()



# Paso 4: Verificar existencia de clave y agregarla si no existe


# Verificamos si la clave "telefono" ya existe en el diccionario
if "telefono" not in informacion_personal:
    # Como no existe, la agregamos con un valor
    informacion_personal["telefono"] = "+593992662143"
    print("Se agregó 'telefono':", informacion_personal["telefono"])
else:
    # Si ya existiera, solo mostramos su valor
    print("La clave 'telefono' ya existe:", informacion_personal["telefono"])

# Mostramos el diccionario después de verificar/agregar 'telefono'
print("Diccionario después de verificar/agregar 'telefono':")
print(informacion_personal)
print()



# Paso 5: Eliminar una clave


# Verificamos si la clave "edad" existe en el diccionario
if "edad" in informacion_personal:
    # Si existe, la eliminamos con pop()
    informacion_personal.pop("edad")
    print("Se eliminó la clave 'edad'.")
else:
    # Si no existe, avisamos que no se pudo eliminar
    print("La clave 'edad' no existe, nada que eliminar.")

# Mostramos el diccionario después de eliminar "edad"
print("Diccionario después de eliminar 'edad':")
print(informacion_personal)