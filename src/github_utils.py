# ==============================================================================
# INTEGRANTES:
# - Felipe U. G. de Sousa (RA: 10418415)
# - Gustavo N. Siqueira (RA: 10419057)
# - Thomaz de S. Scopel (RA: 10417183)
# - Vinicius S. Cappatti (RA: 10418266)
#
# SÍNTESE DO ARQUIVO:
# Módulo para integração com GitHub API para buscar arquivos de repositórios públicos.
#
# HISTÓRICO DE ALTERAÇÕES:
# Data       | Autor       | Breve descrição da atualização
# ------------------------------------------------------------------------------
# 02/04/2026 | Equipe      | Adição de cabeçalho padronizado e adequação N1.
# ==============================================================================

"""
Módulo para integração com GitHub API para buscar arquivos de repositórios públicos.
"""

import re
import requests
from typing import Optional
from config import EXTENSOES_CODIGO, PASTAS_IGNORADAS


def extrair_info_repositorio(url: str) -> tuple[str, str, Optional[str]]:
    """
    Extrai o owner, nome do repositório e branch de uma URL do GitHub.
    
    Args:
        url: URL do repositório GitHub.
        
    Returns:
        Tupla com (owner, repo, branch). Branch pode ser None.
        
    Raises:
        ValueError: Se a URL não for válida.
    """
    # Padrões suportados:
    # https://github.com/owner/repo
    # https://github.com/owner/repo/tree/branch
    # https://github.com/owner/repo.git
    
    padrao = r"github\.com[/:]([^/]+)/([^/.\s]+)(?:\.git)?(?:/tree/([^\s/]+))?"
    
    match = re.search(padrao, url)
    if not match:
        raise ValueError(f"URL do GitHub inválida: {url}")
    
    owner = match.group(1)
    repo = match.group(2)
    branch = match.group(3)  # Pode ser None
    
    return owner, repo, branch


def obter_branch_padrao(owner: str, repo: str) -> str:
    """
    Obtém o branch padrão do repositório.
    
    Args:
        owner: Dono do repositório.
        repo: Nome do repositório.
        
    Returns:
        Nome do branch padrão (geralmente 'main' ou 'master').
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    response.raise_for_status()
    
    dados = response.json()
    return dados.get("default_branch", "main")


def listar_arquivos_repositorio(owner: str, repo: str, branch: str, caminho: str = "") -> list[dict]:
    """
    Lista recursivamente todos os arquivos de um repositório.
    
    Args:
        owner: Dono do repositório.
        repo: Nome do repositório.
        branch: Branch a ser analisado.
        caminho: Caminho dentro do repositório (para recursão).
        
    Returns:
        Lista de dicionários com informações dos arquivos.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{caminho}"
    params = {"ref": branch}
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    itens = response.json()
    arquivos = []
    
    for item in itens:
        nome = item.get("name", "")
        tipo = item.get("type")
        caminho_item = item.get("path", "")
        
        # Ignora pastas que não devem ser analisadas
        if tipo == "dir":
            # Verifica se a pasta deve ser ignorada
            if nome in PASTAS_IGNORADAS or nome.startswith("."):
                continue
            # Busca recursivamente arquivos dentro da pasta
            arquivos.extend(listar_arquivos_repositorio(owner, repo, branch, caminho_item))
        elif tipo == "file":
            arquivos.append({
                "nome": nome,
                "caminho": caminho_item,
                "url_download": item.get("download_url"),
                "tamanho": item.get("size", 0)
            })
    
    return arquivos


def filtrar_arquivos_codigo(arquivos: list[dict]) -> list[dict]:
    """
    Filtra apenas arquivos de código fonte baseado nas extensões.
    
    Args:
        arquivos: Lista de arquivos do repositório.
        
    Returns:
        Lista filtrada contendo apenas arquivos de código.
    """
    arquivos_codigo = []
    
    for arquivo in arquivos:
        nome = arquivo.get("nome", "")
        # Verifica se a extensão do arquivo é de código
        for ext in EXTENSOES_CODIGO:
            if nome.endswith(ext):
                arquivos_codigo.append(arquivo)
                break
    
    return arquivos_codigo


def baixar_conteudo_arquivo(url_download: str) -> str:
    """
    Baixa o conteúdo de um arquivo do GitHub.
    
    Args:
        url_download: URL de download do arquivo.
        
    Returns:
        Conteúdo do arquivo como string.
    """
    response = requests.get(url_download)
    response.raise_for_status()
    return response.text


def buscar_arquivos_codigo_github(url_repositorio: str, limite_arquivos: int = 20, limite_tamanho_kb: int = 100) -> dict[str, str]:
    """
    Função principal que busca e retorna arquivos de código de um repositório GitHub.
    
    Args:
        url_repositorio: URL do repositório GitHub.
        limite_arquivos: Número máximo de arquivos a processar.
        limite_tamanho_kb: Tamanho máximo de cada arquivo em KB.
        
    Returns:
        Dicionário com nome do arquivo (caminho) como chave e conteúdo como valor.
    """
    print(f"Processando repositório: {url_repositorio}")
    
    # Extrai informações da URL
    owner, repo, branch = extrair_info_repositorio(url_repositorio)
    print(f"  Owner: {owner}, Repo: {repo}")
    
    # Obtém branch padrão se não especificado
    if not branch:
        branch = obter_branch_padrao(owner, repo)
    print(f"  Branch: {branch}")
    
    # Lista todos os arquivos
    print("  Buscando arquivos do repositório...")
    todos_arquivos = listar_arquivos_repositorio(owner, repo, branch)
    print(f"  Total de arquivos encontrados: {len(todos_arquivos)}")
    
    # Filtra apenas arquivos de código
    arquivos_codigo = filtrar_arquivos_codigo(todos_arquivos)
    print(f"  Arquivos de código encontrados: {len(arquivos_codigo)}")
    
    # Aplica limite de tamanho (converte KB para bytes)
    limite_bytes = limite_tamanho_kb * 1024
    arquivos_codigo = [a for a in arquivos_codigo if a.get("tamanho", 0) <= limite_bytes]
    
    # Aplica limite de quantidade
    if len(arquivos_codigo) > limite_arquivos:
        print(f"  Limitando a {limite_arquivos} arquivos...")
        arquivos_codigo = arquivos_codigo[:limite_arquivos]
    
    # Baixa o conteúdo dos arquivos
    conteudos = {}
    for arquivo in arquivos_codigo:
        caminho = arquivo.get("caminho", "")
        url = arquivo.get("url_download")
        
        if url:
            try:
                print(f"  Baixando: {caminho}")
                conteudo = baixar_conteudo_arquivo(url)
                conteudos[caminho] = conteudo
            except Exception as e:
                print(f"  Erro ao baixar {caminho}: {e}")
    
    return conteudos
