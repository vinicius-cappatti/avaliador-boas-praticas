"""Módulo com classe Fila (Queue)."""


class Fila:
    """Implementação de uma fila simples."""

    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        """Adiciona um item ao final da fila."""
        self.itens.append(item)

    def desenfileirar(self):
        """Remove e retorna o primeiro item da fila."""
        if self.esta_vazia():
            raise IndexError("Fila vazia.")
        return self.itens.pop(0)

    def primeiro(self):
        """Retorna o primeiro item sem remover."""
        if self.esta_vazia():
            raise IndexError("Fila vazia.")
        return self.itens[0]

    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.itens) == 0

    def tamanho(self):
        """Retorna o tamanho da fila."""
        return len(self.itens)
