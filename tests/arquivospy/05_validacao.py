"""Módulo de validação de dados."""


def validar_email(email):
    """Verifica se um email contém @ e domínio."""
    if "@" not in email:
        return False
    partes = email.split("@")
    if len(partes) != 2:
        return False
    if "." not in partes[1]:
        return False
    return True


def validar_cpf(cpf):
    """Valida se o CPF tem 11 dígitos numéricos."""
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    if len(cpf_limpo) != 11:
        return False
    if not cpf_limpo.isdigit():
        return False
    return True


def validar_idade(idade):
    """Verifica se a idade é válida."""
    if not isinstance(idade, int):
        return False
    return 0 <= idade <= 150
