"""Módulo de manipulação de matrizes."""


def criar_matriz(linhas, colunas, valor=0):
    """Cria uma matriz preenchida com um valor padrão."""
    return [[valor for _ in range(colunas)] for _ in range(linhas)]


def transpor(matriz):
    """Retorna a matriz transposta."""
    if not matriz:
        return []
    return [[matriz[i][j] for i in range(len(matriz))]
            for j in range(len(matriz[0]))]


def somar_matrizes(a, b):
    """Soma duas matrizes de mesma dimensão."""
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Matrizes devem ter mesma dimensão.")
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def multiplicar_por_escalar(matriz, escalar):
    """Multiplica todos os elementos da matriz por um escalar."""
    return [[elemento * escalar for elemento in linha]
            for linha in matriz]
