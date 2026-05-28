"""Módulo com classe Logger simples."""
import datetime

class Logger:
    NIVEIS=["DEBUG","INFO","WARNING","ERROR","CRITICAL"]
    def __init__(self,nivel_minimo="DEBUG"):
        if nivel_minimo not in self.NIVEIS:
            raise ValueError(f"Nível inválido: {nivel_minimo}")
        self.nivel_minimo=self.NIVEIS.index(nivel_minimo)
        self.registros=[]
    def _registrar(self,nivel,mensagem):
        if self.NIVEIS.index(nivel)>=self.nivel_minimo:
            registro={"timestamp":datetime.datetime.now().isoformat(),"nivel":nivel,"mensagem":mensagem}
            self.registros.append(registro)
    def debug(self,mensagem):
        self._registrar("DEBUG",mensagem)
    def info(self,mensagem):
        self._registrar("INFO",mensagem)
    def warning(self,mensagem):
        self._registrar("WARNING",mensagem)
    def error(self,mensagem):
        self._registrar("ERROR",mensagem)
    def critical(self,mensagem):
        self._registrar("CRITICAL",mensagem)
    def obter_registros(self,nivel=None):
        if nivel:
            return [r for r in self.registros if r["nivel"]==nivel]
        return self.registros.copy()
    def limpar(self):
        self.registros=[]
