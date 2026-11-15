# Evolução da Operação X1

Contexto atualizado em 2026-11-14.

## Retorno por anúncio novo, 14/11/2026

Publicada na operação paralela uma correção para quem já recebeu a oferta e volta por outro anúncio: a entrada do fluxo limpa a marca da etapa anterior, e a pessoa recebe a continuação em vez de ficar sem resposta. A proteção contra envio repetido na mesma passagem foi preservada. Os nove cenários do fluxo exportado passaram e um teste real confirmou a entrega. Falta observar um retorno orgânico.

## Recuperação de respostas tardias, 13/11/2026

Publicada na operação paralela a retomada automática de quem responde depois de vencer a espera da abertura. A regra atua somente na etapa inicial, preserva contatos que já avançaram ou têm pagamento registrado e ignora anexos sem resposta textual. Complementa a ampliação anterior para 24 horas. O caso de teste reproduziu a parada e depois confirmou a continuação até a oferta; respostas dentro do prazo e prevenção de repetição também foram verificadas. Configuração principal preservada e teste temporário removido.

## Vínculo de três contas de anúncios, 13/11/2026

Três contas de anúncios foram vinculadas ao atendimento da operação principal, com destino explícito de conversão e rotas existentes preservadas. Cadastro e três rotas ativas foram conferidos na API e por leitura independente. Também foi corrigida uma associação antiga de destino na conta já cadastrada, conferindo os anúncios atuais. Atualização de 13/11 às 16h51: sincronização concluída, entradas antigas e conversões pendentes recuperadas e aceitas pela Meta, com horários/valores preservados e sem repetição dos eventos anteriores. Novas entradas naturais foram conferidas nas três contas. O lote foi concluído; a rotina de reavaliação após sincronização exige uma correção para evitar novas paradas em recuperações futuras. A operação paralela permaneceu separada.

## Entradas dos anúncios na operação paralela, 13/11/2026

Publicado o cadastro das novas entradas de anúncios para selecionar a abertura e o atendimento correspondentes à peça. O inventário das duas contas e as verificações da regra publicada foram conferidos, preservando as receitas e os demais caminhos do fluxo. Ainda falta observar uma entrada real posterior. Sem mensagens de teste ou reprocessamento de contatos.

## Resposta sobre o conteúdo adicional, 13/11/2026

Publicada na operação principal uma orientação de atendimento para perguntas sobre o conteúdo adicional mantido em surpresa. O agente deve preservar o mistério e explicar a liberação após validar o pagamento, sem inventar conteúdo ou tratar ausência de compromisso como dívida. Configuração persistida e campos restantes preservados; verificações estáticas aprovadas. Ainda falta conferir a resposta numa conversa posterior à publicação.

## Resposta após pagamento na operação paralela, 13/11/2026

Publicada uma proteção para não acrescentar a chave de pagamento às respostas quando a compra já está paga. A cobrança de uma oferta adicional pendente continua disponível. Complementa o encerramento do atendimento anterior na aprovação do PDF. Doze cenários passaram no fluxo exportado, inclusive em cópia isolada; versão no ar conferida. Falta observar uma conversa posterior à publicação. Sem mensagens de teste ou pagamento simulado.

## Respostas ao lembrete na operação paralela, 13/11/2026

Publicado o aumento de 3 para 24 horas na espera por resposta ao lembrete da abertura, para atender quem responde depois de uma noite. Configuração no ar conferida, com texto e encaminhamento preservados. Esperas já vencidas não foram retomadas; a próxima verificação é uma resposta real após o prazo anterior e dentro do novo.

## Transição após pagamento na operação paralela, 13/11/2026

Publicada uma correção para encerrar o atendimento de IA anterior quando um comprovante em PDF é aprovado, antes de seguir ao pós-pagamento ou à oferta adicional. As rotas de recusa foram preservadas. A configuração publicada e as quatro rotas foram verificadas; o comportamento numa conversa real posterior ainda será observado. Sem simulação de pagamento nesta entrega.

## Atendimento revisado e registro de recusa publicados, 14/11/2026

