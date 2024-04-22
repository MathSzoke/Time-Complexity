def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Este algoritmo de busca linear tem complexidade
# O(n) porque, no pior caso, precisa percorrer todos
# os elementos da lista.
