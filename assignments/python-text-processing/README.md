# 📘 Atividade: Python Text Processing

## 🎯 Objetivo

Leia e normalize um arquivo de texto com Python e analise a frequência das palavras para resumir seu conteúdo. Você praticará leitura de arquivos, manipulação de strings, listas e dicionários.

## 📝 Tarefas

### 🛠️ Carregar e normalizar o texto

#### Descrição
Use o arquivo `sample.txt` e o código inicial para carregar o texto e convertê-lo em uma lista consistente de palavras. Ignore diferenças entre letras maiúsculas e minúsculas e trate a pontuação como separador entre palavras.

#### Requisitos
O programa concluído deve:

- Ler `sample.txt` como texto UTF-8.
- Converter as palavras para letras minúsculas.
- Remover a pontuação sem juntar palavras que eram separadas por ela.
- Dividir o conteúdo em palavras sem incluir entradas vazias.
- Para o texto `Python, PYTHON! code.`, produzir `['python', 'python', 'code']`.

### 🛠️ Analisar a frequência das palavras

#### Descrição
Conte quantas vezes cada palavra aparece e apresente um resumo legível do arquivo. Use os tokens normalizados produzidos na tarefa anterior. Depois de implementar as funções do código inicial, execute `python starter-code.py` no diretório da atividade.

#### Requisitos
O programa concluído deve:

- Contar as ocorrências de cada palavra usando um dicionário.
- Exibir o total de palavras e a quantidade de palavras únicas.
- Exibir as cinco palavras mais frequentes em ordem decrescente de ocorrência.
- Em caso de empate, ordenar as palavras alfabeticamente.
- Para `['python', 'python', 'code']`, mostrar `python: 2` e `code: 1`.

Com o arquivo `sample.txt`, uma execução completa deve produzir um relatório equivalente a:

```text
Total words: 25
Unique words: 17
Top 5 words:
programs: 3
and: 2
are: 2
clear: 2
code: 2
```