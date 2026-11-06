# Publicação do contexto

Este repositório tem histórico independente do acervo privado. Seu conteúdo inicial foi redigido como resumo, sem importar o histórico nem copiar pastas do acervo.

## Conteúdo permitido

Contexto de empresas e projetos, nomes e papéis profissionais, escopo de produtos, decisões compartilháveis e demandas sem dados pessoais ou informações de acesso.

Conversas, transcrições, áudios, anexos, capturas, dados de clientes, contatos pessoais, contratos, valores comerciais, credenciais, sessões e instruções de acesso permanecem no acervo privado. Achados de segurança recebem tratamento reservado no produto responsável.

## Atualização

1. Escrever ou atualizar o resumo neste repositório. Consultar fontes privadas não autoriza reproduzir os originais.
2. Para arquivo novo, acrescentar seu caminho exato em `publication-manifest.json` e no `.gitignore`. Ler integralmente o arquivo antes de permiti-lo.
3. Preparar os arquivos no índice do Git. Executar `python3 scripts/validate.py` e `git diff --cached --check`.
4. Revisar `git diff --cached`. A verificação usa o índice e também recusa arquivos preparados que ainda tenham alterações locais.
5. Executar Gitleaks com redação dos achados sobre arquivos e histórico antes do primeiro envio. O workflow repete a verificação do histórico após cada envio.
6. Conferir o conteúdo publicado e registrar a data do contexto. Não tratar uma atualização documental como nova validação de produção.

## Limites das proteções

O `.gitignore` exclui arquivos novos por padrão; ele não protege conteúdo já versionado. O manifesto limita os caminhos aceitos pelo validador. A CI detecta problemas depois do envio e não impede a exposição inicial: a revisão e a varredura locais precisam ocorrer antes do push.

Os verificadores não reconhecem toda informação privada escrita em prosa. A revisão humana ou editorial continua necessária, especialmente para nomes, contexto de negócio e detalhes técnicos. Não criar sincronização automática com pastas privadas.
