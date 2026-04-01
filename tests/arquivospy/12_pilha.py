"""Módulo com classe Pilha (Stack)."""

class Pilha:
    def __init__( self ):
        self.itens = []

    def empilhar( self, item ):
        self.itens.append(item)

    def desempilhar(self):
        if self.esta_vazia():
            raise IndexError("Pilha vazia")
        return self.itens.pop()

    def topo( self ):
        if self.esta_vazia():
            raise IndexError("Pilha vazia")
        return self.itens[-1]

    def esta_vazia(self):
        return len( self.itens ) == 0

    def tamanho(self):
        return len(self.itens)
