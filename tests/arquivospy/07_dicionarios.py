"""Módulo de manipulação de dicionários."""


def mesclar_dicionarios(dict_a, dict_b):
    """Mescla dois dicionários, priorizando o segundo."""
    resultado = dict_a.copy()
    resultado.update(dict_b)
    return resultado


def inverter_dicionario(dicionario):
    """Inverte chaves e valores de um dicionário."""
    return {v: k for k, v in dicionario.items()}


def filtrar_por_valor(dicionario, valor_minimo):
    """Filtra entradas cujo valor é maior ou igual ao mínimo."""
    return {k: v for k, v in dicionario.items() if v >= valor_minimo}


def contar_ocorrencias(lista):
    """Conta a ocorrência de cada elemento em uma lista."""
    contagem = {}
    for item in lista:
        contagem[item] = contagem.get(item, 0) + 1
    return contagem
