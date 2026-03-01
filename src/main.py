"""
Programa para ler arquivos de código e armazenar seu conteúdo em strings.
Suporta arquivos locais ou repositórios públicos do GitHub.
"""

import argparse
from utils import ler_multiplos_arquivos, formatar_arquivos
from config import PROMPT_CHECKLIST
from connection_gemini import enviar_para_gemini
from github_utils import buscar_arquivos_codigo_github


def processar_arquivos_locais(arquivos: list[str]) -> dict[str, str]:
    """
    Processa arquivos locais e retorna seus conteúdos.
    
    Args:
        arquivos: Lista de caminhos de arquivos locais.
        
    Returns:
        Dicionário com nome do arquivo e seu conteúdo.
    """
    return ler_multiplos_arquivos(arquivos)


def processar_github(url: str, limite_arquivos: int, limite_tamanho_kb: int) -> dict[str, str]:
    """
    Busca e processa arquivos de código de um repositório GitHub.
    
    Args:
        url: URL do repositório GitHub.
        limite_arquivos: Número máximo de arquivos a processar.
        limite_tamanho_kb: Tamanho máximo de cada arquivo em KB.
        
    Returns:
        Dicionário com caminho do arquivo e seu conteúdo.
    """
    return buscar_arquivos_codigo_github(url, limite_arquivos, limite_tamanho_kb)


def main():
    parser = argparse.ArgumentParser(
        description="Lê arquivos de código e armazena seus conteúdos em strings. Suporta arquivos locais ou repositórios GitHub."
    )
    
    # Grupo mutuamente exclusivo: ou arquivos locais ou URL do GitHub
    grupo_fonte = parser.add_mutually_exclusive_group(required=True)
    grupo_fonte.add_argument(
        '-f', '--arquivos',
        nargs='+',
        help='Um ou mais arquivos de código locais para processar.'
    )
    grupo_fonte.add_argument(
        '-g', '--github',
        type=str,
        help='URL de um repositório público do GitHub para analisar.'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Exibe o conteúdo dos arquivos lidos.'
    )
    parser.add_argument(
        '-l', '--limite-arquivos',
        type=int,
        default=20,
        help='Número máximo de arquivos a processar do GitHub (padrão: 20).'
    )
    parser.add_argument(
        '-t', '--limite-tamanho',
        type=int,
        default=100,
        help='Tamanho máximo de cada arquivo em KB (padrão: 100).'
    )
    
    args = parser.parse_args()
    
    # Determina a fonte dos arquivos
    if args.github:
        print(f"\n{'='*50}")
        print("Modo: Repositório GitHub")
        print(f"{'='*50}\n")
        try:
            conteudos = processar_github(args.github, args.limite_arquivos, args.limite_tamanho)
        except Exception as e:
            print(f"Erro ao processar repositório GitHub: {e}")
            return None
    else:
        print(f"\n{'='*50}")
        print("Modo: Arquivos Locais")
        print(f"{'='*50}\n")
        conteudos = processar_arquivos_locais(args.arquivos)
    
    # Verifica se há arquivos para processar
    if not conteudos:
        print("Nenhum arquivo de código encontrado para análise.")
        return None
    
    # Formata os arquivos para o prompt
    arquivos_formatados = formatar_arquivos(conteudos)
    
    # Monta o prompt completo
    prompt_final = PROMPT_CHECKLIST.format(arquivos_formatados=arquivos_formatados)
    
    # Exibe informações sobre os arquivos lidos
    print(f"\n{'='*50}")
    print(f"Total de arquivos processados: {len(conteudos)}")
    print(f"{'='*50}\n")
    
    for nome_arquivo, conteudo in conteudos.items():
        num_linhas = len(conteudo.splitlines()) if conteudo else 0
        num_caracteres = len(conteudo)
        
        print(f"Arquivo: {nome_arquivo}")
        print(f"  Linhas: {num_linhas}")
        print(f"  Caracteres: {num_caracteres}")
        
        if args.verbose and conteudo:
            print(f"  Conteúdo:")
            print("-" * 40)
            print(conteudo)
            print("-" * 40)
        print()
    
    # Envia para o Gemini e exibe a resposta
    print(f"{'='*50}")
    print("Enviando para análise do Gemini...")
    print(f"{'='*50}\n")
    
    try:
        resposta_gemini = enviar_para_gemini(prompt_final)
        print("Relatório de Análise:")
        print("-" * 40)
        print(resposta_gemini)
    except Exception as e:
        print(f"Erro ao comunicar com o Gemini: {e}")
    
    return conteudos


if __name__ == "__main__":
    main()
