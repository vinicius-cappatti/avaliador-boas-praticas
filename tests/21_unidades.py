"""Módulo de conversão de unidades."""


def metros_para_centimetros(metros):
    """Converte metros para centímetros."""
    return metros * 100


def quilogramas_para_gramas(kg):
    """Converte quilogramas para gramas."""
    return kg * 1000


def litros_para_mililitros(litros):
    """Converte litros para mililitros."""
    return litros * 1000


def km_por_hora_para_m_por_segundo(kmh):
    """Converte km/h para m/s."""
    return kmh / 3.6


def graus_para_radianos(graus):
    """Converte graus para radianos."""
    import math
    return graus * (math.pi / 180)
