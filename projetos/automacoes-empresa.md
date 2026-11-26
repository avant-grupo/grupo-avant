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

Em 18/11/2026, os resumos das duas operações X1 passaram de a cada três horas para três envios por dia, às 9h, 15h e 21h, cada um cobrindo o período desde o anterior. Avisos e resumos que passam de duas horas na fila, como depois de uma queda do WhatsApp, deixam de ser enviados, e a Central espaça os envios para não mandar mensagens em sequência. [Central #30](https://github.com/avant-grupo/central/pull/30).


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

## Resumos periódicos retomados, 16/11/2026

Publicada na Central a correção que devolveu os envios dos resumos programados, parados desde 15/11 em uma operação e em um resumo individual. Um envio pulado na reserva passa a ficar registrado, o que antes acontecia em silêncio. Os dois resumos afetados voltaram a sair no mesmo dia. [Central #24](https://github.com/avant-grupo/central/pull/24).

## Agente do Igor em grupo de WhatsApp, em implementação, 16/11/2026

Decidido um agente que atende o Igor num grupo de WhatsApp com o Yuri, pelo número da Judite. A Central passa a encaminhar as mensagens desse grupo para o agente, que roda isolado em containers na infraestrutura do Grupo Avant, com memória própria e acesso de leitura às ferramentas da empresa. Ações com efeito externo exigirão confirmação do Igor no grupo. Código e operação estão em revisão, sem publicação e sem grupo criado; a Judite do privado continua como está.

## Agentes Claudinho no ar, 17/11/2026

O agente de 16/11 foi publicado como Claudinho, um agente por sócio (Igor, Gustavo e Manu), cada um no seu grupo de WhatsApp pelo número da Judite. Cada Claudinho consulta as ferramentas da empresa (anúncios, BI da GomaPet, painel X1, Central e ROI Chat) e age na Central como o próprio dono. Mudança em anúncio, demanda ou mensagem para outra pessoa só acontece depois do sim do dono no grupo; mudança em sistema vira pull request para revisão do Yuri; Pix, acesso de pessoa e exclusão continuam fora do alcance. No fim do dia o WhatsApp desconectou o número da Judite, e os Claudinhos e os avisos da Central ficam parados até a reconexão.

## Claudinhos com áudio e imagem, 18/11/2026

Os três Claudinhos passaram a transcrever áudio e vídeo que chegam como arquivo, a responder em áudio de voz e a gerar imagens, com as contas de OpenRouter e ElevenLabs do Igor. Cada chamada tem limite de custo e fica registrada com o valor. Imagem para anúncio continua sendo rascunho: subir na Meta depende do sim do dono.

## Agente do Igor vira Cláudio Montenegro, 18/11/2026

A pedido do Igor, o agente dele ganhou nome e foto "de CEO": agora se chama Cláudio Montenegro e assina assim no grupo. Os agentes do Gustavo e da Manu continuam como Claudinho.

## Claudinhos guardam preferências e criam as próprias skills, 18/11/2026

Cada Claudinho agora guarda como cada pessoa do grupo gosta de ser atendida (formato, tamanho, canal, horário) e ajusta isso quando a pessoa muda de ideia. Quando repete um método ou alguém ensina um passo a passo, o agente o guarda como skill própria na memória dele e passa a usar a partir da conversa seguinte. No fechamento de cada sessão, ele revisa preferências, tarefas e fichas. Preferência não muda as regras nem os limites do agente.

## Claudinhos mais rápidos e com avisos separados, 24/11/2026

Publicado em 24/11. Os três agentes passaram a responder por um processo que fica ligado, em vez de abrir um novo a cada mensagem, e a mandar o trabalho longo para subagentes com limite de tempo e de rodadas. Quando algo falha, o dono recebe um aviso simples no grupo e o detalhe técnico vai em particular para o moderador. O comando de parar interrompe o turno e os subagentes. A Central guarda o áudio original antes de transcrever e entrega as respostas sem espera na fila. O conector do ROI Chat ganhou histórico do contato, disparo de subfluxo e lote que pode ser retomado. Ainda não medido: tempo de resposta com os donos usando no dia a dia.

## Claudinhos dividem o que aprendem, 26/11/2026

Publicado em 26/11. Cada Claudinho continua com a memória própria, e agora existe também uma memória da empresa que os três consultam. Um curador lê o que cada agente aprendeu e leva para ela só o que serve a todos: como fazer as rotinas (logar na Meta, conferir criativos do Drive, ranquear ROAS, testar o funil do 7900) e os fatos do negócio, sempre com a origem e a data. Preferências, tarefas e assuntos pessoais de cada sócio ficam fora. Quando duas memórias dizem coisas diferentes, as duas versões ficam registradas lado a lado. A atualização roda toda madrugada, e na hora quando o dono pede que algo valha para todos. Na estreia entraram 19 fichas e 10 rotinas, e o agente do Gustavo passou de 1 para 10 rotinas disponíveis.
