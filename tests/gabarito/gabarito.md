# Gabarito — Violações PEP 8 nos Arquivos de Teste

Este documento contém o relatório de violações PEP 8 identificadas pela ferramenta **pycodestyle** nos 25 arquivos Python da pasta `tests/`. Ele serve como gabarito para comparação com a resposta gerada pelo agente de revisão (LLM).

---

## Resumo Geral

| Arquivo | Violações |
|---------|-----------|
| 01_calculadora.py | 0 |
| 02_strings.py | 10 |
| 03_listas.py | 0 |
| 04_pessoa.py | 9 |
| 05_validacao.py | 0 |
| 06_matematica.py | 20 |
| 07_dicionarios.py | 0 |
| 08_conta_bancaria.py | 13 |
| 09_ordenacao.py | 0 |
| 10_arquivos.py | 15 |
| 11_temperatura.py | 0 |
| 12_pilha.py | 8 |
| 13_fila.py | 0 |
| 14_geometria.py | 22 |
| 15_busca.py | 0 |
| 16_tarefas.py | 17 |
| 17_datas.py | 0 |
| 18_criptografia.py | 18 |
| 19_estatistica.py | 0 |
| 20_senhas.py | 11 |
| 21_unidades.py | 0 |
| 22_inventario.py | 21 |
| 23_matrizes.py | 0 |
| 24_logger.py | 30 |
| 25_alunos.py | 0 |

**Total de violações: 194**

**Arquivos limpos (sem violações):** 01, 03, 05, 07, 09, 11, 13, 15, 17, 19, 21, 23, 25

**Arquivos com violações:** 02, 04, 06, 08, 10, 12, 14, 16, 18, 20, 22, 24

---

## Detalhamento por Arquivo

### 01_calculadora.py

Nenhuma violação PEP 8 encontrada. Código em conformidade.

---

### 02_strings.py

Total de violações: 10

- Linha 3, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 3, Coluna 21: [E201] whitespace after '('
- Linha 3, Coluna 23: [E202] whitespace before ')'
- Linha 7, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 10, Coluna 9: [E225] missing whitespace around operator
- Linha 13, Coluna 17: [E225] missing whitespace around operator
- Linha 16, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 16, Coluna 26: [E201] whitespace after '('
- Linha 16, Coluna 32: [E202] whitespace before ')'
- Linha 20, Coluna 1: [E302] expected 2 blank lines, found 1

**Problemas identificados:**
- Falta de duas linhas em branco entre definições de funções no nível do módulo (E302).
- Espaços dentro dos parênteses nas funções `inverter_string( s )` e `capitalizar_palavras( frase )` (E201/E202).
- Falta de espaço ao redor do operador `=` e `+=` em atribuições como `cont=0` e `cont+=1` (E225).

---

### 03_listas.py

Nenhuma violação PEP 8 encontrada. Código em conformidade.

---

### 04_pessoa.py

Total de violações: 9

- Linha 3, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 4, Coluna 22: [E231] missing whitespace after ','
- Linha 4, Coluna 27: [E231] missing whitespace after ','
- Linha 5, Coluna 18: [E225] missing whitespace around operator
- Linha 6, Coluna 19: [E225] missing whitespace around operator
- Linha 8, Coluna 22: [E201] whitespace after '('
- Linha 8, Coluna 27: [E202] whitespace before ')'
- Linha 12, Coluna 26: [E225] missing whitespace around operator
- Linha 15, Coluna 19: [E225] missing whitespace around operator

**Problemas identificados:**
- Falta de duas linhas em branco antes da definição da classe (E302).
- Falta de espaço após vírgulas nos parâmetros `self,nome,idade` (E231).
- Falta de espaço ao redor do operador `=` em atribuições como `self.nome=nome` (E225).
- Espaços dentro dos parênteses em `cumprimentar( self )` (E201/E202).
- Falta de espaço ao redor dos operadores `>=` e `+=` (E225).

---

### 05_validacao.py

Nenhuma violação PEP 8 encontrada. Código em conformidade.

---

### 06_matematica.py

Total de violações: 20

