# ==============================================================================
# INTEGRANTES:
# - Felipe U. G. de Sousa (RA: 10418415)
# - Gustavo N. Siqueira (RA: 10419057)
# - Thomaz de S. Scopel (RA: 10417183)
# - Vinicius S. Cappatti (RA: 10418266)
#
# SÍNTESE DO ARQUIVO:
# Funções de utilidade geral para ler múltiplos arquivos de diversos formatos.
#
# HISTÓRICO DE ALTERAÇÕES:
# Data       | Autor       | Breve descrição da atualização
# ------------------------------------------------------------------------------
# 02/04/2026 | Equipe      | Adição de cabeçalho padronizado e adequação N1.
# ==============================================================================

import argparse
import sys
from pathlib import Path
from config import EXTENSOES_CODIGO, PASTAS_IGNORADAS


def ler_arquivo(caminho: str) -> str:
    """
    Lê o conteúdo de um arquivo e retorna como string.
    
    Args:
        caminho: Caminho do arquivo a ser lido.
        
    Returns:
        Conteúdo do arquivo como string.
    """
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho}' não encontrado.")
        return ""
    except PermissionError:
        print(f"Erro: Sem permissão para ler o arquivo '{caminho}'.")
        return ""
    except Exception as e:
        print(f"Erro ao ler '{caminho}': {e}")
        return ""


def ler_multiplos_arquivos(caminhos: list[str]) -> dict[str, str]:
    """
    Lê múltiplos arquivos e retorna um dicionário com seus conteúdos.
    
    Args:
        caminhos: Lista de caminhos dos arquivos.
        
    Returns:
        Dicionário onde a chave é o nome do arquivo e o valor é seu conteúdo.
    """
    conteudos = {}
    for caminho in caminhos:
        nome_arquivo = Path(caminho).name
        conteudos[nome_arquivo] = ler_arquivo(caminho)
    return conteudos

def ler_arquivos_pasta(caminho_pasta: str) -> dict[str, str]:
    """
    Lê recursivamente todos os arquivos de código dentro de uma pasta.

    Args:
        caminho_pasta: Caminho da pasta a ser lida.

    Returns:
        Dicionário onde a chave é o caminho relativo do arquivo e o valor é seu conteúdo.
    """
    pasta = Path(caminho_pasta)
    if not pasta.is_dir():
        print(f"Erro: '{caminho_pasta}' não é uma pasta válida.")
        return {}

    conteudos = {}
    for arquivo in sorted(pasta.rglob("*")):
        if not arquivo.is_file():
            continue
        if arquivo.suffix.lower() not in EXTENSOES_CODIGO:
            continue
        if any(parte in PASTAS_IGNORADAS for parte in arquivo.relative_to(pasta).parts):
            continue
        caminho_relativo = str(arquivo.relative_to(pasta))
        conteudo = ler_arquivo(str(arquivo))
        if conteudo:
            conteudos[caminho_relativo] = conteudo
    return conteudos


def formatar_arquivos(arquivos: dict) -> str:
    """
    Formata os arquivos para o prompt, incluindo o nome do arquivo e seu conteúdo.
    Args:
        arquivos: Dicionário onde a chave é o nome do arquivo e o valor é seu conteúdo.
        
    Returns:
        String formatada para o prompt.
    """
    resultado = ""
    for nome, conteudo in arquivos.items():
        resultado += f"\n### Arquivo: {nome} ###\n"
        resultado += f"```\n{conteudo}\n```\n"
    return resultado


def formatar_arquivos_com_pep8(arquivos: dict[str, str], resultados_pep8: dict[str, list[dict]]) -> str:
    """
    Formata os arquivos junto com os resultados da validação PEP 8 para o prompt da LLM.

    Args:
        arquivos: Dicionário com nome do arquivo e conteúdo.
        resultados_pep8: Dicionário com nome do arquivo e lista de violações PEP 8.

    Returns:
        String formatada contendo código-fonte e violações para cada arquivo.
    """
    resultado = ""
    for nome, conteudo in arquivos.items():
        violacoes = resultados_pep8.get(nome, [])
        resultado += f"\n### Arquivo: {nome} ###\n"
        resultado += f"\n**Código-fonte:**\n```python\n{conteudo}\n```\n"

        if violacoes:
            resultado += f"\n**Violações PEP 8 encontradas ({len(violacoes)}):**\n"
            for v in violacoes:
                resultado += f"- Linha {v['linha']}, Coluna {v['coluna']}: [{v['codigo']}] {v['mensagem']}\n"
        else:
            resultado += "\n**Violações PEP 8 encontradas:** Nenhuma violação.\n"

    return resultado