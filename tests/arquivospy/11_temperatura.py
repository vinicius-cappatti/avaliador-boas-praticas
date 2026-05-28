"""Módulo de conversão de temperaturas."""


def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_para_kelvin(celsius):
    """Converte Celsius para Kelvin."""
    return celsius + 273.15


def kelvin_para_celsius(kelvin):
    """Converte Kelvin para Celsius."""
    if kelvin < 0:
        raise ValueError("Kelvin não pode ser negativo.")
    return kelvin - 273.15