O atendimento por IA da X1 Yuri passou a usar instruções mais curtas, voltadas a responder diretamente às dúvidas, depois de testes com um recorte de casos reais e revisão por três modelos. A IA agora registra quando a pessoa recusa ou informa um prazo, e as cobranças automáticas do funil principal conferem esse registro antes de enviar. A mensagem de abertura e os dois recontatos também foram ajustados. Provas feitas em contato de teste. Ficaram fora desta etapa o atendimento da oferta complementar e os fluxos de outras cópias; respostas na abertura continuam seguindo o funil. Próxima ação: revisar a oferta complementar e acompanhar a qualidade do número.

## Registro de recusa e prazo em teste isolado, 14/11/2026

Foi montado um ambiente de teste separado para registrar recusa ou prazo e conferir esse estado antes de uma cobrança. A guarda foi executada com campo vazio e com recusa, com entrega das duas mensagens de teste. Os agentes e fluxos do atendimento atual foram preservados. Qualquer prazo fica suspenso, sem retomada automática, e o atendimento desta etapa usa somente Pix. A chamada das funções pela IA ainda aguarda teste integrado; as cobranças atuais não foram migradas para essa política.

## Análise qualitativa da X1 Yuri, 14/11/2026

Concluída a leitura do recorte de atendimentos da operação atual, com classificação de dúvidas, objeções e problemas recorrentes e comparação descritiva dos caminhos. As propostas de melhoria estão preparadas para decisão; não houve alteração do atendimento por esta análise. Casos individuais, evidências e relatório completo permanecem no ambiente privado.

## Conta adicional na X1 Yuri, 14/11/2026

Uma terceira conta de anúncios foi vinculada ao rastreamento da X1 Yuri, preservando as duas anteriores. Quatro anúncios receberam o cadastro de origem no funil publicado; releitura e 65 verificações confirmaram a alteração restrita ao mapa de anúncios. A sincronização do catálogo foi solicitada e ainda aguarda a fila normal. A configuração não comprova a chegada de uma entrada ou compra; essa conferência permanece pendente. Campanhas e lances foram preservados.


## Objetivo

Melhorar resultado por oferta, vendas, funil e criativos da operação de atendimento.

## Estado documentado

Em 11/11, foi publicada uma correção no gateway de IA para respeitar o prazo de resposta do atendimento e recuperar chamadas seguras que ficam sem resposta. Testes automatizados, simulação de falhas com o código publicado e primeiras chamadas reais passaram. A medição por uma janela maior e a homologação completa das conversas continuam pendentes.

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

## Processamento de leads, 12/11/2026

Publicada uma correção no rastreador para reduzir o atraso entre a entrada e o envio do lead à Meta. O processamento evita revisões repetidas de pendências e lê um número limitado de entradas em paralelo. A fila anterior foi processada e os leads da operação paralela foram aceitos pela Meta, com testes de concorrência e deduplicação. Acompanhar o comportamento no próximo pico de tráfego; o aceite do evento e a atribuição no Gerenciador continuam sendo verificações distintas.

## Biblioteca interna de referências, 12/11/2026

Implementada uma biblioteca interna para consultar referências de criativos por país ou região, tema e origem, com busca em textos disponíveis, reprodução e download dos originais arquivados. A instalação local e o acesso entre computadores foram conferidos, assim como navegação em desktop e celular. A ampliação do acervo continua em andamento. Sem mudança no atendimento, publicação de campanhas ou resultado comercial medido.

## Atendimento conforme o anúncio, 12/11/2026

Na operação paralela, a abertura e o agente de IA do atendimento passaram a seguir o anúncio de origem: os anúncios com o especialista continuam com o atendimento do especialista, e os anúncios de indicação recebem um atendente que se apresenta como alguém que indica a receita. O áudio de abertura virou um só, neutro, para todos. Publicado no funil depois de testado numa cópia e no próprio funil; falta conferir com leads reais de cada tipo de anúncio.

## Respostas curtas ao preço, 12/11/2026

Corrigida na operação paralela a interpretação de aceites curtos com erro de digitação. O fluxo reconhece os aceites completos antes da IA e interpreta as demais respostas com a pergunta enviada. Recusa e dificuldade de pagamento mantêm seus caminhos próprios, sem pergunta adicional ao cliente. Publicado após testes pelo WhatsApp e avaliação de respostas preservadas; a configuração publicada foi relida. Resultado comercial não medido nesta entrega.

