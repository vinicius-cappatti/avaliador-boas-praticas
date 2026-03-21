OLLAMA_MODEL = "minimax-m2.7:cloud"

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

Abaixo estão arquivos Python que foram analisados automaticamente pela ferramenta pycodestyle.
Para cada arquivo, são listadas as violações PEP 8 encontradas (código do erro, linha e descrição).
Também é incluído o código-fonte completo do arquivo para contexto.

Sua tarefa é gerar um feedback estruturado e didático para o desenvolvedor, contendo:
1. **Resumo**: uma visão geral da qualidade do código em relação à PEP 8.
2. **Erros encontrados**: para cada violação, explique o que significa, por que é importante seguir a regra e como corrigir, mostrando o trecho de código corrigido.
3. **Sugestões gerais**: dicas adicionais de boas práticas Python que podem melhorar o código.

Se um arquivo não tiver violações, parabenize o desenvolvedor e faça sugestões gerais de melhoria.

Retorne o relatório separado por arquivo, usando o nome do arquivo como cabeçalho.

{arquivos_formatados}
"""