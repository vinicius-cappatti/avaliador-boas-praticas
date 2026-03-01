GEMINI_MODEL = "gemini-2.5-flash"

# Extensões de arquivos de código fonte reconhecidas
EXTENSOES_CODIGO = [
    # Python
    ".py",
    # JavaScript/TypeScript
    ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs",
    # Java
    ".java",
    # C/C++
    ".c", ".cpp", ".cc", ".cxx", ".h", ".hpp", ".hxx",
    # C#
    ".cs",
    # Ruby
    ".rb",
    # Go
    ".go",
    # Rust
    ".rs",
    # PHP
    ".php",
    # Swift
    ".swift",
    # Kotlin
    ".kt", ".kts",
    # Scala
    ".scala",
    # Dart
    ".dart",
    # R
    ".r", ".R",
    # Shell
    ".sh", ".bash",
    # PowerShell
    ".ps1",
    # Lua
    ".lua",
    # Perl
    ".pl", ".pm",
    # Haskell
    ".hs",
    # Elixir
    ".ex", ".exs",
    # Clojure
    ".clj", ".cljs",
    # HTML/CSS (opcional)
    ".html", ".htm", ".css", ".scss", ".sass", ".less",
    # SQL
    ".sql",
    # Vue/Svelte
    ".vue", ".svelte",
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
Você é um revisor de código experiente. Abaixo estão os arquivos submetidos para análise, cada um identificado pelo seu nome.

Para cada arquivo, verifique:
- Nomenclatura de variáveis e funções
- Presença de comentários
- Tratamento de exceções
- Modularização

Retorne um relatório separado por arquivo, usando o nome do arquivo como cabeçalho.

{arquivos_formatados}
"""