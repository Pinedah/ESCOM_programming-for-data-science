import math

# Función que calcula la distribución normal general
def trapecios(n, mu=158, sigma=4):
    # Función de densidad de probabilidad de la normal general
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((n - mu)**2) / (2 * sigma**2))

# Parámetros
inicio = 160     # Inicio del intervalo
fin = 200       # Fin del intervalo
paso = 0.0008   # Paso de integración (más pequeño para mayor precisión)
area = 0        # Inicializar el área

# Sumar las áreas bajo la curva usando la regla del trapecio
while inicio <= fin:
    print(f"{inicio}\t-\t{area}")
    area += trapecios(inicio) * paso
    inicio += paso

# Imprimir el área total bajo la curva en el intervalo dado
print("Área bajo la curva (normal general):", area)