## Revisão dos storyboards, 12/11/2026

O lote de 20 storyboards da operação paralela recebeu revisão dos ganchos, textos na tela e duração das cenas. Os arquivos foram validados e os PDFs atualizados para avaliação, com as imagens existentes preservadas. Próxima etapa: aprovar a revisão e concluir ajustes visuais antes de produzir os vídeos. Sem publicação de campanha nesta entrega.

## Piloto de vídeo, 12/11/2026 à noite

A produção dos storyboards foi autorizada em paralelo à criação de novos formatos. Seis cenas do primeiro piloto foram geradas no Google Flow e montadas em uma prévia, com conferência local das falas e dos quadros. A chamada final foi recusada pela plataforma e ainda falta para concluir o vídeo. Próxima etapa: resolver a chamada e avaliar o piloto antes da expansão. Sem publicação de anúncio ou resultado comercial medido.


Atualização de 12/11 à noite: a produção passa a ser paralela, com um agente responsável por cada roteiro e revisão central das entregas. Três roteiros estão atribuídos à primeira rodada. Atribuição não representa geração concluída nem publicação de campanha.


Complemento de 12/11: os vídeos passam a receber trilha instrumental e transições breves na edição. A entrega será progressiva por peça completa e conferida, identificada pela tag; a associação de anúncios ao atendimento permanece separada. Teste de acabamento concluído em prévia, sem publicação de campanha.


Resultado da rodada paralela: três bases parciais geradas e conferidas, com lacunas por recusas da plataforma e uma falha de duração em parte dos clipes. O acabamento foi testado em prévia; nenhum vídeo completo foi entregue para campanha. Próxima etapa: resolver as cenas faltantes antes da entrega progressiva.

Atualização de 13/11: prévia revisada em velocidade de 1,2x, preservando a voz e mantendo a música no ritmo original. Ajuste conferido localmente e adotado para as próximas montagens. A chamada final continua pendente; sem entrega para campanha.

Atualização de 13/11: três variantes de vídeo receberam chamada visual na edição, preservando os takes aproveitáveis. Uma passou na conferência final automática; duas aguardam revisão complementar. A revisão e o envio ficaram centralizados no supervisor. Sem publicação de campanha nesta entrega.

Atualização de 13/11 às00h44: primeiro piloto entregue ao Igor pelo supervisor, como documento, após conferência final. As próximas peças seguem o mesmo pacote de revisão e envio centralizado. Sem publicação de campanha comprovada.

## Ritmo e continuidade dos criativos, 13/11/2026

Após a entrega inicial de quatro variantes, duas peças voltaram para ajuste de montagem. A revisão exige imagens em movimento, insertos curtos e correspondência entre quem aparece falando e o narrador. As versões anteriores ficam preservadas; novas versões passam por conferência de fala, texto e movimento e por revisão do supervisor antes do reenvio. A diretriz foi incorporada ao lote seguinte. Sem publicação de campanha comprovada nesta etapa.

As duas versões corrigidas concluíram a conferência técnica e aguardam revisão e reenvio centralizados no supervisor. A correção aproveitou a filmagem existente, preservou a fala e não gerou novas cenas. O aceite do reenvio e o resultado em campanha ainda não foram verificados.

Atualização de13/11: as duas correções de vídeo foram reenviadas e tiveram entrega confirmada pelo supervisor. A produção dos demais roteiros foi retomada; o próximo vídeo e os planos seguintes estão em preparação enquanto a plataforma de geração mantém uma restrição temporária. Sem publicação de campanha comprovada.

Atualização de13/11: parte da nova leva segue pendente por uma restrição externa na plataforma de geração. O material existente foi preservado e a edição/conferência local pode continuar; não há confirmação de conclusão dessas peças.


Atualização de 13/11, consolidação da produção: uma nova peça concluiu a conferência técnica e aguarda revisão e envio pelo supervisor. A leva seguinte, de 15 roteiros, permanece incompleta sob restrição da plataforma; material aproveitável foi preservado. Novas gerações seguem suspensas. Sem publicação de campanha comprovada.

