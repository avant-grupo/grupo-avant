# Central Avant

## Propósito

Coordenação de pessoas, empresas, demandas, acompanhamento e acesso aos sistemas do grupo.

## Escopo

Pessoas e papéis por empresa; quadros, demandas e calendário; Judite; acesso aos demais produtos; resumos de gestão.

## Limites

Permissões e dados respeitam a empresa e a pessoa. A Central coordena o acesso; cada produto continua responsável pelas suas regras e cálculos.

## Estado resumido em 2026-11-05

Produto publicado, com evolução documentada até 2026-11-05. A adoção pelas equipes e os testes de novos fluxos são acompanhados separadamente.

Em 2026-11-08, a Judite passou a consultar, somente para leitura, rastreamento e funil da Operação X1, métricas do BI GomaPet e dados de anúncios, para responder dúvidas de diagnóstico da gestão. O acesso é restrito a quem conduz essas operações.

## Código e projetos

[Repositório do produto](https://github.com/avant-grupo/central).

- [automacoes empresa](../projetos/automacoes-empresa.md)
- [judite entre produtos](../projetos/judite-entre-produtos.md)
- [dashboard modular](../projetos/dashboard-modular.md)

## Atualização de 09/11/2026

Os perfis do Dashboard BI e os perfis de acesso ganharam a ação "Configurar os blocos do Retorno por campanha", válida junto com a tela Tráfego. Na janela do BI, a Judite lê e altera esses blocos com o acesso de quem conversa, mostrando o que cada mudança move e permitindo desfazer. [PR e código publicado](https://github.com/avant-grupo/central/pull/14).

## Faturamento da Judite pelo BI, publicado em 10/11/2026

A Judite passou a responder faturamento, pedidos e ticket médio pela consulta de métricas do BI, que traz o mesmo número da tela, e a usar o total de todas as lojas quando recorre ao resumo comercial. A conferência da resposta dela ficou pendente: no mesmo dia, as chamadas ao modelo da Judite falhavam por limite de crédito no provedor de IA. [PR e código publicado](https://github.com/avant-grupo/central/pull/17).


## Resumos por operação publicados em 11/11/2026

Gestão > Resumos passou a atender GomaPet, X1 e X1 Yuri, com configuração independente de métricas, recorte, agenda e destinatários. Novos resumos começam pausados, e cada pessoa recebe conforme seu acesso. O resumo diário existente foi preservado; a ativação do piloto permanece separada da publicação. [Central #20](https://github.com/avant-grupo/central/pull/20).


## Resumos em grupo e individuais, 11/11/2026

A Central passou a enviar resumos a grupos registrados por operação. Os resumos da X1 Yuri foram ativados no grupo próprio; os da X1 normal seguem diretamente para Igor, a cada três horas, com gasto em anúncios, faturamento e ROAS. Os primeiros envios foram aceitos pelo provedor. A composição do grupo e o acesso de todos os participantes são conferidos antes de enviar. A criação do grupo foi uma ação operacional, sem ferramenta de criação na Judite. [Central #21](https://github.com/avant-grupo/central/pull/21).

## Entrada única publicada, 14/11/2026

Os dashboards e o Creator Studio passaram a usar a entrada comum pela Central também na abertura direta. A publicação dos quatro produtos foi concluída e verificada online. [Estado da frente](../projetos/automacoes-empresa.md).
