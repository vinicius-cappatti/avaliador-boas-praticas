"""Módulo com classe Pessoa."""

class pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

    def cumprimentar( self ):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

    def eh_maior_de_idade(self):
        return self.idade>=18

    def aniversario(self):
        self.idade+=1
        return self.idade
