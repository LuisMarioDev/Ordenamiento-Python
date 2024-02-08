import os
os.system('cls')

def seleccion_sort(arr):
    n = len(arr)
    print(f"Arreglo inicial: {arr}\n")

    for i in range(n - 1):
        indice_minimo = i

        for j in range(i + 1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
        if indice_minimo != i:
            arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]
        print(f"Paso: {arr}")
    return arr

# Ejemplo de uso:
array_a_ordenar = [64, 25, 12, 22, 11]

array_ordenado = seleccion_sort(array_a_ordenar)
print(f"\nArreglo final: {array_ordenado}")