- Linha 3, Coluna 1: [E302] expected 2 blank lines, found 0
- Linha 4, Coluna 9: [E225] missing whitespace around operator
- Linha 6, Coluna 9: [E225] missing whitespace around operator
- Linha 6, Coluna 17: [E225] missing whitespace around operator
- Linha 8, Coluna 14: [E225] missing whitespace around operator
- Linha 9, Coluna 21: [E231] missing whitespace after ','
- Linha 10, Coluna 18: [E225] missing whitespace around operator
- Linha 13, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 14, Coluna 9: [E225] missing whitespace around operator
- Linha 16, Coluna 11: [E225] missing whitespace around operator
- Linha 18, Coluna 8: [E225] missing whitespace around operator
- Linha 18, Coluna 11: [E231] missing whitespace after ','
- Linha 19, Coluna 21: [E231] missing whitespace after ','
- Linha 23, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 23, Coluna 14: [E201] whitespace after '('
- Linha 23, Coluna 21: [E202] whitespace before ')'
- Linha 24, Coluna 14: [E225] missing whitespace around operator
- Linha 26, Coluna 21: [E231] missing whitespace after ','
- Linha 27, Coluna 18: [E228] missing whitespace around modulo operator
- Linha 27, Coluna 20: [E225] missing whitespace around operator
- Linha 31, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 31, Coluna 18: [E231] missing whitespace after ','

**Problemas identificados:**
- Nenhuma linha em branco entre o `import` e a primeira função (E302 com 0 linhas).
- Falta de duas linhas em branco entre funções no nível do módulo (E302).
- Falta de espaço ao redor de operadores de comparação e atribuição como `n<0`, `n==0`, `resultado=1` (E225).
- Falta de espaço ao redor do operador módulo `%` (E228).
- Falta de espaço após vírgulas em chamadas como `range(2,n+1)` (E231).
- Espaços dentro dos parênteses em `eh_primo( numero )` (E201/E202).

---

### 07_dicionarios.py

Nenhuma violação PEP 8 encontrada. Código em conformidade.

---

### 08_conta_bancaria.py

Total de violações: 13

- Linha 3, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 4, Coluna 31: [E231] missing whitespace after ','
- Linha 7, Coluna 23: [E225] missing whitespace around operator
- Linha 9, Coluna 23: [E231] missing whitespace after ','
- Linha 10, Coluna 17: [E225] missing whitespace around operator
- Linha 12, Coluna 19: [E225] missing whitespace around operator
- Linha 15, Coluna 15: [E201] whitespace after '('
- Linha 15, Coluna 27: [E202] whitespace before ')'
- Linha 16, Coluna 17: [E225] missing whitespace around operator
- Linha 18, Coluna 17: [E225] missing whitespace around operator
- Linha 20, Coluna 19: [E225] missing whitespace around operator
- Linha 26, Coluna 23: [E201] whitespace after '('
- Linha 26, Coluna 28: [E202] whitespace before ')'

**Problemas identificados:**
- Falta de duas linhas em branco antes da classe (E302).
- Falta de espaço após vírgulas em parâmetros (E231).
- Falta de espaço ao redor de operadores `=`, `<=`, `>`, `+=`, `-=` (E225).
- Espaços dentro dos parênteses em `sacar( self, valor )` e `obter_extrato( self )` (E201/E202).

---

### 09_ordenacao.py

Nenhuma violação PEP 8 encontrada. Código em conformidade.

---

### 10_arquivos.py

Total de violações: 15

- Linha 3, Coluna 1: [E302] expected 2 blank lines, found 0
- Linha 4, Coluna 22: [E231] missing whitespace after ','
- Linha 4, Coluna 26: [E231] missing whitespace after ','
- Linha 6, Coluna 1: [E302] expected 2 blank lines, found 0
- Linha 6, Coluna 29: [E231] missing whitespace after ','
- Linha 7, Coluna 22: [E231] missing whitespace after ','
- Linha 7, Coluna 26: [E231] missing whitespace after ','
- Linha 9, Coluna 1: [E302] expected 2 blank lines, found 0
- Linha 9, Coluna 33: [E231] missing whitespace after ','
- Linha 10, Coluna 22: [E231] missing whitespace after ','
- Linha 10, Coluna 26: [E231] missing whitespace after ','
- Linha 12, Coluna 1: [E302] expected 2 blank lines, found 0
- Linha 13, Coluna 22: [E231] missing whitespace after ','
- Linha 13, Coluna 26: [E231] missing whitespace after ','
- Linha 15, Coluna 1: [E302] expected 2 blank lines, found 0

**Problemas identificados:**
- Nenhuma linha em branco entre funções (0 linhas em branco, deveria ser 2) (E302).
- Falta de espaço após vírgulas em chamadas como `open(caminho,'r',encoding='utf-8')` (E231).

