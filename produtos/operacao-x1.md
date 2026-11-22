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

Também em 11/11, o faturamento do painel passou a incluir as vendas sem atribuição: pagamentos que o atendimento marcou como pagos e que o rastreamento não enviou à Meta por não encontrar o lead de origem. Elas aparecem separadas do que foi enviado à Meta e ficam fora das visões por conta de anúncio, criativo e anúncio. Antes, essas vendas não entravam no total.

A investigação mostrou que a maior parte desses casos no dia veio de atraso no processamento das entradas pelo rastreamento: a compra era avaliada antes de o lead existir. As compras do dia com origem comprovada foram reprocessadas e enviadas com o horário original. A correção que reavalia a compra sozinha quando o lead aparece foi publicada no rastreamento no fim da tarde do mesmo dia e passou a recuperar essas compras sem intervenção. O atraso no processamento das entradas continua em aberto: enquanto ele durar, o lead aparece depois e a compra entra como sem atribuição até ser reavaliada.

## Atualização de 2026-11-12

A X1 passou a manter uma base própria de clientes, separada do ROI Chat e do rastreamento: contatos com etiquetas e campos, etapas do funil, conversas, comprovantes e demais arquivos recebidos, além de uma cópia dos leads, entradas, eventos e avisos de compra do rastreamento. O objetivo é não perder histórico quando o ROI Chat apaga contatos ao chegar no limite do bot, nem quando a conversa sai da janela de um mês da API. A leitura do ROI Chat ficou incremental, porque a cota da API não comportava reler todos os contatos a cada 10 minutos, e o histórico das semanas anteriores foi carregado a partir das coletas já feitas. As conversas restantes entram aos poucos, dentro da cota. Nenhum fluxo do ROI Chat foi alterado. [Dashboards #35 a #41](https://github.com/avant-grupo/avant-bi/pull/35).

## Código e projetos

[Repositório do produto](https://github.com/avant-grupo/avant-bi), em `apps/x1`. O repositório `operacao-x1` foi arquivado em 11/11/2026.

- [operacao x1](../projetos/operacao-x1.md)


## Resumos por operação publicados em 11/11/2026

As instalações X1 e X1 Yuri oferecem à Central resultados de faixas exatas de pagamento e gasto horário real da Meta, com filtros de conta, campanha e anúncio. Resultado após anúncios é faturamento menos mídia. Fonte indisponível mantém gasto e resultado indisponíveis com aviso. O editor usa busca para o histórico de campanhas e anúncios. A ativação do piloto e os acessos da nova operação permanecem para configuração. [Dashboards #33](https://github.com/avant-grupo/avant-bi/pull/33) e [#34](https://github.com/avant-grupo/avant-bi/pull/34).


Atualização de 14/11/2026: corrigida a dependência de leitura de metadados ao montar
resumos de gasto e ROAS. As duas instalações usam cadastro de fuso/moeda e reutilizam
somente consultas completas e recentes da mesma janela. Consulta real pela Central
verificada sem avisos; acompanhamento do próximo envio automático ainda pendente.

## Entrada única publicada, 14/11/2026

As duas instalações usam automaticamente a Central na entrada direta, com provisionamento dos novos usuários autorizados e preservação das permissões existentes. Publicação concluída e conferida online; a otimização anterior foi preservada no código versionado. [PR #44](https://github.com/avant-grupo/avant-bi/pull/44).

## Custo por lead e consultas da secretária, publicados em 16/11/2026

O painel das duas instalações ganhou o card "Custo por lead" em Leads e conversão, com comparação ao período anterior, e a mesma coluna na tabela por número. O cálculo é o que o painel já fazia: gasto de anúncios dividido pelos leads novos, com os mesmos filtros. Sem lead novo ou sem conta de anúncio ligada, o campo fica vazio e diz o motivo. [Dashboards #46](https://github.com/avant-grupo/avant-bi/pull/46).

No mesmo dia, o limite de consultas de leitura por agente foi ampliado. A secretária da Central recebia recusas ao comparar funil e compras em vários recortes seguidos; depois da publicação, uma sequência de 30 consultas passou sem recusa. A leitura por agente da X1 Yuri segue sem configuração, e ainda não há consulta de ROAS da X1. [Dashboards #45](https://github.com/avant-grupo/avant-bi/pull/45).

Também em 16/11, o painel deixou de contar como compra descartada um lead qualificado recebido em repetição. [Dashboards #47](https://github.com/avant-grupo/avant-bi/pull/47).

## Pix sem comprovante no X1 Yuri, 16/11/2026

O robô do X1 Yuri só marcava venda quando o cliente mandava o comprovante. Quem pedia a outra pessoa para fazer o Pix ficava sem venda marcada e continuava sendo cobrado, mesmo com o dinheiro na conta. Agora, quando o cliente diz que pagou e não tem o comprovante, o robô pergunta o nome de quem fez o Pix e o valor, deixa uma nota na conversa, suspende as cobranças e marca o contato para a equipe conferir no extrato. A marcação de pago depois da conferência ainda é manual. Quando o comprovante mostra outro recebedor, o robô diz ao cliente o nome que aparece nele, explica que o valor não chegou, manda a chave certa e marca o contato para conferência.
