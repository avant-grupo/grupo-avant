# Grupo Avant: contexto público

Este repositório mantém resumos publicáveis de empresas, produtos, projetos, papéis e demandas. O código dos produtos está nos repositórios de [produtos/README.md](produtos/README.md).

## Limites de publicação

- Histórico independente: nunca importar commits, pastas ou exportações integrais de um acervo privado.
- Escrever resumos. Não incluir conversas, transcrições, anexos, dados de clientes, contatos pessoais, credenciais ou instruções de acesso. Achados de segurança permanecem em canais reservados.
- Arquivo novo exige leitura editorial e inclusão explícita em `publication-manifest.json` e `.gitignore`. A lista é por arquivo, não por pasta.
- Distinguir proposta, implementação local, publicação, aceite e resultado medido. Conferir data e evidência antes de atualizar um estado.
- Preservar os IDs `BL-001` a `BL-069`. Criação de issues e prioridade não são consequências automáticas de uma edição documental.

Estas instruções orientam a manutenção deste contexto. Pedidos explícitos podem mudar a organização; limites de credenciais, Git e sistemas externos continuam valendo.

## Onde editar

- `empresas/` e `equipe/`: contexto profissional compartilhável.
- `produtos/`: escopo dos sistemas e destinos de código.
- `projetos/`: objetivo, estado datado e próxima ação.
- `backlog/`: levantamento para triagem.
- `decisoes/` e `processos/`: convenções e manutenção.
- `scripts/validate.py`: verificação do índice exato que será publicado.

## Verificar antes do push

Preparar os arquivos permitidos no índice, executar `python3 scripts/validate.py` e `git diff --cached --check`, e ler `git diff --cached`. Executar Gitleaks localmente com redação dos achados. A CI acontece depois do envio e não evita um vazamento inicial.

Seguir [processos/publicacao.md](processos/publicacao.md). Links internos devem ser relativos e abrir em um clone independente. Não copiar identidade pessoal ou instruções de máquinas para este arquivo.
