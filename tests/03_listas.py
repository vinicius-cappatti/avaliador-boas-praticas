"""Módulo com operações em listas."""


def encontrar_maximo(lista):
    """Encontra o valor máximo de uma lista."""
    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    return max(lista)


def encontrar_minimo(lista):
    """Encontra o valor mínimo de uma lista."""
    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    return min(lista)


def calcular_media(lista):
    """Calcula a média dos valores de uma lista."""
    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    return sum(lista) / len(lista)
