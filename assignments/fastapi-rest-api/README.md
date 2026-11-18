# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Crie uma API REST para gerenciar livros usando FastAPI. Você praticará rotas HTTP, validação de dados com modelos e respostas de erro para recursos inexistentes.

## 📝 Tarefas

### 🛠️ Criar e listar livros

#### Descrição
Baixe o código inicial, renomeie `starter-code.py` para `main.py` e instale as dependências com `python -m pip install fastapi uvicorn`. Em seguida, crie os endpoints que cadastram livros e listam os livros cadastrados. A API deve validar os dados recebidos e manter os registros em memória durante a execução.

#### Requisitos
O programa concluído deve:

- Iniciar uma aplicação FastAPI que possa ser explorada em `/docs`.
- Executar a aplicação localmente com `uvicorn main:app --reload`.
- Implementar `GET /books` para retornar todos os livros, inclusive uma lista vazia quando não houver registros.
- Implementar `POST /books` para cadastrar um livro com título, autor e ano de publicação.
- Validar os dados de entrada com um modelo Pydantic e atribuir um identificador único a cada livro.
- Retornar o livro criado com o status HTTP `201 Created`.

### 🛠️ Consultar e atualizar livros

#### Descrição
Amplie a API para permitir consultar, atualizar e remover um livro pelo identificador. Trate de forma clara as solicitações para livros que não existem.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` para retornar um único livro.
- Implementar `PUT /books/{book_id}` para atualizar os dados de um livro existente.
- Implementar `DELETE /books/{book_id}` para remover um livro existente.
- Retornar o status HTTP `404 Not Found` quando o identificador não corresponder a um livro.
- Permitir testar e inspecionar os endpoints pela documentação interativa em `/docs`.