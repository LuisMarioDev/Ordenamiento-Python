import os
os.system('cls')

def bubble_sort(arr):
    print(f"Arreglo original: {arr}\n")
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(f"Paso: {arr}")
    return arr


#Ejemplo
array_a_ordenar = [64, 25, 12, 22, 11]

array_ordenado = bubble_sort(array_a_ordenar)
print(f"\nArreglo final: {array_ordenado}")