import os
import random
import time

# Limpiar la pantalla
os.system('cls')

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [elemento for elemento in arr[1:] if elemento <= pivote]
        mayores = [elemento for elemento in arr[1:] if elemento > pivote]

        return quicksort(menores) + [pivote] + quicksort(mayores)

# Obtener el tiempo inicial
tiempo_inicial = time.time()

# Ejecutar el código
random.seed(42)
array_a_ordenar = [random.randint(1, 1000) for _ in range(1000)]
print(f"Arreglo original: {array_a_ordenar}\n")
array_ordenado = quicksort(array_a_ordenar)
print(f"\nArreglo final: {array_ordenado}")

# Obtener el tiempo final
tiempo_final = time.time()

# Calcular el tiempo total de ejecución
tiempo_total = tiempo_final - tiempo_inicial
print(f"\nTiempo total de ejecución: {tiempo_total} segundos")
