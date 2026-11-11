# Evolução da Operação X1

Contexto atualizado em 2026-11-08.

## Objetivo

Melhorar resultado por oferta, vendas, funil e criativos da operação de atendimento.

## Estado documentado

Painel publicado; frentes recentes em acompanhamento. Em 06/11, foi publicado um ajuste de continuidade diante de falha técnica na automação de atendimento. Melhorias de estabilidade do gateway de IA foram publicadas após os testes locais e conferidas por cenários controlados na API de produção. A homologação completa da conversa e a medição comparável do atendimento continuam pendentes. Também foi retomado o levantamento do canal WhatsApp com inventário operacional; a causa das diferenças entre o estado exibido da conta e o atendimento relatado segue sem confirmação.

## Próxima ação e dependências

Homologar a automação em contato controlado e acompanhar erros e tempo de resposta em janelas comparáveis depois da publicação. As demais frentes seguem separadas entre painel, rastreamento e automação de atendimento. Concluir o diagnóstico do canal relacionando estado da conta, modalidade de mensagem e confirmação de entrega.

## Relações

Produto relacionado: [operacao-x1](../produtos/operacao-x1.md). Demandas relacionadas estão no [backlog](../backlog/README.md); a responsabilidade individual é confirmada na demanda.

## Preparação do rastreamento de nova conta, 06/11/2026

Configuração da nova conta de anúncios concluída em produção após resolver o pré-requisito na Meta. Conta, destino e rota validados na API, no resolvedor de anúncios e na interface, com sincronização concluída e rotas anteriores preservadas. Isso supera o bloqueio inicial. A campanha permanece pausada; próxima ação é a ativação pelo tráfego e a conferência da primeira entrada e compra reais.

Atualização de 06/11: a revisão da campanha ativa identificou uma rota de rastreamento ausente, corrigida em produção com as rotas existentes preservadas. O envio foi validado com uma entrada real pendente, aceita como lead pela Meta no destino correto. Ainda há entradas anteriores a recuperar; a chegada automática de uma nova entrada após a correção e a compra continuam pendentes de validação.

Atualização de 06/11: a revisão da conexão da conta foi concluída após atender ao pré-requisito externo, preservando os destinos e todas as rotas. O envio foi revalidado com outra entrada real pendente, aceita como lead pela Meta, sem duplicar a validação anterior. A recuperação das demais entradas antigas e a observação de uma entrada automática nova e de uma compra continuam pendentes.

A sincronização da conta após a revisão foi concluída em 06/11, sem erro, e a conferência final preservou todas as rotas e a separação dos anúncios por destino.

Atualização de 06/11: a recuperação autorizada das entradas antigas de lead foi concluída, com aceitação pela Meta e preservação de horários e deduplicação. A conferência também identificou eventos de compra anteriores que aguardam decisão sobre recuperação; a observação de uma entrada automática nova continua pendente.

Atualização de 06/11: a recuperação dos eventos de compra anteriores foi autorizada e concluída, com aceitação pela Meta, valores e horários originais preservados e deduplicação conferida. O grupo de entradas e compras identificado está recuperado; a observação de novas entradas automáticas segue pendente.


## Medição dos aceites no atendimento, 06/11/2026

Nova demanda em triagem: distinguir a entrada, o primeiro aceite e o aceite após a apresentação da oferta, alinhando esses momentos às etapas exibidas no painel. Próxima ação é conferir os pontos de rastreamento do fluxo atual antes de propor ajustes na medição ou no roteiro. Não houve alteração do atendimento ou do painel nesta organização; a hipótese de simplificar a abertura ainda depende de avaliação.

Atualização de 06/11: as marcações das etapas foram revistas nos fluxos publicados. A conferência posterior identificou um aviso de passagem ainda desalinhado com a nova marcação; o alinhamento da instrumentação e a preservação da interpretação histórica seguem pendentes antes de considerar a medição concluída. Nenhuma correção operacional aplicada pelo agente nesta conferência.

Atualização de 06/11: os avisos de passagem foram alinhados e publicados nas duas versões do atendimento, preservando o roteiro e o histórico. A configuração publicada foi conferida e novos registros das três etapas chegaram ao painel. Isso supera a pendência de alinhamento acima. A próxima ação é acompanhar uma coorte diária nova e uma jornada completa; o período anterior continua com a interpretação histórica.

## Rastreamento de nova conta GomaPet, 06/11/2026

Uma nova conta de anúncios da GomaPet foi conectada à integração existente, com destino e rota de atendimento validados e anúncios sincronizados. A recuperação das entradas elegíveis guardadas foi concluída pelo fluxo nativo, com aceitação pela Meta, horários originais preservados e identificadores de evento únicos. Rotas anteriores preservadas. Uma entrada sem identificador de clique ficou inelegível; uma nova entrada automática após a recuperação e uma compra ainda aguardam conferência.

