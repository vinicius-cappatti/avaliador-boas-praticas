"""Módulo de calculadora básica."""


def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b


def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b


def dividir(a, b):
    """Retorna a divisão de dois números."""
    if b == 0:
        raise ValueError("Divisor não pode ser zero.")
    return a / b
