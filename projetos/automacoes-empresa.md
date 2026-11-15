# Automações e Judite

Contexto preparado em 2026-11-05.

## Objetivo

Apoiar o trabalho da equipe com demandas, resumos e assistência da Judite.

## Estado documentado

Central publicada; novos fluxos em evolução.

Atualização de 11/11/2026: Gestão > Resumos foi ampliada e publicada para GomaPet, X1 e X1 Yuri, com métricas, filtros, período, frequência e destinatários por operação. O resumo diário anterior foi preservado. Novos resumos começam pausados; o piloto das duas X1 foi configurado na continuação descrita abaixo. A GomaPet oferece faturamento, pedidos e ticket por hora de pagamento em Yampi/Payt; custos e lucro continuam no consolidado diário. Dados ausentes permanecem indisponíveis. [Central #20](https://github.com/avant-grupo/central/pull/20) e dashboards [#33](https://github.com/avant-grupo/avant-bi/pull/33), [#34](https://github.com/avant-grupo/avant-bi/pull/34).

## Próxima ação e dependências

Mapear processos reais e separar configuração, adoção e desenvolvimento. A existência de uma ferramenta não demonstra adoção pela equipe.

## Relações

Produto relacionado: [central](../produtos/central.md). Demandas relacionadas estão no [backlog](../backlog/README.md); a responsabilidade individual é confirmada na demanda.


## Resumos em grupo e individuais, 11/11/2026

A Central passou a enviar resumos a grupos registrados por operação. Os resumos da X1 Yuri foram ativados no grupo próprio; os da X1 normal seguem diretamente para Igor, a cada três horas, com gasto em anúncios, faturamento e ROAS. Os primeiros envios foram aceitos pelo provedor. A composição do grupo e o acesso de todos os participantes são conferidos antes de enviar. A criação do grupo foi uma ação operacional, sem ferramenta de criação na Judite. [Central #21](https://github.com/avant-grupo/central/pull/21).


## Consultas dos resumos, 14/11/2026

Aplicada otimização nos backends X1 e X1 Yuri e no Rastrack. Os resumos passaram a
usar os metadados cadastrados das contas e a reutilizar leituras completas da mesma
janela por cinco minutos. O Rastrack reutiliza catálogos, coleta alterações entre
leituras completas diárias e agrega métricas por anúncio após comparação controlada.

Os três serviços foram publicados e verificados. A consulta usada pela Central
retornou gasto e ROAS completos para as contas das duas operações. Próximo passo:
observar os envios programados e medir a economia total de chamadas ao longo dos ciclos.
Não houve reenvio manual de resumo nesta entrega. As fontes do Rastrack continuam locais, aguardando incorporação ao fluxo de versionamento. O X1 foi incorporado ao PR #44 na publicação da entrada única. Este resumo público não foi publicado.

## Entrada única publicada, 14/11/2026

Publicada a entrada comum pela Central no BI, nas duas operações X1 e no Creator Studio. Os quatro serviços foram publicados e verificados online; o retorno à tela solicitada e os perfis foram preservados. O ajuste do X1 que já estava em produção também foi incorporado ao versionamento normal. [Dashboards #44](https://github.com/avant-grupo/avant-bi/pull/44) e [Creator Studio #32](https://github.com/avant-grupo/creator-studio/pull/32).
