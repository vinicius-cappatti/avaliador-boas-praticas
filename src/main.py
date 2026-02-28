"""
Programa para ler arquivos de código e armazenar seu conteúdo em strings.
"""

import argparse
from utils import ler_multiplos_arquivos, formatar_arquivos
from config import PROMPT_CHECKLIST
from connection_gemini import enviar_para_gemini

def main():
    parser = argparse.ArgumentParser(
        description="Lê arquivos de código e armazena seus conteúdos em strings."
    )
    parser.add_argument(
        'arquivos',
        nargs='+',
        help='Um ou mais arquivos de código para processar.'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Exibe o conteúdo dos arquivos lidos.'
    )
    
    args = parser.parse_args()
    
    # Lê todos os arquivos
    conteudos = ler_multiplos_arquivos(args.arquivos)
    
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
        resposta = enviar_para_gemini(prompt_final)
        print("Relatório de Análise:")
        print("-" * 40)
        print(resposta)
    except Exception as e:
        print(f"Erro ao comunicar com o Gemini: {e}")
    
    return conteudos


if __name__ == "__main__":
    main()