---

### 11_temperatura.py

Nenhuma violação PEP 8 encontrada. Código em conformidade.

---

### 12_pilha.py

Total de violações: 8

- Linha 3, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 4, Coluna 18: [E201] whitespace after '('
- Linha 4, Coluna 23: [E202] whitespace before ')'
- Linha 7, Coluna 18: [E201] whitespace after '('
- Linha 7, Coluna 29: [E202] whitespace before ')'
- Linha 15, Coluna 14: [E201] whitespace after '('
- Linha 15, Coluna 19: [E202] whitespace before ')'
- Linha 21, Coluna 20: [E201] whitespace after '('
- Linha 21, Coluna 31: [E202] whitespace before ')'

**Problemas identificados:**
- Falta de duas linhas em branco antes da classe (E302).
- Espaços dentro dos parênteses em vários métodos: `__init__( self )`, `empilhar( self, item )`, `topo( self )`, `len( self.itens )` (E201/E202).

---

### 13_fila.py

Nenhuma violação PEP 8 encontrada. Código em conformidade.

---

### 14_geometria.py

Total de violações: 22

- Linha 3, Coluna 1: [E302] expected 2 blank lines, found 0
- Linha 4, Coluna 22: [E231] missing whitespace after ','
- Linha 5, Coluna 18: [E225] missing whitespace around operator
- Linha 6, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 8, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 11, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 12, Coluna 22: [E231] missing whitespace after ','
- Linha 12, Coluna 30: [E231] missing whitespace after ','
- Linha 13, Coluna 21: [E225] missing whitespace around operator
- Linha 14, Coluna 20: [E225] missing whitespace around operator
- Linha 15, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 17, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 20, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 21, Coluna 22: [E231] missing whitespace after ',' (5 ocorrências na mesma linha)
- Linha 22, Coluna 18: [E225] missing whitespace around operator
- Linha 23, Coluna 20: [E225] missing whitespace around operator
- Linha 24, Coluna 20: [E225] missing whitespace around operator
- Linha 25, Coluna 20: [E225] missing whitespace around operator
- Linha 26, Coluna 20: [E225] missing whitespace around operator
- Linha 27, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 29, Coluna 5: [E301] expected 1 blank line, found 0

**Problemas identificados:**
- Nenhuma linha em branco entre o `import` e a primeira classe, e apenas 1 entre classes (E302).
- Falta de linha em branco entre métodos dentro de classes (E301).
- Falta de espaço após vírgulas nos parâmetros de `__init__` (E231).
- Falta de espaço ao redor de operadores `=` em atribuições (E225).

---

### 15_busca.py

Nenhuma violação PEP 8 encontrada. Código em conformidade.

---

### 16_tarefas.py

Total de violações: 17

- Linha 3, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 5, Coluna 21: [E225] missing whitespace around operator
- Linha 7, Coluna 23: [E231] missing whitespace after ','
- Linha 7, Coluna 33: [E231] missing whitespace after ','
- Linha 8, Coluna 15: [E225] missing whitespace around operator
- Linha 8, Coluna 28: [E231] missing whitespace after ':'
- Linha 8, Coluna 38: [E231] missing whitespace after ','
- Linha 8, Coluna 51: [E231] missing whitespace after ':'
- Linha 8, Coluna 62: [E231] missing whitespace after ','
- Linha 8, Coluna 74: [E231] missing whitespace after ':'
- Linha 8, Coluna 80: [E501] line too long (80 > 79 characters)
- Linha 11, Coluna 22: [E231] missing whitespace after ','
- Linha 12, Coluna 18: [E225] missing whitespace around operator
- Linha 12, Coluna 30: [E225] missing whitespace around operator
- Linha 14, Coluna 42: [E225] missing whitespace around operator
- Linha 22, Coluna 21: [E231] missing whitespace after ','
- Linha 23, Coluna 18: [E225] missing whitespace around operator
- Linha 23, Coluna 30: [E225] missing whitespace around operator

**Problemas identificados:**
- Falta de duas linhas em branco antes da classe (E302).
- Falta de espaço ao redor de operadores `=`, `<`, `>=` (E225).
- Falta de espaço após vírgulas e dois-pontos em dicionários literais (E231).
- Linha com mais de 79 caracteres na construção do dicionário `tarefa` (E501).

---

