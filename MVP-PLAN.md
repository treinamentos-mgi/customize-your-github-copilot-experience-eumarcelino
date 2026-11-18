# Plano do MVP Inicial

## Conceito

Construir um portal educacional simples para compartilhar atividades de programação e personalizar o GitHub Copilot para ajudar professores a criá-las com consistência. O MVP combina o site de atividades com instruções específicas, uma skill de criação e um agente de brainstorming.

A atividade em andamento, **Python Text Processing**, ensina estudantes de nível intermediário a carregar um arquivo de texto, normalizar palavras e analisar frequências.

## Concluído

- [x] Instruções gerais do projeto em `.github/copilot-instructions.md`.
- [x] Instruções específicas de formato para tarefas em `.github/instructions/assignments.instructions.md`.
- [x] Skill `new-assignment` com guia de referência e scripts para atualizar `config.json` e anexar arquivos.
- [x] Agente `Assignment Brainstorming` com handoff para a skill de criação.
- [x] Branch de trabalho `feat/python-text-processing` criada.
- [x] README da atividade criado com duas tarefas progressivas.
- [x] Starter code e arquivo de amostra adicionados.
- [x] Atividade registrada em `config.json` com os dois anexos.
- [x] Sintaxe do starter code, registro, anexos e diagnósticos verificados.

## Para concluir o MVP

- [x] Acrescentar ao README o comando para executar o starter code e um exemplo de saída do relatório.
- [x] Conferir com `sample.txt` a normalização, o total de palavras (25), palavras únicas (17), o desempate alfabético e o top 5. O starter code continua intencionalmente incompleto para os alunos.
- [x] Verificar via HTTP que o preview serve a página, `config.json`, README e os dois anexos (todos responderam `200`).
- [x] Inspecionar visualmente a página da atividade e testar os links de download no navegador (confirmado pelo usuário).
- [x] Revisar o diff: as mudanças estão limitadas a `config.json`, `assignments/python-text-processing/` e este mapa.
- [x] Fazer commit e push de `feat/python-text-processing` após a revisão.
- [ ] Depois de integrar/publicar a branch, confirmar que a atividade aparece corretamente no portal publicado.

## Depois do MVP

- [ ] Padronizar o README de `assignments/data-analysis/` com os cabeçalhos do template.
- [ ] Considerar testes automatizados para os scripts da skill de criação.
