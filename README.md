# Igor: contexto de projetos

Contexto compartilhado do trabalho com Igor, GomaPet e Grupo Avant. Este repositório apresenta os negócios, os produtos, as pessoas que participam das frentes e o backlog para discussão.

## Comece por aqui

- [Empresas e negócios](empresas/README.md): relação entre GomaPet, Grupo Avant, X1 e marca pessoal.
- [Equipe e responsabilidades](equipe/README.md): papéis profissionais documentados.
- [Produtos e repositórios](produtos/README.md): onde cada sistema e seu código vivem.
- [Projetos](projetos/README.md): objetivos, estado resumido e próximo passo.
- [Backlog de 69 entradas](backlog/README.md): levantamento para validar e priorizar.
- [Fluxo de demandas](processos/demandas.md): passagem do pedido de negócio à issue técnica.
- [Decisões comuns dos produtos](decisoes/produtos.md): limites e convenções compartilhados.

## Como interpretar o estado

Este recorte foi preparado em 2026-11-05 a partir do contexto documentado. A preparação não reexecutou testes nem consultou todos os produtos em produção. Cada estado conserva sua data; implementação local, publicação e aceite são etapas diferentes.

Uma entrada no backlog não cria compromisso, prioridade ou prazo. Os repositórios de código têm acesso próprio e podem exigir autorização para abrir os links.

## Como manter

Os resumos compartilháveis têm sua fonte neste repositório. Conversas, evidências de trabalho e complementos pessoais permanecem em acervo privado separado. Não há sincronização automática do acervo privado para cá.

Para acrescentar conteúdo, siga [o procedimento de publicação](processos/publicacao.md). Há uma lista explícita de arquivos permitidos em `publication-manifest.json`; o `.gitignore` também exclui arquivos por padrão.

Depois de preparar os arquivos no índice do Git, execute:

```sh
python3 scripts/validate.py
git diff --cached --check
```

A validação automatizada complementa a leitura editorial. Ela não decide se uma informação de negócio deve ser pública.
