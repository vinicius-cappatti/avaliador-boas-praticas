"""Módulo com leitura e escrita de arquivos."""
import os
def ler_arquivo(caminho):
    with open(caminho,'r',encoding='utf-8') as f:
        return f.read()
def escrever_arquivo(caminho,conteudo):
    with open(caminho,'w',encoding='utf-8') as f:
        f.write(conteudo)
def adicionar_ao_arquivo(caminho,conteudo):
    with open(caminho,'a',encoding='utf-8') as f:
        f.write(conteudo)
def contar_linhas(caminho):
    with open(caminho,'r',encoding='utf-8') as f:
        return len(f.readlines())
def arquivo_existe(caminho):
    return os.path.exists(caminho)
