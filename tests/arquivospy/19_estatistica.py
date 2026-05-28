"""Módulo de estatística básica."""


import math


def media(valores):
    """Calcula a média aritmética."""
    if not valores:
        raise ValueError("Lista vazia.")
    return sum(valores) / len(valores)


def mediana(valores):
    """Calcula a mediana de uma lista de valores."""
    if not valores:
        raise ValueError("Lista vazia.")
    ordenados = sorted(valores)
    n = len(ordenados)
    meio = n // 2
    if n % 2 == 0:
        return (ordenados[meio - 1] + ordenados[meio]) / 2
    return ordenados[meio]


def variancia(valores):
    """Calcula a variância populacional."""
    if not valores:
        raise ValueError("Lista vazia.")
    m = media(valores)
    return sum((x - m) ** 2 for x in valores) / len(valores)


def desvio_padrao(valores):
    """Calcula o desvio padrão populacional."""
    return math.sqrt(variancia(valores))
