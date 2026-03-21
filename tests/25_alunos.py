"""Módulo de processamento de notas de alunos."""


class Aluno:
    """Representa um aluno com suas notas."""

    def __init__(self, nome, notas=None):
        self.nome = nome
        self.notas = notas if notas is not None else []

    def adicionar_nota(self, nota):
        """Adiciona uma nota ao aluno."""
        if not 0 <= nota <= 10:
            raise ValueError("Nota deve estar entre 0 e 10.")
        self.notas.append(nota)

    def media(self):
        """Calcula a média das notas."""
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        """Retorna a situação do aluno."""
        m = self.media()
        if m >= 7.0:
            return "Aprovado"
        elif m >= 5.0:
            return "Recuperação"
        else:
            return "Reprovado"

    def __repr__(self):
        return f"Aluno({self.nome}, média={self.media():.1f})"


class Turma:
    """Representa uma turma de alunos."""

    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        """Adiciona um aluno à turma."""
        self.alunos.append(aluno)

    def media_turma(self):
        """Calcula a média geral da turma."""
        if not self.alunos:
            return 0.0
        return sum(a.media() for a in self.alunos) / len(self.alunos)

    def aprovados(self):
        """Retorna lista de alunos aprovados."""
        return [a for a in self.alunos if a.situacao() == "Aprovado"]

    def reprovados(self):
        """Retorna lista de alunos reprovados."""
        return [a for a in self.alunos if a.situacao() == "Reprovado"]
