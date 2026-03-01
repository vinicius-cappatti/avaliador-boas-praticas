import os
from google import genai
from config import GEMINI_MODEL


def enviar_para_gemini(prompt: str) -> str:
    """
    Envia o prompt para o Gemini e retorna a resposta.
    
    Args:
        prompt: O prompt formatado para enviar ao Gemini.
        
    Returns:
        Resposta do modelo Gemini.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY não está definida nas variáveis de ambiente.")
    
    client = genai.Client()
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )
    return response.text