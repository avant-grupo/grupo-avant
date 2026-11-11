# Operação X1

## Propósito

Acompanhamento de ofertas e vendas por atendimento no WhatsApp, com métricas próprias da operação X1.

## Escopo

Vendas, funil, tráfego, criativos e leitura de dados de atendimento e rastreamento.

## Limites

A X1 mantém painel, regras e configuração separados da GomaPet. Integrações de atendimento e rastreamento podem pertencer a outros serviços.

## Estado resumido em 2026-11-05

Painel publicado, com melhorias de criativos registradas em 2026-11-05. As demais entradas do backlog precisam de conferência individual.

## Atualização de 2026-11-08

A X1 passou a oferecer consultas só de leitura para a secretária da Central diagnosticar dúvidas de rastreamento, eventos, compras, funil e conversas do bot. Nenhuma consulta altera campanhas, rotas, fluxos ou conversas.

No mesmo dia, o Funil X1 passou a reconhecer as etapas do bot do número 7900, que usa o agente de IA da GomaPet. Antes disso, a etapa 0 desse número aparecia quase vazia por erro de leitura, não por perda real de leads.

## Atualização de 2026-11-10

O painel ganhou a tela Viabilidade, no modelo da GomaPet. Ela parte do faturamento do produto principal mais o upsell, que aparece em linha própria, e desconta o gasto de anúncios, os impostos e os custos fixos e variáveis cadastrados. O custo fixo entra proporcional aos dias do período. A conta usa só os números da X1; o número de atendimento da GomaPet fica de fora porque já entra na viabilidade da GomaPet. O que o Igor chama de custo variável ainda está por definir.

No mesmo dia, o painel deixou de misturar dados da GomaPet. O rastreamento é compartilhado, e o painel somava o número e as contas de anúncio da GomaPet aos totais da X1, com algumas contas contadas duas vezes. Agora as telas mostram só os números da X1. A consulta de diagnóstico da Central continua vendo os dois.

## Atualização de 2026-11-11

Começou a ser montada uma segunda operação da X1, a X1 Yuri, com atendimento todo por IA e em outro número de WhatsApp, o 7891. Ela fica separada da operação atual para os resultados das duas poderem ser comparados. O funil desse número foi publicado com rastreamento próprio: leads, etapas e compras entram só no 7891 e não se misturam com o outro número. No painel, basta filtrar por número. Na Central existe a empresa X1 Yuri para as demandas da operação.

Ainda falta ligar o número à conta de anúncio, à página e ao pixel em que os anúncios vão rodar. Até lá, nada desse número é enviado à Meta. Persona, textos e áudios do atendimento também estão em definição.

No mesmo dia, o painel da X1 ganhou a interface do BI GomaPet: menu lateral, filtros no cabeçalho, cards com comparação ao período anterior e configurações em painel à direita. Números, regras e acessos não mudaram. O código foi para o repositório dos painéis, o [avant-bi](https://github.com/avant-grupo/avant-bi), junto com o BI.

## Código e projetos

[Repositório do produto](https://github.com/avant-grupo/avant-bi), em `apps/x1`. O repositório `operacao-x1` foi arquivado em 11/11/2026.

- [operacao x1](../projetos/operacao-x1.md)
