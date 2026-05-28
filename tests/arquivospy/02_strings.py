"""Módulo de manipulação de strings."""

def inverter_string( s ):
    """Inverte uma string."""
    return s[::-1]

def contar_vogais(texto):
    """Conta as vogais em um texto."""
    vogais = "aeiouAEIOU"
    cont=0
    for c in texto:
        if c in vogais:
            cont+=1
    return cont

def capitalizar_palavras( frase ):
    """Capitaliza cada palavra de uma frase."""
    return frase.title()

def remover_espacos(texto):
    """Remove espaços em branco extras."""
    return " ".join(texto.split())
