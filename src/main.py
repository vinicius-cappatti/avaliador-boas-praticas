# ==============================================================================
# INTEGRANTES:
# - Felipe U. G. de Sousa (RA: 10418415)
# - Gustavo N. Siqueira (RA: 10419057)
# - Thomaz de S. Scopel (RA: 10417183)
# - Vinicius S. Cappatti (RA: 10418266)
#
# SÍNTESE DO ARQUIVO:
# Ponto de entrada principal do avaliador. Orquestra a leitura, validação PEP8 e a LLM.
#
# HISTÓRICO DE ALTERAÇÕES:
# Data       | Autor       | Breve descrição da atualização
# ------------------------------------------------------------------------------
# 02/04/2026 | Equipe      | Adição de cabeçalho padronizado e adequação N1.
# ==============================================================================

"""
Programa para ler arquivos Python e avaliá-los com validação PEP 8 automática.
Os erros encontrados são enviados a uma LLM para gerar feedback estruturado.
Suporta arquivos locais, pastas locais ou repositórios públicos do GitHub.
"""

import argparse
from utils import ler_multiplos_arquivos, ler_arquivos_pasta, formatar_arquivos_com_pep8
from config import PROMPT_CHECKLIST
from github_utils import buscar_arquivos_codigo_github
from connection_ia import enviar_para_ia
from pep8_validator import validar_arquivos, formatar_resultado_pep8

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
    grupo_fonte.add_argument(
        '-d', '--diretorio',
        type=str,
        help='Caminho para uma pasta local cujos arquivos de código serão analisados recursivamente.'
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
    elif args.diretorio:
        print(f"\n{'='*50}")
        print("Modo: Pasta Local")
        print(f"{'='*50}\n")
        conteudos = ler_arquivos_pasta(args.diretorio)
    else:
        print(f"\n{'='*50}")
        print("Modo: Arquivos Locais")
        print(f"{'='*50}\n")
        conteudos = processar_arquivos_locais(args.arquivos)
    
    # Filtra apenas arquivos Python
    conteudos = {nome: cont for nome, cont in conteudos.items() if nome.endswith(".py")}

    # Verifica se há arquivos para processar
    if not conteudos:
        print("Nenhum arquivo Python encontrado para análise.")
        return None

    # Executa validação PEP 8
    print(f"\n{'='*50}")
    print("Executando validação PEP 8 com pycodestyle...")
    print(f"{'='*50}\n")

    resultados_pep8 = validar_arquivos(conteudos)

    total_violacoes = sum(len(v) for v in resultados_pep8.values())

    # Exibe informações sobre os arquivos lidos e violações
    print(f"Total de arquivos processados: {len(conteudos)}")
    print(f"Total de violações PEP 8: {total_violacoes}\n")
    
    for nome_arquivo, conteudo in conteudos.items():
        num_linhas = len(conteudo.splitlines()) if conteudo else 0
        num_caracteres = len(conteudo)
        violacoes = resultados_pep8.get(nome_arquivo, [])

        print(f"Arquivo: {nome_arquivo}")
        print(f"  Linhas: {num_linhas}")
        print(f"  Caracteres: {num_caracteres}")
        print(f"  Violações PEP 8: {len(violacoes)}")

        if violacoes:
            print(f"  {formatar_resultado_pep8(nome_arquivo, violacoes)}")
        
        if args.verbose and conteudo:
            print(f"  Conteúdo:")
            print("-" * 40)
            print(conteudo)
            print("-" * 40)
        print()

    # Formata os arquivos com os resultados PEP 8 para o prompt
    arquivos_formatados = formatar_arquivos_com_pep8(conteudos, resultados_pep8)

    # Monta o prompt completo
    prompt_final = PROMPT_CHECKLIST.format(arquivos_formatados=arquivos_formatados)

    # Envia para o llama e exibe a resposta
    print(f"{'='*50}")
    print("Enviando para análise do Llama...")
    print(f"{'='*50}\n")
    
    try:
        resposta_llama = enviar_para_ia(prompt_final)
        
        with open("resposta_llama.md", "w", encoding="utf-8") as arquivo_saida:
            arquivo_saida.write("Revisão do Llama:\n")
            fonte = args.github if args.github else (args.diretorio if args.diretorio else ", ".join(args.arquivos))
            arquivo_saida.write("Código analisado: " + fonte + "\n\n")
            arquivo_saida.write(f"{'='*50}\n")
            arquivo_saida.write(resposta_llama)
        
        print("Resposta do Llama salva em 'resposta_llama.md'.")
    except Exception as e:
        print(f"Erro ao comunicar com o Llama: {e}")
    
    return conteudos


if __name__ == "__main__":
    main()
