# ==============================================================================
# INTEGRANTES:
# - Felipe U. G. de Sousa (RA: 10418415)
# - Gustavo N. Siqueira (RA: 10419057)
# - Thomaz de S. Scopel (RA: 10417183)
# - Vinicius S. Cappatti (RA: 10418266)
#
# SÍNTESE DO ARQUIVO:
# Conexão principal com a API da biblioteca `ollama` para inferências.
#
# HISTÓRICO DE ALTERAÇÕES:
# Data       | Autor       | Breve descrição da atualização
# ------------------------------------------------------------------------------
# 02/04/2026 | Equipe      | Adição de cabeçalho padronizado e adequação N1.
# ==============================================================================

import ollama
from config import OLLAMA_MODEL

def enviar_para_ollama(prompt: str) -> str:
    """
    Envia o prompt para o modelo hospedado no Ollama e retorna a resposta.

    Args:
        prompt: O prompt formatado para enviar ao modelo.
    Returns:
        Resposta do modelo hospedado no Ollama.
    """

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]