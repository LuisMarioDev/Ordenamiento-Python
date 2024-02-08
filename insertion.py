import os
os.system('cls')

def insertion_sort(arr):
    n = len(arr)
    print(f"Arreglo original: {arr}\n")

    for i in range(1, n):
        valor_actual = arr[i]
        posicion = i - 1

        while posicion >= 0 and arr[posicion] > valor_actual:
            arr[posicion + 1] = arr[posicion]
            posicion -= 1

        arr[posicion + 1] = valor_actual
        print(f"Paso: {arr}")
    return arr

# Ejemplo de uso:
array_a_ordenar = [64, 25, 12, 22, 11]

array_ordenado = insertion_sort(array_a_ordenar)
print(f"\nArreglo final: {array_ordenado}")
