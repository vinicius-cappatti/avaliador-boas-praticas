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