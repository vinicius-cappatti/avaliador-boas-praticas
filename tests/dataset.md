# Dataset utilizado

Este dataset é uma base original e controlada construída pelo grupo para avaliar
o agente de feedback sobre estilo e legibilidade em código Python. A base foi
elaborada com apoio de IA generativa e curadoria do grupo, simulando exercícios
comuns de disciplinas introdutórias de programação.

## Composição

- 25 arquivos Python localizados em `tests/arquivospy`.
- 13 arquivos sem violações PEP 8 detectadas pelo `pycodestyle`.
- 12 arquivos com violações propositais de espaçamento, linhas em branco,
  vírgulas, parênteses e limite de linha.
- Gabarito de referência em `tests/gabarito/gabarito.md`.
- Saída de exemplo da LLM em `tests/resposta_llama/resposta_llama.md`.

## Finalidade

O objetivo da base é permitir uma avaliação reprodutível do pipeline:

1. execução do `pycodestyle`;
2. contagem das violações por arquivo e categoria;
3. comparação com o gabarito;
4. geração de feedback didático pela LLM;
5. análise qualitativa da fidelidade e clareza do relatório.

## Representatividade

Os arquivos simulam problemas frequentes em códigos de estudantes iniciantes,
como ausência de espaços ao redor de operadores, ausência de espaço após
vírgulas e linhas em branco insuficientes antes de funções/classes. A base não
substitui uma coleta real de submissões de alunos, mas foi planejada para cobrir
erros recorrentes de estilo em um cenário controlado e adequado à validação do
agente.
