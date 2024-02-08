import os
import random
os.system('cls')

def seleccion_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        indice_minimo = i

        for j in range(i + 1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
        if indice_minimo != i:
            arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

    return arr

# Ejemplo de uso:
random.seed(42)
array_a_ordenar = [random.randint(1, 1000) for _ in range(1000)]
print(f"Arreglo original: {array_a_ordenar}\n")

array_ordenado = seleccion_sort(array_a_ordenar)
print(f"\nArreglo final: {array_ordenado}")
