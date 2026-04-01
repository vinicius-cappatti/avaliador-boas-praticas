"""Módulo de manipulação de datas."""


from datetime import datetime, timedelta


def dias_entre_datas(data_inicio, data_fim):
    """Calcula a diferença em dias entre duas datas."""
    delta = data_fim - data_inicio
    return abs(delta.days)


def adicionar_dias(data, dias):
    """Adiciona um número de dias a uma data."""
    return data + timedelta(days=dias)


def eh_ano_bissexto(ano):
    """Verifica se um ano é bissexto."""
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


def formatar_data(data, formato="%d/%m/%Y"):
    """Formata uma data para uma string."""
    return data.strftime(formato)


def data_atual():
    """Retorna a data atual."""
    return datetime.now()
