import os
import random
import time

os.system('cls')

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        valor_actual = arr[i]
        posicion = i - 1

        while posicion >= 0 and arr[posicion] > valor_actual:
            arr[posicion + 1] = arr[posicion]
            posicion -= 1

        arr[posicion + 1] = valor_actual

    return arr

tiempo_inicial = time.time()

# Ejemplo de uso:
random.seed(42)
array_a_ordenar = [random.randint(1, 1000) for _ in range(1000)]
print(f"Arreglo original: {array_a_ordenar}\n")

array_ordenado = insertion_sort(array_a_ordenar)
print(f"\nArreglo final: {array_ordenado}")

tiempo_final = time.time()

tiempo_total = tiempo_final - tiempo_inicial
print(f"\nTiempo total de ejecución: {tiempo_total} segundos")
