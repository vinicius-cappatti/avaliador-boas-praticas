# ==============================================================================
# INTEGRANTES:
# - Felipe U. G. de Sousa (RA: 10418415)
# - Gustavo N. Siqueira (RA: 10419057)
# - Thomaz de S. Scopel (RA: 10417183)
# - Vinicius S. Cappatti (RA: 10418266)
#
# SÍNTESE DO ARQUIVO:
# Camada de abstração simples para interface com as requisições à Inteligência Artificial.
#
# HISTÓRICO DE ALTERAÇÕES:
# Data       | Autor       | Breve descrição da atualização
# ------------------------------------------------------------------------------
# 02/04/2026 | Equipe      | Adição de cabeçalho padronizado e adequação N1.
# ==============================================================================

from connection_ollama import enviar_para_ollama

def enviar_para_ia(prompt: str) -> str:
  return enviar_para_ollama(prompt)
