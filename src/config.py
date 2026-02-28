GEMINI_MODEL ="gemini-2.5-flash"

PROMPT_CHECKLIST = """
Você é um revisor de código experiente. Abaixo estão os arquivos submetidos para análise, cada um identificado pelo seu nome.

Para cada arquivo, verifique:
- Nomenclatura de variáveis e funções
- Presença de comentários
- Tratamento de exceções
- Modularização

Retorne um relatório separado por arquivo, usando o nome do arquivo como cabeçalho.

{arquivos_formatados}
"""