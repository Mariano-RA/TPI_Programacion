import random
import time
from tabulate import tabulate

# Algoritmos de ordenamiento

def burbuja(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def seleccion(arr):
    a = arr.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def insercion(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = random.choice(arr)
        menores = [x for x in arr if x < pivote]
        iguales = [x for x in arr if x == pivote]
        mayores = [x for x in arr if x > pivote]
        return quicksort(menores) + iguales + quicksort(mayores)

def mergesort(arr):
    if len(arr) > 1:
        medio = len(arr) // 2
        izq = arr[:medio]
        der = arr[medio:]
        mergesort(izq)
        mergesort(der)
        i = j = k = 0
        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                arr[k] = izq[i]
                i += 1
            else:
                arr[k] = der[j]
                j += 1
            k += 1
        while i < len(izq):
            arr[k] = izq[i]
            i += 1
            k += 1
        while j < len(der):
            arr[k] = der[j]
            j += 1
            k += 1
    return arr

# Algoritmos de búsqueda

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        mid = (izq + der) // 2
        if lista[mid] == objetivo:
            return mid
        elif lista[mid] < objetivo:
            izq = mid + 1
        else:
            der = mid - 1
    return -1

# Función para medir el tiempo de ejecución

def medir_tiempo(funcion, datos, objetivo=None):
    inicio = time.perf_counter()
    if objetivo is not None:
        funcion(datos, objetivo)
    else:
        funcion(datos)
    fin = time.perf_counter()
    return round((fin - inicio) * 1000, 4)

# Comparación de ordenamientos
def comparar_ordenamientos():
    tamaños = [500, 1000, 2000]
    formas = ["aleatoria", "ordenada", "invertida"]
    ordenamientos = [
        ("Burbuja", burbuja), 
        ("Selección", seleccion), 
        ("Inserción", insercion), 
        ("Quicksort", quicksort), 
        ("Mergesort", mergesort)
    ]

    tabla = []
    for tamaño in tamaños:
        for forma in formas:
            if forma == "aleatoria":
                lista = [random.randint(0, 10000) for _ in range(tamaño)]
            elif forma == "ordenada":
                lista = list(range(tamaño))
            else:
                lista = list(range(tamaño, 0, -1))

            fila = [f"{tamaño} / {forma.capitalize()}"]
            for _, algoritmo in ordenamientos:
                t = medir_tiempo(algoritmo, lista)
                fila.append(f"{round(t, 2)} ms")
            tabla.append(fila)

        
    print("\n\n=== COMPARACIÓN DE TIEMPOS DE ORDENAMIENTO ===")
    headers = ["Tamaño / Tipo"] + [nombre for nombre, _ in ordenamientos]
    print(tabulate(tabla, headers=headers, tablefmt="grid"))

# Comparación de búsqueda
def comparar_busquedas():
    longitud = [50, 100, 1000, 100000]
    objetivo = -1


    resultados = []
    for n in longitud:
        lista_ordenada = list(range(n))
        t_lineal = medir_tiempo(busqueda_lineal, lista_ordenada, objetivo)
        t_binaria = medir_tiempo(busqueda_binaria, lista_ordenada, objetivo)

        resultados.append([
            f"{n}",
            round(t_lineal, 4),
            round(t_binaria, 4)
        ])

    print("\n\n=== COMPARACIÓN DE TIEMPOS DE BÚSQUEDA ===")
    print(tabulate(resultados, headers=["Tamaño", "Lineal (ms)", "Binaria (ms)"], tablefmt="grid"))


if __name__ == "__main__":
    # Ejecutar comparaciones
    comparar_ordenamientos()
    comparar_busquedas()