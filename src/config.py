# ==============================================================================
# INTEGRANTES:
# - Felipe U. G. de Sousa (RA: 10418415)
# - Gustavo N. Siqueira (RA: 10419057)
# - Thomaz de S. Scopel (RA: 10417183)
# - Vinicius S. Cappatti (RA: 10418266)
#
# SÍNTESE DO ARQUIVO:
# Arquivo de configuração contendo parâmetros como o modelo do Ollama e
# prompts da LLM.
#
# HISTÓRICO DE ALTERAÇÕES:
# Data       | Autor       | Breve descrição da atualização
# ------------------------------------------------------------------------------
# 02/04/2026 | Equipe      | Adição de cabeçalho padronizado e adequação N1.
# 28/05/2026 | Equipe      | Ajustes PEP 8 e documentação para N2.
# ==============================================================================

OLLAMA_MODEL = "llama3.1"

# Extensões de arquivos de código fonte reconhecidas (somente Python)
EXTENSOES_CODIGO = [
    ".py",
]

# Pastas que devem ser ignoradas na análise
PASTAS_IGNORADAS = [
    "node_modules",
    "venv",
    ".venv",
    "env",
    ".env",
    "__pycache__",
    ".git",
    ".github",
    ".vscode",
    ".idea",
    "dist",
    "build",
    "target",
    "bin",
    "obj",
    "out",
    "vendor",
    "packages",
    ".next",
    ".nuxt",
    "coverage",
    "test",
    "tests",
    "__tests__",
    "spec",
    "specs",
]

PROMPT_CHECKLIST = """
Você é um revisor de código Python experiente, especialista em PEP 8.

Abaixo estão arquivos Python que foram analisados automaticamente
pela ferramenta pycodestyle.
Para cada arquivo, são listadas as violações PEP 8 encontradas
(código do erro, linha e descrição).
Também é incluído o código-fonte completo do arquivo para contexto.

Sua tarefa é gerar um feedback estruturado e didático para o
desenvolvedor, contendo:
1. **Resumo**: uma visão geral da qualidade do código em relação à PEP 8.
2. **Erros encontrados**: para cada violação, explique o que significa,
por que é importante seguir a regra e como corrigir, mostrando o
trecho de código corrigido.
3. **Sugestões gerais**: dicas adicionais de boas práticas Python que
podem melhorar o código.

Restrições obrigatórias:
- Baseie a contagem de erros exclusivamente na lista de violações fornecida.
- Não invente códigos de erro, linhas ou quantidades que não
estejam na entrada.
- Se identificar possíveis melhorias que não são checadas pelo
pycodestyle, marque claramente como "Sugestão extra".
- Ao final de cada arquivo, informe: "Total de violações consideradas: N".

Se um arquivo não tiver violações, parabenize o desenvolvedor e
faça sugestões gerais de melhoria sem afirmar erros inexistentes.

Retorne o relatório separado por arquivo, usando o nome do arquivo
como cabeçalho.

{arquivos_formatados}
"""