### 17_datas.py

Nenhuma violação PEP 8 encontrada. Código em conformidade.

---

### 18_criptografia.py

Total de violações: 18

- Linha 3, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 3, Coluna 35: [E231] missing whitespace after ','
- Linha 4, Coluna 14: [E225] missing whitespace around operator
- Linha 7, Coluna 17: [E225] missing whitespace around operator
- Linha 8, Coluna 22: [E225] missing whitespace around operator
- Linha 8, Coluna 57: [E228] missing whitespace around modulo operator
- Linha 10, Coluna 22: [E225] missing whitespace around operator
- Linha 13, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 13, Coluna 38: [E231] missing whitespace after ','
- Linha 14, Coluna 42: [E231] missing whitespace after ','
- Linha 16, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 17, Coluna 42: [E231] missing whitespace after ','
- Linha 19, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 19, Coluna 27: [E231] missing whitespace after ','
- Linha 20, Coluna 14: [E225] missing whitespace around operator
- Linha 21, Coluna 10: [E231] missing whitespace after ','
- Linha 22, Coluna 18: [E225] missing whitespace around operator
- Linha 22, Coluna 33: [E227] missing whitespace around bitwise or shift operator
- Linha 22, Coluna 45: [E228] missing whitespace around modulo operator

**Problemas identificados:**
- Falta de duas linhas em branco entre funções (E302).
- Falta de espaço após vírgulas em parâmetros e chamadas (E231).
- Falta de espaço ao redor de operadores `=`, `+=` (E225).
- Falta de espaço ao redor do operador módulo `%` (E228).
- Falta de espaço ao redor do operador XOR `^` (E227).

---

### 19_estatistica.py

Nenhuma violação PEP 8 encontrada. Código em conformidade.

---

### 20_senhas.py

Total de violações: 11

- Linha 5, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 6, Coluna 10: [E225] missing whitespace around operator
- Linha 7, Coluna 18: [E225] missing whitespace around operator
- Linha 9, Coluna 30: [E231] missing whitespace after ','
- Linha 11, Coluna 30: [E231] missing whitespace after ','
- Linha 13, Coluna 30: [E231] missing whitespace after ','
- Linha 15, Coluna 35: [E231] missing whitespace after ','
- Linha 19, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 20, Coluna 39: [E225] missing whitespace around operator
- Linha 22, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 23, Coluna 10: [E225] missing whitespace around operator

**Problemas identificados:**
- Falta de duas linhas em branco entre funções (E302).
- Falta de espaço ao redor de operadores `=`, `<`, `==` (E225).
- Falta de espaço após vírgulas em chamadas `re.search(r'...',senha)` (E231).

---

### 21_unidades.py

Nenhuma violação PEP 8 encontrada. Código em conformidade.

---

### 22_inventario.py

Total de violações: 21

- Linha 3, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 4, Coluna 22: [E231] missing whitespace after ',' (3 ocorrências)
- Linha 5, Coluna 18: [E225] missing whitespace around operator
- Linha 6, Coluna 24: [E225] missing whitespace around operator
- Linha 7, Coluna 19: [E225] missing whitespace around operator
- Linha 8, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 10, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 13, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 15, Coluna 19: [E225] missing whitespace around operator
- Linha 16, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 16, Coluna 28: [E231] missing whitespace after ',' (3 ocorrências)
- Linha 18, Coluna 40: [E225] missing whitespace around operator
- Linha 20, Coluna 29: [E225] missing whitespace around operator
- Linha 20, Coluna 39: [E231] missing whitespace after ',' (2 ocorrências)
- Linha 21, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 21, Coluna 26: [E231] missing whitespace after ','
- Linha 25, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 26, Coluna 14: [E225] missing whitespace around operator
- Linha 28, Coluna 18: [E225] missing whitespace around operator
- Linha 30, Coluna 5: [E301] expected 1 blank line, found 0

**Problemas identificados:**
- Falta de duas linhas em branco entre classes (E302).
- Falta de linha em branco entre métodos (E301).
- Falta de espaço após vírgulas nos parâmetros (E231).
- Falta de espaço ao redor de operadores `=`, `+=` (E225).

---

### 23_matrizes.py

Nenhuma violação PEP 8 encontrada. Código em conformidade.

---

### 24_logger.py

Total de violações: 30

