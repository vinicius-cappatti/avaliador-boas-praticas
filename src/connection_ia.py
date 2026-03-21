from connection_ollama import enviar_para_ollama

def enviar_para_ia(prompt: str) -> str:
  return enviar_para_ollama(prompt)
