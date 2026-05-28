"""Módulo de ordenação de listas."""


def bubble_sort(lista):
    """Ordena uma lista usando Bubble Sort."""
    copia = lista.copy()
    n = len(copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            if copia[j] > copia[j + 1]:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
    return copia


def selection_sort(lista):
    """Ordena uma lista usando Selection Sort."""
    copia = lista.copy()
    n = len(copia)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if copia[j] < copia[menor]:
                menor = j
        copia[i], copia[menor] = copia[menor], copia[i]
    return copia


def insertion_sort(lista):
    """Ordena uma lista usando Insertion Sort."""
    copia = lista.copy()
    for i in range(1, len(copia)):
        chave = copia[i]
        j = i - 1
        while j >= 0 and copia[j] > chave:
            copia[j + 1] = copia[j]
            j -= 1
        copia[j + 1] = chave
    return copia
