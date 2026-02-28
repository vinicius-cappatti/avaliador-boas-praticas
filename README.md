# Avaliador de Boas Práticas de Código

Projeto da disciplina de IA para criar um agente que avalia as boas práticas de código utilizando a API do Google Gemini.

## Descrição

Este projeto analisa arquivos de código fonte e gera um relatório de boas práticas utilizando inteligência artificial. O sistema verifica:

- Nomenclatura de variáveis e funções
- Presença de comentários
- Tratamento de exceções
- Modularização do código

## Estrutura do Projeto

```
avaliador-boas-praticas/
├── src/
│   ├── main.py              # Ponto de entrada do programa
│   ├── utils.py             # Funções utilitárias para leitura de arquivos
│   ├── config.py            # Configurações e prompts
│   └── connection_gemini.py # Conexão com a API do Gemini
├── .env                     # Variáveis de ambiente (criar manualmente)
├── .gitignore
└── README.md
```

---

## Pré-requisitos

- Python 3.10 ou superior
- Conta Google com acesso ao Google AI Studio
- Chave de API do Gemini

---

## Configuração Passo a Passo

### 1. Criar Chave de API no Google AI Studio

1. Acesse o [Google AI Studio](https://aistudio.google.com/)
2. Faça login com sua conta Google
3. No menu lateral, clique em **"Get API key"** ou acesse diretamente: https://aistudio.google.com/app/apikey
4. Clique em **"Create API key"**
5. Selecione um projeto existente ou crie um novo projeto no Google Cloud
6. Copie a chave de API gerada (ela será exibida apenas uma vez)

> **Importante:** Guarde sua chave de API em local seguro. Nunca compartilhe ou commite sua chave no repositório.

### 2. Consultar Tabela de Preços

Antes de usar a API, consulte os custos associados:

- **Tabela de Preços do Gemini API:** https://ai.google.dev/pricing

O modelo `gemini-2.5-flash` possui um nível gratuito generoso, mas verifique os limites de uso.

### 3. Criar o Arquivo `.env`

Na raiz do projeto, crie um arquivo chamado `.env` com o seguinte conteúdo:

```env
GEMINI_API_KEY=sua_chave_de_api_aqui
```

Substitua `sua_chave_de_api_aqui` pela chave obtida no passo 1.

### 4. Configurar o VSCode para Usar o `.env`

Para que o VSCode carregue automaticamente as variáveis de ambiente do arquivo `.env`, adicione as seguintes configurações:

#### Opção A: Configuração do Workspace (recomendado)

Crie ou edite o arquivo `.vscode/settings.json` na raiz do projeto:

```json
{
    "python.envFile": "${workspaceFolder}/.env",
    "terminal.integrated.env.windows": {
        "GEMINI_API_KEY": "${env:GEMINI_API_KEY}"
    },
    "terminal.integrated.env.linux": {
        "GEMINI_API_KEY": "${env:GEMINI_API_KEY}"
    },
    "terminal.integrated.env.osx": {
        "GEMINI_API_KEY": "${env:GEMINI_API_KEY}"
    }
}
```

#### Opção B: Configuração Global do Usuário

Abra as configurações do VSCode (`Ctrl+,`) e adicione:

```json
{
    "python.envFile": "${workspaceFolder}/.env"
}
```

#### Opção C: Usar python-dotenv no código

Instale o pacote `python-dotenv` e carregue as variáveis no início do código:

```python
from dotenv import load_dotenv
load_dotenv()
```

### 5. Instalar Dependências

```bash
pip install google-genai python-dotenv
```

Ou crie um arquivo `requirements.txt`:

```txt
google-genai
python-dotenv
```

E execute:

```bash
pip install -r requirements.txt
```

---

## Como Executar

### Uso Básico

```bash
cd src
python main.py caminho/para/arquivo1.py caminho/para/arquivo2.py
```

### Com Modo Verbose (exibe conteúdo dos arquivos)

```bash
python main.py -v arquivo1.py arquivo2.py
```

### Exemplos

Analisar um único arquivo:
```bash
python main.py ../exemplos/meu_codigo.py
```

Analisar múltiplos arquivos:
```bash
python main.py utils.py config.py connection_gemini.py
```

---

## Variáveis de Ambiente

| Variável | Descrição | Obrigatório |
|----------|-----------|-------------|
| `GEMINI_API_KEY` | Chave de API do Google Gemini | Sim |

---

## Solução de Problemas

### Erro: "GEMINI_API_KEY não está definida"

- Verifique se o arquivo `.env` existe na raiz do projeto
- Confirme que a variável está corretamente definida no `.env`
- Reinicie o terminal do VSCode após criar/modificar o `.env`

### Erro: "Import could not be resolved"

Execute a instalação das dependências:
```bash
pip install google-genai
```

### Erro de autenticação na API

- Verifique se a chave de API está correta
- Confirme que a API do Gemini está habilitada no seu projeto Google Cloud
- Verifique se você não excedeu os limites de uso

---

## Links Úteis

- [Google AI Studio](https://aistudio.google.com/)
- [Documentação da API Gemini](https://ai.google.dev/docs)
- [Tabela de Preços](https://ai.google.dev/pricing)
- [Guia de Início Rápido](https://ai.google.dev/tutorials/python_quickstart)

---

## Licença

Este projeto foi desenvolvido para fins educacionais na disciplina de Inteligência Artificial.
