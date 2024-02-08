import os
import random
os.system('cls')

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [elemento for elemento in arr[1:] if elemento <= pivote]
        mayores = [elemento for elemento in arr[1:] if elemento > pivote]

        return quicksort(menores) + [pivote] + quicksort(mayores)

# Ejemplo de uso:
random.seed(42)
array_a_ordenar = [random.randint(1, 1000) for _ in range(1000)]
print(f"Arreglo original: {array_a_ordenar}\n")

array_ordenado = quicksort(array_a_ordenar)
print(f"\nArreglo final: {array_ordenado}")
