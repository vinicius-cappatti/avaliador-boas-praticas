"""Módulo de validação de senhas."""

import re

def verificar_senha(senha):
    erros=[]
    if len(senha)<8:
        erros.append("Senha deve ter no mínimo 8 caracteres")
    if not re.search(r'[A-Z]',senha):
        erros.append("Senha deve ter ao menos uma letra maiúscula")
    if not re.search(r'[a-z]',senha):
        erros.append("Senha deve ter ao menos uma letra minúscula")
    if not re.search(r'[0-9]',senha):
        erros.append("Senha deve ter ao menos um dígito")
    if not re.search(r'[!@#$%^&*]',senha):
        erros.append("Senha deve ter ao menos um caractere especial")
    return erros

def senha_forte(senha):
    return len(verificar_senha(senha))==0

def gerar_feedback_senha(senha):
    erros=verificar_senha(senha)
    if not erros:
        return "Senha forte!"
    return "Problemas encontrados: "+"; ".join(erros)
