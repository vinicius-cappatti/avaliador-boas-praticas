"""Módulo com classe ContaBancaria."""

class ContaBancaria:
    def __init__(self, titular,saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.historico=[]

    def depositar(self,valor):
        if valor<=0:
            raise ValueError("Valor deve ser positivo")
        self.saldo+=valor
        self.historico.append(f"Depósito: +{valor}")

    def sacar( self, valor ):
        if valor<=0:
            raise ValueError("Valor deve ser positivo")
        if valor>self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo-=valor
        self.historico.append(f"Saque: -{valor}")

    def consultar_saldo(self):
        return self.saldo

    def obter_extrato( self ):
        return self.historico.copy()
