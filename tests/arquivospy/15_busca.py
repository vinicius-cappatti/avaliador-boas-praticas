"""Módulo de busca em listas."""


def busca_linear(lista, alvo):
    """Realiza busca linear e retorna o índice do elemento."""
    for i, item in enumerate(lista):
        if item == alvo:
            return i
    return -1


def busca_binaria(lista, alvo):
    """Realiza busca binária em uma lista ordenada."""
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def buscar_todos(lista, alvo):
    """Retorna todos os índices onde o alvo aparece."""
    return [i for i, item in enumerate(lista) if item == alvo]
