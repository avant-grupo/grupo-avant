# BI GomaPet

## Propósito

Gestão de vendas, mídia, financeiro e desempenho da GomaPet.

## Escopo

Vendas e pedidos; atribuição de origem; tráfego e criativos; financeiro e viabilidade; painéis e métricas.

## Limites

Os números devem usar os contratos e o motor de cálculo do próprio BI. O painel da X1 é outro produto. Integrações dependem de dados e acessos adequados.

## Estado resumido em 2026-11-05

Produto publicado. O contexto de 2026-11-05 registra uma nova bancada de criativos publicada; aceite e conciliação externa continuam etapas próprias.

## Código e projetos

[Repositório do produto](https://github.com/avant-grupo/avant-bi), em `apps/gomapet`. Até 11/11/2026 o repositório se chamava `gomapet-frontend`; os links antigos redirecionam.

- [dashboard bi](../projetos/dashboard-bi.md)
- [dashboard modular](../projetos/dashboard-modular.md)
- [checkout proprio](../projetos/checkout-proprio.md)

## Atualização de 06/11/2026

Publicada a correção de atribuição dos links por kit com nome do atendente em campo separado. Lojas Yampi, Minhas Vendas e comissões preservam a prioridade dos vínculos existentes; os pedidos anteriores passam a ser reconhecidos sem reescrita dos valores. [PR e código publicado](https://github.com/avant-grupo/gomapet-frontend/pull/7).


## Conversão monetária, implementação local em 08/11/2026

Tráfego, campanhas e criativos passaram a usar as cotações históricas de cada dia, seguindo o critério do financeiro. Receitas de pedidos em reais permanecem sem reconversão; falta de histórico deixa a conversão indisponível. Testes automatizados, build e fluxo local no navegador foram conferidos, incluindo comparação com dados reais em somente leitura. A alteração ainda não foi publicada no produto; próxima etapa é autorizar a publicação e conferir a versão online.


## Extrato diário de anúncios, implementação local em 08/11/2026

Preparado o extrato por conta, acessível na Tráfego e na Viabilidade, com gasto diário, cotação aplicada, origem, encargos e histórico. Dias encerrados preservam a cotação; fechamento e reabertura da conferência são restritos a administradores e exigem motivo. Revisões recebidas após fechamento ficam pendentes e preservam o custo aprovado. Testes automatizados, build e fluxo no navegador com banco descartável foram verificados. A alteração permanece local e ainda depende de publicação e conferência online. A conciliação de faturas não faz parte desta entrega.

## Cotação e extrato diário publicados em 08/11/2026

A conversão diária e o extrato por conta foram publicados na GomaPet, com origem da cotação, encargos, histórico e conferência mensal. Tráfego/Criativos, Vendas, DRE, Viabilidade e o painel do extrato foram conferidos online, incluindo uso no celular e comparação dos valores no mesmo período. Dias anteriores preservam a cotação aplicada; correções e fechamento exigem perfil administrativo e motivo. Histórico antigo recuperado agora fica identificado. A conciliação de faturas permanece como etapa separada. [Publicação no produto](https://github.com/avant-grupo/gomapet-frontend/pull/13).

Conferência complementar concluída na mesma data: ajuste de arredondamento decimal publicado e validado na API, no banco e na tela, com trilha de revisão preservada. [Complemento publicado](https://github.com/avant-grupo/gomapet-frontend/pull/14). O aceite operacional do Igor ainda não foi registrado.

## Atualização de 09/11/2026

Publicada a ação de perfil "Configurar os blocos do Retorno por campanha", que permite à gestão de tráfego criar e mudar os blocos da tela Tráfego sem ser administradora. O bloco novo passa a entrar no topo da lista, e a Judite pode explicar o que cada bloco soma (gasto por campanha e vendas por campanha e UTM) e alterar os blocos com a permissão da própria pessoa. Liberação para o perfil e aceite ainda pendentes. [PR e código publicado](https://github.com/avant-grupo/gomapet-frontend/pull/15).

## Resumo comercial com todas as lojas, publicado em 10/11/2026

O resumo comercial que a Judite consulta somava só Yampi e Payt, enquanto a tela Vendas soma também Mercado Livre, Shopee, Pagah e Vendas Extras. Por isso a resposta dela ficava abaixo do total da tela. O resumo passou a ler os mesmos pedidos da tela, com a divisão por loja, e o total foi conferido online contra a DRE e o banco no mesmo dia. A API externa do resumo também passou ao total de todas as lojas. [PR e código publicado](https://github.com/avant-grupo/gomapet-frontend/pull/20).

## Venda influenciada pelo disparo, publicado em 10/11/2026

A tela WhatsApp, na seção Disparos, passou a mostrar a venda de quem recebeu um disparo de WhatsApp e comprou por outro link, separada da venda pela UTM do disparo. O administrador cadastra a etiqueta que o disparo aplicou e o dia do envio; o BI conta os pedidos pagos do mesmo telefone até 7 dias depois e mostra por onde cada pedido entrou. Cadastro, tabela e painel foram conferidos online, inclusive no celular, contra uma conferência independente no banco. O número indica influência, não causa: o pedido continua contando no canal de origem. [PR e código publicado](https://github.com/avant-grupo/gomapet-frontend/pull/22).

## Tráfego: totais por campanha e troca de período, publicado em 10/11/2026

A tabela de criativos passou a trazer todos os anúncios e campanhas com entrega, e o gasto de cada campanha agora bate com o Gerenciador da Meta (antes ela somava só os 60 anúncios que mais venderam por conta). Ao trocar o período, a tela mantém os números anteriores esmaecidos até os novos chegarem, sem voltar ao topo. Em "Dados dos pedidos", a venda pela UTM passou a casar com campanhas que ganharam emoji no nome. Publicado em três PRs do [repositório do produto](https://github.com/avant-grupo/gomapet-frontend) e conferido em produção.

## Atualização de 11/11/2026

O BI e o painel da X1 passaram a viver no mesmo repositório, o [avant-bi](https://github.com/avant-grupo/avant-bi), cada um com o próprio servidor, regras e publicação. A base visual do BI virou um pacote compartilhado, para que os próximos painéis já nasçam com a mesma interface. A tela do BI não mudou.


## Formulário de dados de entrega Pix, publicado em 11/11/2026

Publicado pelo [PR #31](https://github.com/avant-grupo/avant-bi/pull/31), commit 6918425. O cliente preenche nome e dados de entrega por um link individual no celular. Em Vendas Extras, a operação acompanha o recebimento, renova um link ainda não usado e recupera o aviso ao atendimento sem duplicar a venda. O aviso tem tentativas automáticas, e a regra do atendimento reconhece dados já recebidos. Testes, banco descartável e navegador conferidos; deploy saudável e painel verificado online. Preenchimento não substitui conferência de pagamento. Próximo: acompanhar os primeiros usos com a operação; aceite ainda não registrado.


## Resumos por operação publicados em 11/11/2026

O BI passou a fornecer os dados dos resumos parametrizáveis da Central. O consolidado diário conserva seu cálculo; Yampi e Payt oferecem faturamento, pedidos e ticket médio pela hora real do pagamento. Custos, anúncios e lucro continuam no consolidado diário. O resumo anterior foi preservado, e nenhum novo envio foi ativado nesta publicação. [Dashboards #33](https://github.com/avant-grupo/avant-bi/pull/33).


## Gasto do Google Ads no Retorno por campanha, publicado em 11/11/2026

Publicado pelo [PR #32](https://github.com/avant-grupo/avant-bi/pull/32). Um script rodando na conta do Google Ads envia todo dia o gasto por campanha, que entra no bloco Google Ads com ROAS e CPA, como já acontece com a Meta. A tela avisa quando ainda não houve envio ou quando a última leitura tem mais de 36 horas, e recusa conta em moeda diferente de real. Ainda inativo: falta configurar o envio no servidor, trocar a fonte do gasto do bloco em "Configurar blocos" e o gestor de tráfego instalar o script na conta.

## Entrada única publicada, 14/11/2026

Entrada direta e renovação de sessão passam automaticamente pela Central, com perfis preservados. Publicado e verificado online pelo [PR #44](https://github.com/avant-grupo/avant-bi/pull/44). [Estado da frente](../projetos/automacoes-empresa.md).
