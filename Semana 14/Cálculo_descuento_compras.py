# Universidad Estatal Amazónica
# cálculo de descuento en compras
# Luis Flores
# 19/09/2025

# Función para calcular el descuento
def calcular_descuento(valor_total, porcentaje_descuento=10):  # Define una función con un valor por defecto del 10% de descuento
    descuento = valor_total * (porcentaje_descuento / 100)     # Calcula el descuento multiplicando el valor total por el porcentaje
    return descuento                                           # Retorna el valor del descuento calculado

# Programación:

# Primera llamada: Usando el valor por defecto de 10%
valor1 = 500.0                           # Define el valor total de la primera compra
descuento1 = calcular_descuento(valor1)  # Llama a la función sin especificar porcentaje (usa 10% por defecto)
total_pagar1 = valor1 - descuento1       # Calcula el total a pagar restando el descuento al valor original

print("--Compra 1--")                                            # Muestra el encabezado de la primera compra
print(f"Valor total: ${valor1:.2f}")                             # Imprime el valor original de la compra
print(f"Descuento aplicado (10%): ${descuento1:.2f}")            # Imprime el descuento calculado (10%)
print(f"Valor final a pagar: ${total_pagar1:.2f}\n")             # Imprime el valor final después del descuento

# Segunda llamada: especificando un porcentaje diferente
valor2 = 300.0                                # Define el valor total de la segunda compra
porcentaje2 = 15                              # Define el porcentaje de descuento a aplicar (15%)
descuento2 = calcular_descuento(valor2, porcentaje2)  # Llama a la función con un porcentaje específico
total_pagar2 = valor2 - descuento2            # Calcula el total a pagar restando el descuento

print("--Compra 2--")                                                  # Muestra el encabezado de la segunda compra
print(f"Valor total: ${valor2:.2f}")                               # Imprime el valor original de la compra
print(f"Descuento aplicado ({porcentaje2}%): ${descuento2:.2f}")   # Imprime el descuento aplicado (15%)
print(f"Valor final a pagar: ${total_pagar2:.2f}")                 # Imprime el valor final después del descuento
