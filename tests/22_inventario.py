"""Módulo com classe Inventário."""

class Item:
    def __init__(self,nome,quantidade,preco):
        self.nome=nome
        self.quantidade=quantidade
        self.preco=preco
    def valor_total(self):
        return self.quantidade*self.preco
    def __repr__(self):
        return f"Item({self.nome}, qtd={self.quantidade}, preco={self.preco})"

class Inventario:
    def __init__(self):
        self.itens={}
    def adicionar_item(self,nome,quantidade,preco):
        if nome in self.itens:
            self.itens[nome].quantidade+=quantidade
        else:
            self.itens[nome]=Item(nome,quantidade,preco)
    def remover_item(self,nome):
        if nome not in self.itens:
            raise KeyError(f"Item '{nome}' não encontrado")
        del self.itens[nome]
    def valor_total_inventario(self):
        total=0
        for item in self.itens.values():
            total+=item.valor_total()
        return total
    def listar_itens(self):
        return list(self.itens.values())