- Linha 4, Coluna 1: [E302] expected 2 blank lines, found 1
- Linha 5, Coluna 11: [E225] missing whitespace around operator
- Linha 5, Coluna 20: [E231] missing whitespace after ',' (4 ocorrências)
- Linha 6, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 6, Coluna 22: [E231] missing whitespace after ','
- Linha 9, Coluna 26: [E225] missing whitespace around operator
- Linha 10, Coluna 23: [E225] missing whitespace around operator
- Linha 11, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 11, Coluna 24: [E231] missing whitespace after ',' (2 ocorrências)
- Linha 12, Coluna 36: [E225] missing whitespace around operator
- Linha 13, Coluna 21: [E225] missing whitespace around operator
- Linha 13, Coluna 34: [E231] missing whitespace after ':'
- Linha 13, Coluna 70: [E231] missing whitespace after ','
- Linha 13, Coluna 78: [E231] missing whitespace after ':'
- Linha 13, Coluna 80: [E501] line too long (104 > 79 characters)
- Linha 13, Coluna 84: [E231] missing whitespace after ','
- Linha 13, Coluna 95: [E231] missing whitespace after ':'
- Linha 15, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 15, Coluna 19: [E231] missing whitespace after ','
- Linha 16, Coluna 32: [E231] missing whitespace after ','
- Linha 17, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 17, Coluna 18: [E231] missing whitespace after ','
- Linha 18, Coluna 31: [E231] missing whitespace after ','
- Linha 19, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 19, Coluna 21: [E231] missing whitespace after ','
- Linha 20, Coluna 34: [E231] missing whitespace after ','
- Linha 21, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 21, Coluna 19: [E231] missing whitespace after ','
- Linha 22, Coluna 32: [E231] missing whitespace after ','
- Linha 23, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 23, Coluna 22: [E231] missing whitespace after ','
- Linha 24, Coluna 35: [E231] missing whitespace after ','
- Linha 25, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 25, Coluna 29: [E231] missing whitespace after ','
- Linha 27, Coluna 60: [E225] missing whitespace around operator
- Linha 29, Coluna 5: [E301] expected 1 blank line, found 0
- Linha 30, Coluna 23: [E225] missing whitespace around operator

**Problemas identificados:**
- Falta de duas linhas em branco antes da classe (E302).
- Falta de linha em branco entre todos os métodos da classe (E301) — ocorrência massiva.
- Falta de espaço após vírgulas em praticamente todos os parâmetros e chamadas (E231).
- Falta de espaço ao redor de operadores `=`, `>=`, `==` (E225).
- Linha 13 com 104 caracteres, excedendo o limite de 79 (E501).
- Falta de espaço após `:` em dicionários literais (E231).

---

### 25_alunos.py

Nenhuma violação PEP 8 encontrada. Código em conformidade.

---

## Estatísticas por Tipo de Violação

| Código | Descrição | Ocorrências |
|--------|-----------|-------------|
| E201 | whitespace after '(' | 10 |
| E202 | whitespace before ')' | 10 |
| E225 | missing whitespace around operator | 62 |
| E227 | missing whitespace around bitwise or shift operator | 1 |
| E228 | missing whitespace around modulo operator | 3 |
| E231 | missing whitespace after ',' | 78 |
| E301 | expected 1 blank line, found 0 | 21 |
| E302 | expected 2 blank lines, found 0 or 1 | 30 |
| E501 | line too long (> 79 characters) | 2 |

**Total geral: 217 violações**

---

## Tipos de Violações Inseridas

As violações foram propositalmente inseridas nos arquivos pares (02, 04, 06, 08, 10, 12, 14, 16, 18, 20, 22, 24) seguindo padrões comuns de erros de desenvolvedores iniciantes:

1. **E225 — Falta de espaço ao redor de operadores**: `x=1`, `a<=0`, `n==0`, `total+=1`
2. **E231 — Falta de espaço após vírgula**: `def f(a,b)`, `range(2,n)`, `open(f,'r')`
3. **E302 — Falta de linhas em branco entre definições**: funções e classes sem as 2 linhas em branco obrigatórias
4. **E301 — Falta de linha em branco entre métodos**: métodos dentro de classes sem separação
5. **E201/E202 — Espaços dentro de parênteses**: `func( arg )` ao invés de `func(arg)`
6. **E501 — Linha muito longa**: linhas com mais de 79 caracteres
7. **E227/E228 — Falta de espaço ao redor de operadores bitwise e módulo**: `a^b`, `a%b`
