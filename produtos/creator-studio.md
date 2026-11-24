# Creator Studio

## Propósito

Pesquisa de referências, estratégia, roteiro, criação e edição de conteúdo, geração UGC e gestão da produção.

## Escopo

Análise e mineração de referências; roteiros e formatos; geração de imagens e vídeos; edição; gestão de criadores, acordos e entregas.

## Limites

Produção é uma capacidade própria do Studio. A integração com a Central é opcional. As regras editoriais dependem da marca e do projeto.

## Estado resumido em 2026-11-05

Em 05/11/2026, o modo UGC Resposta direta foi publicado, com catálogo de copy e escolha separada dos modelos de B-roll e avatar. Um lote de quatro vídeos GomaPet exercitou versões narradas e mistas com fala para a câmera. Outros incrementos locais e fases planejadas continuam descritos nos projetos; a verificação técnica não comprova resultado de campanha.

Em 06/11, a regra de direção de gestos UGC16 foi refinada e validada localmente, orientando função do objeto e checagem da pose antes da animação. Publicação pendente; [estado e aplicação na geração UGC](../projetos/geracao-ugc.md).

## Código e projetos

[Repositório do produto](https://github.com/avant-grupo/creator-studio).

- [ferramenta criadores](../projetos/ferramenta-criadores.md)
- [geracao ugc](../projetos/geracao-ugc.md)
- [central conteudo criadores](../projetos/central-conteudo-criadores.md)
- [producao de video](../projetos/producao-de-video.md)
- [conteudo igor](../projetos/conteudo-igor.md)

## Entrada única publicada, 14/11/2026

A entrada direta usa automaticamente a Central, mantendo empresas e perfis. Aplicativo e backend publicados e conferidos online pelo [PR #32](https://github.com/avant-grupo/creator-studio/pull/32). [Estado da frente](../projetos/automacoes-empresa.md).

## Visual de Modelar um vídeo publicado, 21/11/2026

A bancada ganhou uma entrada que começa pelo arquivo, compara lado a lado as falas da referência e as reescritas e permite navegar pelos blocos da copy. A publicação do [PR #35](https://github.com/avant-grupo/creator-studio/pull/35) foi conferida na bancada autenticada, no desktop. O estado da geração de mídia está na [frente de UGC](../projetos/geracao-ugc.md).

## Fila e montagem de UGC, 22/11/2026

A bancada passou a preservar recibos de geração, parar pedidos que ainda estão na fila e recuperar montagens interrompidas. A checagem de quadros aponta trechos quase estáticos e faixas escuras. O [PR #37](https://github.com/avant-grupo/creator-studio/pull/37) foi publicado e conferido na bancada.

## Reparo de rótulo no UGC, 22/11/2026

A bancada passou a corrigir o rótulo pelo nome cadastrado ou por uma foto escolhida da ficha. Cada resultado fica no histórico de tentativas para revisão. Os dois modos foram conferidos na bancada em produção. [Entrega do Creator Studio](https://github.com/avant-grupo/creator-studio/pull/39).

## Ajustes de imagem no UGC, 22/11/2026

A correção livre passou a enviar ajustes locais compatíveis no mesmo pedido. O piloto existente foi conferido depois da publicação. [PR #40](https://github.com/avant-grupo/creator-studio/pull/40).

## Foto da ficha na correção livre, 22/11/2026

A correção livre passou a aceitar uma foto escolhida da ficha junto com outra tomada opcional. A imagem gerada fica disponível para revisão e o pedido anterior pode ser consultado na bancada. A publicação foi conferida em produção. [PR #41](https://github.com/avant-grupo/creator-studio/pull/41).

## Direção de cena no Roteiro, 22/11/2026

O Roteiro passou a registrar enquadramento, aparelho em cena e apoio na abertura de recipientes. A bancada pede edição quando identifica conflito entre a direção e a ação. Os controles foram conferidos na bancada publicada. [PR #38](https://github.com/avant-grupo/creator-studio/pull/38).

## Roteiros UGC que vendem e soam falados, 24/11/2026

O roteiro passou a ser escrito em três etapas: história, oralidade e decupagem. Entre elas, o próprio Studio mede vícios de texto escrito e devolve a fala uma vez para correção. O Studio deixou de suavizar as falas por conta própria. Na resposta direta, a regra de saúde só veta uma fala quando o parecer aponta o trecho e o código o encontra no roteiro.

A bancada ganhou variações de gancho sobre um corpo fixo e prévia de voz da copy modelada. A conferência automática agora aponta a fala de pagamento que perdeu a condição da oferta.

Antes do merge, quatro modelos revisaram a mudança em nove rodadas, até nota 9. O [PR #43](https://github.com/avant-grupo/creator-studio/pull/43) foi publicado e conferido na bancada em produção, sem nova geração paga.