Atualização de 13/11, retomada da supervisão: treze vídeos finais foram revisados e entregues. A frente de formatos concluiu 20 storyboards e 46 imagens, ainda sujeitos à seleção editorial. Os 15 roteiros seguintes ficaram suspensos por restrição da plataforma e recusas de conteúdo; a retomada sequencial será conferida antes de prosseguir. Arquivos e evidências preservados. Sem publicação de campanha comprovada.

Atualização de 13/11, revisão de acabamento: os treze vídeos entregues voltaram para ajuste local de câmera e transições, preservando trilha e arte; duas peças também terão a narração corrigida. A restrição da plataforma reapareceu mesmo na operação sequencial, e as quinze peças seguintes continuam suspensas. Materiais anteriores preservados, sem nova campanha publicada.

Conclusão local de 13/11: os treze arquivos corrigidos foram revisados e arquivados. O reenvio permanece pendente de coordenação do canal de entrega; as versões anteriores estão preservadas. Os quinze roteiros seguintes continuam suspensos pela plataforma e por decisões editoriais. Sem publicação de campanha nesta etapa.

Revisão complementar de 13/11: oito peças voltaram para redução dos títulos de abertura, preservando texto, duração e áudio. As versões anteriores continuam preservadas; o reenvio do conjunto aguarda revisão final. Ajuste local, sem novas cenas geradas ou campanha publicada.

Conclusão da revisão dos títulos em 13/11: oito versões atualizadas foram conferidas e substituídas na fila, preservando duração e áudio. O conjunto aguarda revisão final antes do reenvio; arquivos anteriores preservados, sem geração de novas cenas ou publicação de campanha.

Reabertura complementar de 13/11: cinco finais voltaram para ajuste local de trechos repetidos e reenquadramentos, que permaneceram após a correção anterior. O envio dessas versões fica retido até novos arquivos verificados e revisão final. As outras oito peças seguem preservadas; sem nova geração de cenas ou publicação de campanha.

Revisão de abertura em 13/11: oito peças passaram a manter apenas identificação e emojis, preservando áudio e duração. Novas versões conferidas e aguardando revisão final antes do reenvio; as cinco peças em correção de montagem continuam retidas. Arquivos anteriores preservados, sem novas cenas ou campanha publicada.


## Proteção da abertura do atendimento, 13/11/2026

Publicada no atendimento da X1 Yuri uma proteção para impedir que respostas seguidas repitam a mesma etapa inicial. Resposta, lembrete e reação usam a mesma marca de etapa. A configuração publicada e nove cenários sequenciais foram conferidos. A verificação em conversa posterior permanece pendente; execuções rigorosamente simultâneas ainda dependem da garantia de concorrência da plataforma.

Atualização de cobertura em 13/11: uma peça teve autorizada a produção sequencial de cenas adicionais para corrigir a falta de variedade na montagem; a primeira cena foi informada como concluída. Quatro candidatas locais aguardam aprovação editorial. As demais restrições de produção e a retenção do envio continuam; as oito peças da outra frente foram preservadas, sem publicação de campanha.

## Planejamento de testes, 11/11/2026

Discutida a comparação entre criativos que levam ao especialista e criativos com personagem, mantendo coerência entre chamada e atendimento. Também foi proposta a comparação entre mensagem geral e mensagens específicas por origem do anúncio. Próxima ação: definir execução e critérios de medição; este registro não comprova implantação dos testes nem resultado.


## Marcação por Pix, implementação local de 11/11/2026

O rastreador recebeu uma correção local para distinguir pagamentos Pix do mesmo valor pelo identificador bancário e impedir a duplicação do mesmo Pix entre atendimentos. Testes selecionados e integração com banco descartável passaram. O leitor determinístico e as alterações de conteúdo do fluxo também foram preparados, com revisão manual para evidência incompleta. A ligação dos campos e da fila, a homologação no atendimento e a publicação operacional continuam pendentes. Nenhuma recuperação histórica ou mudança no total do painel foi executada nesta etapa; casos financeiros permanecem no ambiente privado.


## Conferência de pagamentos publicada, 11/11/2026

