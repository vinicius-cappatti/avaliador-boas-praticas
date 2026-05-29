# ==============================================================================
# INTEGRANTES:
# - Felipe U. G. de Sousa (RA: 10418415)
# - Gustavo N. Siqueira (RA: 10419057)
# - Thomaz de S. Scopel (RA: 10417183)
# - Vinicius S. Cappatti (RA: 10418266)
#
# SÍNTESE DO ARQUIVO:
# Módulo responsável por fazer a validação automática PEP 8 utilizando
# pycodestyle.
#
# HISTÓRICO DE ALTERAÇÕES:
# Data       | Autor       | Breve descrição da atualização
# ------------------------------------------------------------------------------
# 02/04/2026 | Equipe      | Adição de cabeçalho padronizado e adequação N1.
# 28/05/2026 | Equipe      | Ajustes de conformidade PEP 8 e documentação para N2.
# ==============================================================================

"""
Módulo para validação PEP 8 utilizando pycodestyle.
"""

import pycodestyle
import tempfile
import os


def validar_pep8_conteudo(nome_arquivo: str, conteudo: str) -> list[dict]:
    """
    Valida o conteúdo de um arquivo Python contra as regras PEP 8.

    Args:
        nome_arquivo: Nome do arquivo (usado para identificação no relatório).
        conteudo: Código-fonte do arquivo como string.

    Returns:
        Lista de dicionários com as violações encontradas.
        Cada dicionário contém: linha, coluna, codigo, mensagem.
    """
    # Escreve o conteúdo em um arquivo temporário para o pycodestyle analisar
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(conteudo)
        tmp_path = tmp.name

    violacoes = []
    try:
        guia = pycodestyle.StyleGuide(
            parse_argv=False,
            reporter=_ColetorErros,
            quiet=True,
        )
        relatorio = guia.check_files([tmp_path])

        # O relatório customizado expõe os erros coletados para consumo
        # no pipeline.
        if hasattr(relatorio, "erros"):
            violacoes = relatorio.erros

        violacoes.sort(key=lambda v: (v["linha"], v["coluna"], v["codigo"]))
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

    return violacoes


class _ColetorErros(pycodestyle.BaseReport):
    """Reporter customizado que coleta os erros em uma lista de dicionários."""

    def __init__(self, options=None):
        if options is None:
            options = pycodestyle.StyleGuide(
                parse_argv=False, quiet=True
            ).options
        super().__init__(options)
        self.erros = []

    def error(self, line_number, offset, text, check):
        code = super().error(line_number, offset, text, check)
        if code:
            mensagem = text
            if text.startswith(f"{code} "):
                mensagem = text[len(code) + 1:]

            self.erros.append({
                "linha": line_number,
                "coluna": offset + 1,
                "codigo": code,
                "mensagem": mensagem,
            })
        return code


def validar_arquivos(conteudos: dict[str, str]) -> dict[str, list[dict]]:
    """
    Valida múltiplos arquivos Python contra as regras PEP 8.

    Args:
        conteudos: Dicionário com nome do arquivo como chave e
                   conteúdo como valor.

    Returns:
        Dicionário com nome do arquivo como chave e lista de
        violações como valor.
    """
    resultados = {}
    for nome, conteudo in conteudos.items():
        if not nome.endswith(".py"):
            continue
        resultados[nome] = validar_pep8_conteudo(nome, conteudo)
    return resultados


def formatar_resultado_pep8(nome_arquivo: str, violacoes: list[dict]) -> str:
    """
    Formata as violações PEP 8 de um arquivo em uma string legível.

    Args:
        nome_arquivo: Nome do arquivo.
        violacoes: Lista de violações encontradas.

    Returns:
        String formatada com as violações.
    """
    if not violacoes:
        return f"Nenhuma violação PEP 8 encontrada."

    linhas = [f"Total de violações: {len(violacoes)}"]
    for v in violacoes:
        linhas.append(
            f"  Linha {v['linha']}, Coluna {v['coluna']}: "
            f"[{v['codigo']}] {v['mensagem']}"
        )
    return "\n".join(linhas)
