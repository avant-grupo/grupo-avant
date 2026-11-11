# Evolução do BI GomaPet

Contexto atualizado em 2026-11-06.

## Objetivo

Melhorar leitura de vendas, atribuição, tráfego e financeiro preservando consistência dos números.

## Estado documentado

Produto publicado; integrações e conciliação em acompanhamento. Em 06/11, publicada a correção de crédito dos links por kit que enviam o nome do atendente separado da identificação da oferta. Lojas, Minhas Vendas e comissões reconhecem a mesma prioridade, preservando atribuições anteriores. Deploy saudável e pedidos anteriores conferidos pela API e pelo SQL publicado. [PR da correção](https://github.com/avant-grupo/gomapet-frontend/pull/7).

## Próxima ação e dependências

Revalidar integrações e pendências por origem dos dados. Uma referência visual foi recebida em 06/11 para futura revisão do dashboard; telas e direção ainda precisam ser definidas. Conciliação com documentos externos depende da operação financeira.

## Relações

Produto relacionado: [gomapet-bi](../produtos/gomapet-bi.md). Demandas relacionadas estão no [backlog](../backlog/README.md); a responsabilidade individual é confirmada na demanda.

## Preparação operacional de 07/11/2026

Novos links de campanha e rascunhos de automação foram preparados para validação operacional. O teste do público VIP foi preparado por mensagens privadas no suporte, preservando o grupo existente. Os dois modelos VIP foram aprovados e as simulações internas conferidas; a seleção final dos participantes e os testes de entrega ainda antecedem a ativação. A ativação e o envio ainda não ocorreram. As regras do BI e os fluxos já publicados foram preservados.


## Conversão monetária, implementação local em 08/11/2026

Tráfego, campanhas e criativos passaram a usar as cotações históricas de cada dia, seguindo o critério do financeiro. Receitas de pedidos em reais permanecem sem reconversão; falta de histórico deixa a conversão indisponível. Testes automatizados, build e fluxo local no navegador foram conferidos, incluindo comparação com dados reais em somente leitura. A alteração ainda não foi publicada no produto; próxima etapa é autorizar a publicação e conferir a versão online.


## Extrato diário de anúncios, implementação local em 08/11/2026

Preparado o extrato por conta, acessível na Tráfego e na Viabilidade, com gasto diário, cotação aplicada, origem, encargos e histórico. Dias encerrados preservam a cotação; fechamento e reabertura da conferência são restritos a administradores e exigem motivo. Revisões recebidas após fechamento ficam pendentes e preservam o custo aprovado. Testes automatizados, build e fluxo no navegador com banco descartável foram verificados. A alteração permanece local e ainda depende de publicação e conferência online. A conciliação de faturas não faz parte desta entrega.

## Cotação e extrato diário publicados em 08/11/2026

A conversão diária e o extrato por conta foram publicados na GomaPet, com origem da cotação, encargos, histórico e conferência mensal. Tráfego/Criativos, Vendas, DRE, Viabilidade e o painel do extrato foram conferidos online, incluindo uso no celular e comparação dos valores no mesmo período. Dias anteriores preservam a cotação aplicada; correções e fechamento exigem perfil administrativo e motivo. Histórico antigo recuperado agora fica identificado. A conciliação de faturas permanece como etapa separada. [Publicação no produto](https://github.com/avant-grupo/gomapet-frontend/pull/13).

Conferência complementar concluída na mesma data: ajuste de arredondamento decimal publicado e validado na API, no banco e na tela, com trilha de revisão preservada. [Complemento publicado](https://github.com/avant-grupo/gomapet-frontend/pull/14). O aceite operacional do Igor ainda não foi registrado.