Atualização de 06/11: novas entradas automáticas foram confirmadas e uma compra anterior foi recuperada, com aceitação pela Meta. O rastreamento de carrinho abandonado foi ativado e validado com um evento real; o de pedido aguardando pagamento está ativo e aguarda o primeiro evento elegível dessa conta. A API recebeu uma correção pontual para combinar a origem da venda com o canal de atendimento. Horários originais, deduplicação e rotas anteriores foram preservados, com testes e prontidão do serviço conferidos. Isso supera a pendência anterior de nova entrada e compra; a próxima conferência é o pedido aguardando pagamento.


## Segunda ligação GomaPet, 07/11/2026

Outra conta de anúncios foi ligada ao atendimento existente, com todas as rotas anteriores preservadas e anúncios separados por página de destino. As entradas antigas elegíveis foram recuperadas pelo fluxo nativo, com aceitação pela Meta, horários originais e deduplicação conferidos; novas entradas automáticas também foram confirmadas. Dois eventos de pedido aguardando pagamento e um carrinho abandonado anteriores foram recuperados e aceitos. Registros sem identificador de clique permaneceram inelegíveis. A regra de compra continua ativa, sem compra atribuível a essa conta localizada nas fontes retidas nesta entrega. Configuração em produção, sem alteração de código ou nova publicação do serviço.


## Criação simplificada de campanhas, proposta de 07/11/2026

Estudo técnico iniciado: fluxo de criação, inventário de ativos, mídia, públicos, processamento e configurações inspecionados. A proposta é avaliar uma ferramenta interna de campanhas com destino WhatsApp usando a integração oficial e partes da infraestrutura existente. O levantamento de leitura foi ampliado e uma consulta de mídia com paginação foi reproduzida. Os efeitos alegados pelo fornecedor e a execução das operações de escrita não foram comprovados. Próxima ação é confrontar anúncios existentes e definir o escopo inicial. Nenhuma implementação ou campanha foi publicada por esse estudo; não há prazo de desenvolvimento acordado.

Atualização de 08/11: pesquisa complementar de fontes públicas concluída, com limites das evidências registrados no acervo privado. A validação dos resultados pretendidos em campanhas existentes continua pendente; a pesquisa não autoriza nem comprova uma implementação ou publicação de campanha.

Aprofundamento de 08/11 concluído: catálogo privado de fontes primárias e demonstrações públicas conferido, com protocolos para comparar campanhas existentes, representação dos criativos e formatos. A pesquisa registra falhas, limites e resultados negativos; as vantagens pretendidas continuam dependendo da medição na operação. Testes operacionais, implementação e publicação de campanha não foram executados.

Atualização específica de 08/11: investigada a compatibilidade entre mídia de catálogo e anúncios que abrem WhatsApp. Há modalidades documentadas, mas os formatos dinâmicos e sua disponibilidade exigem confirmação na configuração da operação. A pesquisa não comprova as vantagens pretendidas; nenhuma campanha ou implementação foi executada nesta etapa.

Atualização de 08/11: aprovada a direção de um publicador interno compartilhado por API e MCP. Primeira implementação local concluída para preparar planos e criar anúncios de vídeo pausados, com fila e conferência. Testes controlados passaram; recurso desligado e ainda sem homologação Meta real, interface nova, ativação, catálogo ou publicação de campanha. Próxima etapa é revisar e definir a configuração da homologação.

Atualização de 08/11, publicação: API e painel do rastreamento atualizados para a versão oficial 1.3.3, com as adaptações de recuperação preservadas. O publicador interno por API e MCP também foi publicado, com preparação de planos e criação pausada prevista; a criação na Meta permanece desligada até homologação. Backup, migrações e verificações de API e navegador concluídos. Nenhuma campanha criada; configuração da homologação, interface de criação e validação dos resultados pretendidos continuam pendentes.

Atualização de 08/11, tela de campanhas: o painel de rastreamento ganhou a tela de campanhas, com lista e criação guiada em etapas num painel lateral, publicada em produção e verificada no computador e no celular. A criação na Meta continua desligada e nenhuma campanha foi criada; falta escolher conta, página, número, vídeo, orçamento e agenda para a homologação de uma criação pausada.

## Estudo do atendimento para plataforma própria, 08/11/2026

Uma entrega incremental organiza caminhos de atendimento e requisitos de contexto, pagamento, acesso ao material, pausa e suporte para uma plataforma própria e um classificador de intenções. A ampliação do acervo e a revisão das classificações continuam. Taxonomia, regras de estado e avaliação são propostas, sem implementação operacional ou medição de acerto do classificador. Evidências e casos individuais permanecem no ambiente privado.

Atualização de 08/11, interface de campanhas: aprovada e implementada localmente a criação guiada, com lista de publicações, revisão das configurações, acompanhamento e interrupção de etapas futuras. Testes de interface, serviço e banco em isolamento e verificação no navegador passaram. A interface ainda não foi publicada na instalação; criação real de campanha, ativação e medição dos resultados pretendidos continuam pendentes.

## Operação paralela automatizada, decisão de 10/11/2026

Em reunião de 10/11, ficou decidido testar uma operação paralela com atendimento automatizado em outro número, com rastreamento próprio, para comparar o resultado com a operação de gestão manual. Novas variações de criativo e um upsell estão em preparação. Próxima ação: montar o funil e subir os primeiros anúncios. Nada publicado por esta decisão.
