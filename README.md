# Avaliador de Boas Práticas de Código

Projeto da disciplina de IA para criar um agente que avalia as boas práticas de código utilizando o modelo Llama via [Ollama](https://ollama.com/).

## Descrição

Este projeto analisa arquivos de código **Python** e gera um relatório de boas práticas utilizando inteligência artificial. O sistema executa uma validação automática PEP 8 com **pycodestyle** antes de enviar os resultados para a LLM, que gera um feedback estruturado e didático.

O sistema suporta:

- **Arquivos locais**: Analise arquivos Python diretamente do seu computador
- **Pasta local**: Informe o caminho de uma pasta e o sistema analisa recursivamente todos os arquivos `.py` dentro dela
- **Repositórios GitHub**: Informe a URL de um repositório público e o sistema busca automaticamente os arquivos Python

Fluxo de análise:

1. Os arquivos Python são lidos
2. O **pycodestyle** valida cada arquivo contra as regras PEP 8
3. As violações encontradas + código-fonte são enviados à LLM
4. A LLM gera um feedback estruturado com explicações e sugestões de correção

## Estrutura do Projeto

```
avaliador-boas-praticas/
├── src/
│   ├── main.py              # Ponto de entrada do programa
│   ├── utils.py             # Funções utilitárias para leitura de arquivos
│   ├── config.py            # Configurações, prompts e extensões
│   ├── pep8_validator.py    # Validação PEP 8 com pycodestyle
│   ├── connection_ia.py     # Camada de abstração para a IA
│   ├── connection_ollama.py # Conexão com o modelo via Ollama
│   └── github_utils.py      # Integração com a API do GitHub
├── requirements.txt         # Dependências do projeto
├── .gitignore
└── README.md
```

---

## Pré-requisitos

- Python 3.10 ou superior
- [Ollama](https://ollama.com/) instalado e em execução

---

## Configuração Passo a Passo

### 1. Instalar o Ollama

1. Acesse [https://ollama.com/download](https://ollama.com/download) e baixe o instalador para o seu sistema operacional
2. Execute a instalação seguindo as instruções do instalador
3. Após instalar, verifique se o Ollama está funcionando:

```bash
ollama --version
```

### 2. Baixar o Modelo

O projeto utiliza o modelo `minimax-m2.7:cloud` por padrão (configurável em `src/config.py`). Para baixá-lo, execute:

```bash
ollama pull minimax-m2.7:cloud
```

> **Nota:** O modelo será baixado localmente. Certifique-se de ter espaço em disco suficiente.

Para usar um modelo diferente, altere a variável `OLLAMA_MODEL` em `src/config.py`:

```python
OLLAMA_MODEL = "nome-do-modelo"
```

Você pode listar os modelos disponíveis com `ollama list` e ver todos os modelos no [catálogo do Ollama](https://ollama.com/library).

### 3. Instalar Dependências Python

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install ollama requests pycodestyle
```

---

## Como Executar

### 1. Certifique-se de que o Ollama está rodando

O Ollama precisa estar em execução para que o projeto funcione. Ele normalmente inicia automaticamente após a instalação, mas caso não esteja rodando:

```bash
ollama serve
```

### 2. Analisar Arquivos Locais

```bash
cd src
python main.py -f caminho/para/arquivo1.py caminho/para/arquivo2.py
```

### 3. Analisar uma Pasta Local

```bash
cd src
python main.py -d caminho/para/pasta
```

O sistema irá percorrer a pasta recursivamente, lendo todos os arquivos `.py` e ignorando pastas como `__pycache__`, `.git`, `.venv`, etc.

### 4. Analisar Repositório GitHub

```bash
cd src
python main.py -g https://github.com/usuario/repositorio
```

### Opções Disponíveis

| Opção | Descrição |
|-------|------------|
| `-f, --arquivos` | Arquivos locais para analisar |
| `-d, --diretorio` | Caminho para uma pasta local (análise recursiva) |
| `-g, --github` | URL do repositório GitHub público |
| `-v, --verbose` | Exibe o conteúdo dos arquivos |
| `-l, --limite-arquivos` | Máximo de arquivos do GitHub (padrão: 20) |
| `-t, --limite-tamanho` | Tamanho máximo por arquivo em KB (padrão: 100) |

### Exemplos

Analisar um único arquivo local:
```bash
python main.py -f ../exemplos/meu_codigo.py
```

Analisar múltiplos arquivos locais:
```bash
python main.py -f utils.py config.py connection_ollama.py
```

Analisar todos os arquivos de código de uma pasta:
```bash
python main.py -d ../meu_projeto
```

Analisar repositório GitHub com limite de 10 arquivos:
```bash
python main.py -g https://github.com/usuario/projeto -l 10
```

Analisar repositório com modo verbose:
```bash
python main.py -g https://github.com/usuario/projeto -v
```

---

## Solução de Problemas

### Erro: conexão recusada / Ollama não encontrado
- Verifique se o Ollama está instalado e em execução (`ollama serve`)
- Confirme que o serviço está acessível em `http://localhost:11434`

### Erro: modelo não encontrado
- Certifique-se de ter baixado o modelo com `ollama pull minimax-m2.7:cloud`
- Verifique os modelos instalados com `ollama list`

### Erro: "Import could not be resolved"

Execute a instalação das dependências:
```bash
pip install ollama requests pycodestyle
```

---

## Links Úteis

- [Ollama - Site Oficial](https://ollama.com/)
- [Ollama - Catálogo de Modelos](https://ollama.com/library)
- [Ollama - GitHub](https://github.com/ollama/ollama)
- [Ollama Python Library](https://github.com/ollama/ollama-python)

---

## Licença

Este projeto foi desenvolvido para fins educacionais na disciplina de Inteligência Artificial.
