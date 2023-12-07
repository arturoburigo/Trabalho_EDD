import random
import time

# Função para gerar um vetor com 10 mil elementos aleatórios
def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Gerar um vetor com 10 mil elementos aleatórios
array = generate_random_array(10000)

# Fazer cópias do vetor para ordenar com diferentes algoritmos
array_bubble = array.copy()
array_insertion = array.copy()
array_merge = array.copy()
array_quick = array.copy()

# Medir o tempo de execução de cada algoritmo
start_time = time.time()
bubble_sort(array_bubble)
bubble_time = time.time() - start_time

start_time = time.time()
insertion_sort(array_insertion)
insertion_time = time.time() - start_time

start_time = time.time()
merge_sort(array_merge)
merge_time = time.time() - start_time

start_time = time.time()
array_quick = quick_sort(array_quick)
quick_time = time.time() - start_time

# Imprimir os tempos de execução de cada algoritmo
print(f"Tempo de execução do Bubble Sort: {bubble_time:.6f} segundos")
print(f"Tempo de execução do Insertion Sort: {insertion_time:.6f} segundos")
print(f"Tempo de execução do Merge Sort: {merge_time:.6f} segundos")
print(f"Tempo de execução do Quick Sort: {quick_time:.6f} segundos")


