# Teste de `instrucoes/montar-base.md` via API do Gemini — 02/11/2026

> **Teste via API, não na interface do app.** Mesmo conector e modelo do outro teste (`gemini-3.8-flash` indicado pela ferramenta; nome exato não confirmado em painel), temperatura 1, uma única chamada. Entrada: a instrução + `entrada-ficticia-politicas.md` (políticas POL-01 a POL-10) + as 14 dúvidas de `entrada-ficticia-perguntas.md` + "quem resolve" (pós-venda, logística, financeiro, comercial, plantão; exceção de entrega: "não sei"). Dados 100% fictícios.

## O que conferimos

| Critério | Resultado |
|---|---|
| Entregou A (CSV com o cabeçalho exato), B (pendências) e C (8 perguntas de teste) | Sim |
| Nenhuma linha marcada "aprovada" | Sim: 12 linhas "rascunho" e 2 "A CONFIRMAR" |
| Toda resposta com fonte (POL-xx, v1) | Sim |
| Lacunas viraram A CONFIRMAR em vez de invenção | Sim: exceção de entrega (POL-04) e prazo de troca (POL-08) |
| Preço, prazo ou condição fora das políticas | Não encontramos. Uma frase sem fonte direta: na linha "Cadê meu pedido?", "Para verificarmos seu caso, envie o número do pedido" (pedido razoável, mas não está na política — a revisão humana decide) |
| Destino de encaminhamento | Conforme "quem resolve"; exceção de entrega ficou A CONFIRMAR, como pedido |
| Pendências úteis | 4: responsável por exceção de entrega; prazo de troca; esclarecer sábado (atendimento abre, retirada não); quem altera endereço antes da separação |
| Lacuna que deixou passar | **Não apontou** que não existe regra para pagamento identificado depois das 12h |
| Formato utilizável | 11 colunas em todas as linhas, sem ";" dentro dos textos (conferido a olho). Um trecho de 4 linhas, com o campo "passar para pessoa" encurtado em 3 delas, passou no `scripts/conferir_base.py` sem erro |
| Estilo | O campo "passar para pessoa quando" repetiu a mesma lista longa em todas as linhas. Funciona, mas fica pesado: na revisão, deixe só o que é específico de cada dúvida (as regras gerais já estão na instrução do assistente) |
| Perguntas de teste | 8 perguntas difíceis e pertinentes (fora da base, desconto, exceção, Procon, tentativa de burlar as regras, machucado, dados de cartão, pedido já separado). Os números de cartão, pedido e endereço que o modelo inventou para essas perguntas são fictícios; não use dados reais nos seus testes |

## Conclusão

A instrução de montagem entrega um rascunho de base revisável, sem aprovar nada e marcando as lacunas principais. **Não substitui a revisão do dono**: neste teste, uma lacuna (pagamento depois das 12h) passou sem aviso, e uma frase sem fonte direta entrou. Por isso o `CHECKLIST.md` manda ler cada linha antes de mudar o status para "aprovada".

Não testado: ChatGPT, Claude, interface do Gemini; regras coladas como PDF ou print; conversa em que a IA precisa fazer perguntas (aqui a entrada já estava completa).
