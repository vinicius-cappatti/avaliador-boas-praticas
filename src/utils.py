import argparse
import sys
from pathlib import Path


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

def formatar_arquivos(arquivos: dict) -> str:
    """
    Formata os arquivos para o prompt do Gemini, incluindo o nome do arquivo e seu conteúdo.
    Args:
        arquivos: Dicionário onde a chave é o nome do arquivo e o valor é seu conteúdo.
        
    Returns:
        String formatada para o prompt do Gemini.
    """
    resultado = ""
    for nome, conteudo in arquivos.items():
        resultado += f"\n### Arquivo: {nome} ###\n"
        resultado += f"```\n{conteudo}\n```\n"
    return resultado