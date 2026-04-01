"""Módulo de gerenciamento de tarefas."""

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas=[]

    def adicionar(self,descricao,prioridade="media"):
        tarefa={"descricao":descricao,"prioridade":prioridade,"concluida":False}
        self.tarefas.append(tarefa)

    def concluir(self,indice):
        if indice<0 or indice>=len(self.tarefas):
            raise IndexError("Índice inválido")
        self.tarefas[indice]["concluida"]=True

    def listar_pendentes(self):
        return [t for t in self.tarefas if not t["concluida"]]

    def listar_concluidas(self):
        return [t for t in self.tarefas if t["concluida"]]

    def remover(self,indice):
        if indice<0 or indice>=len(self.tarefas):
            raise IndexError("Índice inválido")
        return self.tarefas.pop(indice)

    def total(self):
        return len(self.tarefas)
