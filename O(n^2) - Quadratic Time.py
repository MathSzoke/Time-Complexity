def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# O algoritmo de ordenação bubble sort tem complexidade
# O(n^2) porque compara repetidamente pares de elementos
# adjacentes e os troca se estiverem na ordem errada.
