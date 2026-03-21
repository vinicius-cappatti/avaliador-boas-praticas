"""Módulo de criptografia simples."""

def cifra_cesar_criptografar(texto,deslocamento):
    resultado=""
    for char in texto:
        if char.isalpha():
            base=ord('A') if char.isupper() else ord('a')
            resultado+=chr((ord(char)-base+deslocamento)%26+base)
        else:
            resultado+=char
    return resultado

def cifra_cesar_descriptografar(texto,deslocamento):
    return cifra_cesar_criptografar(texto,-deslocamento)

def rot13(texto):
    return cifra_cesar_criptografar(texto,13)

def xor_criptografar(texto,chave):
    resultado=""
    for i,char in enumerate(texto):
        resultado+=chr(ord(char)^ord(chave[i%len(chave)]))
    return resultado
