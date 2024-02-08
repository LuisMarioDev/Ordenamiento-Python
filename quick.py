import os
os.system('cls')

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [elemento for elemento in arr[1:] if elemento <= pivote]
        mayores = [elemento for elemento in arr[1:] if elemento > pivote]
        print(f"Paso: {arr}")
        return quicksort(menores) + [pivote] + quicksort(mayores)

# Ejemplo de uso:
array_a_ordenar = [64, 25, 12, 22, 11]
print(f"Arreglo original: {array_a_ordenar}\n")

array_ordenado = quicksort(array_a_ordenar)
print(f"\nArreglo final: {array_ordenado}")
