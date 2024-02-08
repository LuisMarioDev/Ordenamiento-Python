import os
import random
os.system('cls')

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


#Ejemplo
random.seed(42)
array_a_ordenar = [random.randint(1, 1000) for _ in range(1000)]
print(f"Arreglo original: {array_a_ordenar}\n")


array_ordenado = bubble_sort(array_a_ordenar)
print(f"\nArreglo final: {array_ordenado}")