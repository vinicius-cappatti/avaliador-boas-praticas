from connetion_gemini import enviar_para_gemini

def enviar_para_ia(prompt: str) -> str:
  #Implementar conexão com o Llama
  #return enviar_para_llama(prompt)
  return enviar_para_gemini(prompt)