O painel X1 ganhou uma tela de consulta dos avisos de pagamento que precisam de acompanhamento, com filtros e detalhe de motivo, etapa e referências para investigação. Avisos recuperados deixam a lista automaticamente. A consulta respeita o perfil e o workspace; não aprova pagamentos nem reenvia eventos. Publicação e verificações de serviço, banco em isolamento e interface no computador/celular concluídas. Próxima ação: conferir pendências e ampliar a captura anterior ao aviso, a prevenção de falhas e a resolução manual auditada. Conciliação bancária completa ainda não foi entregue nesta etapa.


## Recuperação automática do rastreamento, implementação local de 14/11/2026

Foi concluída e verificada localmente a retomada das entradas antigas que aguardavam o catálogo de anúncios, com lotes limitados, intervalo entre tentativas e proteção contra duplicação. A conferência periódica separa entradas, compras, pendências e confirmações de recebimento da Meta, sem atribuir conta quando a origem é desconhecida. Testes com PostgreSQL descartável e respostas Meta sintéticas passaram, incluindo preservação de valor, horário e destino e retomada depois de interrupção.

A correção ainda não foi publicada. Próxima ação: autorização de publicação, aplicação dos índices aditivos e conferência do ciclo real. Não houve reprocessamento em produção nem mudança de totais nesta entrega.

## Revisão do porta-voz dos criativos, 14/11/2026

Definida a divisão entre depoimento e oferta: mulher ou homem podem contar a experiência do casal; o homem que detém a receita faz a chamada final, coerente com o atendimento. As versões afetadas foram retidas e a correção pontual foi preparada, preservando os depoimentos. Uma checagem local passou a validar o porta-voz. Refação dos vídeos e revisão editorial continuam pendentes; não houve novo envio ou publicação de campanha.


## Montagem dos criativos parciais, 14/11/2026

Quatro peças que já tinham cenas foram montadas em versões curtas, com chamada final pelo homem da própria peça. A conferência de fala, movimento e quadros foi concluída; arquivos e versões anteriores foram preservados. As candidatas aguardam escuta editorial e aceite. Não houve envio ao cliente ou publicação de campanha por esta etapa.

Revisão posterior da montagem identificou retornos repetitivos a cenários e imagens fora do bloco de fala. A candidata do porteiro foi rejeitada e preservada. Os dez primeiros vídeos foram decupados para orientar a correção; as demais candidatas continuam em revisão. Não houve nova geração, remontagem ou envio por esse diagnóstico.

Após autorização para corrigir uma peça primeiro, o porteiro recebeu uma nova montagem por blocos da história, com fala e imagem vinculadas e correção do tempo do áudio. As conferências técnicas passaram e a versão aguarda avaliação antes de estender o ajuste às demais. Não houve nova geração ou envio ao cliente; anteriores preservadas.

Atualização de14/11: retirado um começo falso da fala na mesma peça, com áudio e imagem cortados juntos. A leitura literal foi integrada ao caminho de render e conferida antes e depois da edição; verificações técnicas passaram. O ritmo e a montagem receberam aprovação editorial em 14/11. Depois, foi escolhido e gerado um novo fechamento pelo próprio personagem, explicando que valor e entrega serão tratados no atendimento. A versão seguinte preserva o corpo aprovado e passou nas conferências técnicas; o novo CTA aguarda revisão editorial. As demais peças seguem preservadas, sem envio ao cliente ou publicação de campanha.


Atualização de 14/11, oralidade: definidos quatro perfis compartilhados de fala para variar entre os vídeos. O texto do piloto passou por revisões para um registro de conversa, com esclarecimentos da história e retirada de uma urgência sem contexto. Depois da aprovação do texto, as falas revisadas do piloto foram geradas e montadas, mantendo a menção ao valor na chamada. Conferências de texto, continuidade e sincronização passaram; a nova interpretação aguarda revisão editorial. Anteriores preservadas, sem envio ao cliente ou publicação de campanha.

## Padronização dos headers, decisão de 14/11/2026

Aprovado um padrão visual para os headers dos próximos vídeos e um catálogo inicial de pares de texto, escolhidos conforme a história de cada peça. O contrato de parametrização e as conferências foram documentados; a integração aos dois caminhos de montagem ainda está pendente. A decisão não comprova aplicação automática, refação de vídeos ou publicação de campanha.
