

print("busqueda de arreglo multidimencional")


def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return True, (i, j)
    return False, (-1, -1)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz:")
for fila in matriz:
    print(fila)

# Aquí es donde se pediría el valor por teclado en un entorno de ejecución local
valor_a_buscar = int(input("Ingrese el valor a buscar en la matriz: "))

encontrado, posicion = buscar_en_matriz(matriz, valor_a_buscar)

if encontrado:
    print(f"Valor {valor_a_buscar} encontrado en la posición {posicion}.")
else:
    print(f"Valor {valor_a_buscar} no encontrado en la matriz.")

#programa 2
print("Programa 2: Ordenación de Arreglo Multidimensional")
def bubble_sort(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

def ordenar_fila_matriz(matriz, fila):
    bubble_sort(matriz[fila])
    return matriz

# Definimos una matriz 3x3
matriz = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 1, 8]
]

fila_a_ordenar = 0  # Ordenaremos la primera fila (index 0)

print("Matriz original:")
for fila in matriz:
    print(fila)

matriz_ordenada = ordenar_fila_matriz(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)