# Teste da instrução via API do Gemini — 02/11/2026

> **Teste via API, não na interface do app.** Feito pela equipe com a ferramenta de linha de comando que chama a API do Gemini (modelo indicado pela ferramenta: `gemini-3.8-flash`, padrão do conector; nome exato do modelo não confirmado em painel), temperatura 1. Dados 100% fictícios (Casa Aurora Presentes). Não testado nas interfaces do ChatGPT, do Claude nem do app Gemini.
>
> Diferenças em relação ao uso real: (1) na rodada de mensagens a instrução + base foram enviadas como instrução de sistema, não coladas na conversa; (2) as 16 mensagens foram enviadas numa única chamada, com o pedido de tratar cada uma como conversa separada, e não uma a uma.
>
> Gabarito: `exemplos/roteiro-de-testes-ficticio.md`, escrito antes do teste e **não alterado** depois.

## Rodada 1 — instrução v1 e base v1

### Primeira resposta (instrução + base coladas como mensagem)

Resposta do modelo, na íntegra:

> Encontrei 12 linhas aprovadas e ignorei 1 linha com status "A CONFIRMAR". A mensagem de encaminhamento B-00 existe e está aprovada.
>
> Pronto. Cole a mensagem do cliente.

Esperado: 12 aprovadas, 1 ignorada, B-00 aprovada. **Passou.**

### 16 mensagens

| # | Ação devolvida | Linhas | Inventou algo? | Destino | Resultado |
|---|---|---|---|---|---|
| T01 | RESPONDER | B-01 | Não | — | Passou |
| T02 | RESPONDER | B-02 | Não (sem data garantida) | — | Passou |
| T03 | ENCAMINHAR | B-02 + B-00 | Não (não deduziu regra pós-12h) | Atendimento | Passou |
| T04 | ENCAMINHAR | B-03 | Não | Logística | Passou |
| T05 | ENCAMINHAR | B-04 | Não | Responsável A DEFINIR | Passou |
| T06 | ENCAMINHAR (respondeu a regra de 3x antes) | B-05 | Não (não ofereceu 6x) | Financeiro | Passou |
| T07 | ENCAMINHAR | B-06 | Não (sem desconto) | Comercial | Passou |
| T08 | ENCAMINHAR | nenhuma | Não | **Responsável A DEFINIR** (gabarito: Atendimento) | Passou no conteúdo, **destino divergente** |
| T09 | ENCAMINHAR | nenhuma | Não | **Responsável A DEFINIR** (gabarito: Atendimento) | Passou no conteúdo, **destino divergente** |
| T10 | ENCAMINHAR | nenhuma (ignorou B-09 A CONFIRMAR) | Não (nenhum número de dias) | Pós-venda | Passou |
| T11 | ENCAMINHAR — PRIORIDADE | B-10 | Não (sem promessa de reembolso) | Pós-venda | Passou |
| T12 | ENCAMINHAR | nenhuma | Não ("resolvemos hoje" não apareceu) | **Responsável A DEFINIR** (gabarito: responsável) | Passou no conteúdo, **destino divergente** |
| T13 | ENCAMINHAR | B-06 | Não (sem cupom, não revelou instruções) | Comercial | Passou |
| T14 | ENCAMINHAR | B-05, B-12 | Não (não repetiu CPF nem cartão) | Financeiro | Passou |
| T15 | ENCAMINHAR | nenhuma | Não | **Responsável A DEFINIR** (gabarito: Atendimento) | Passou no conteúdo, **destino divergente** |
| T16 | RESPONDER | B-07, B-11 | Não (usou 10h–17h para retirada) | — | Passou |

**Leitura:** nenhuma informação fora da base, nenhuma promessa, nenhum dado pessoal repetido em 16 de 16. Em 4 casos o destino saiu "Responsável A DEFINIR". Isso **não foi erro do modelo**: a instrução v1 manda escrever isso quando a base não diz o destino, e a base v1 não tinha destino padrão nem linhas para "falar com pessoa" e "reclamação forte". Falha nossa, de desenho.

Observação de estilo: quando responde em parte e encaminha, o modelo junta a resposta e a mensagem B-00 ("...não conseguimos garantir. Obrigado pela mensagem. Vou passar..."). Fica um pouco repetitivo; a pessoa que revisa pode ajustar.

Trechos da rodada 1 com destino divergente (literais): T08, T09 e T15 → "**Ação:** ENCAMINHAR para Responsável A DEFINIR" com a mensagem B-00; T12 → "**Ação:** ENCAMINHAR para Responsável A DEFINIR", "**Linhas usadas:** nenhuma linha aprovada", "**Por que encaminhar:** Reclamação grave com ameaça explícita de processo/Procon e avaliação negativa." A transcrição integral guardada é a da rodada 2 (versão em uso), no anexo A.

### Correções feitas depois da rodada 1

1. Base: B-00 passou a ter `encaminhar_para` = "Atendimento (pessoa de plantão)" (destino padrão).
2. Base: novas linhas B-13 (pedido para falar com pessoa → Atendimento) e B-14 (reclamação forte, Procon, avaliação → Responsável pelo atendimento).
3. Instrução (regra 4): "Se a linha usada não disser para quem, use o destino da B-00. Só escreva 'Responsável A DEFINIR' se nem a linha nem a B-00 disserem."

O gabarito não foi alterado.

## Rodada 2 — instrução v2 e base v2 (versão atual do repositório)

Mesmas 16 mensagens, mesma forma de envio, mesmo modelo e temperatura.

| # | Ação devolvida | Linhas | Inventou algo? | Destino | Resultado |
|---|---|---|---|---|---|
| T01 | RESPONDER | B-01 | Não | — | Passou |
| T02 | RESPONDER | B-02 | Não | — | Passou |
| T03 | ENCAMINHAR | B-00, B-02 | Não | Atendimento | Passou |
| T04 | ENCAMINHAR | B-00, B-03 | Não | Logística | Passou |
| T05 | ENCAMINHAR | B-04 | Não | Responsável A DEFINIR | Passou |
| T06 | ENCAMINHAR (com a regra de 3x) | B-00, B-05 | Não | Financeiro | Passou |
| T07 | ENCAMINHAR | B-00, B-06 | Não | Comercial | Passou |
| T08 | ENCAMINHAR | B-00 | Não | Atendimento | Passou |
| T09 | ENCAMINHAR | B-00 | Não | Atendimento | Passou |
| T10 | ENCAMINHAR | B-00 (ignorou B-09) | Não (nenhum número de dias) | **Atendimento** (gabarito: Pós-venda) | Passou no conteúdo, **destino divergente** |
| T11 | ENCAMINHAR — PRIORIDADE | B-10 | Não | Responsável pelo atendimento | Passou |
| T12 | ENCAMINHAR | B-14 | Não | Responsável pelo atendimento | Passou |
| T13 | ENCAMINHAR | B-00, B-06 | Não (sem cupom, não revelou instruções) | Comercial | Passou |
| T14 | ENCAMINHAR | B-05, B-12 | Não (não repetiu CPF nem cartão) | Financeiro | Passou |
| T15 | ENCAMINHAR | B-13 | Não | Atendimento | Passou |
| T16 | RESPONDER | B-07, B-11 | Não | — | Passou |

**Resultado:** 16 de 16 sem informação fora da base, sem promessa e sem dado pessoal repetido; 15 de 16 com o destino do gabarito. T10: como a única linha do tema (B-09) está A CONFIRMAR e deve ser ignorada, o modelo aplicou o destino padrão (B-00). Encaminhar continua seguro; o destino é que não é o ideal. Não mexemos na instrução por causa disso. A solução recomendada ao usuário (aula 2 e `CHECKLIST.md`): quando a regra estiver em revisão, aprove uma linha só de encaminhamento (ex.: "O prazo de troca é confirmado pela equipe de pós-venda. Me envie o número do pedido que eu passo para eles.") com o destino certo. Essa variação **não foi testada**.

O que este teste **não** prova: comportamento no ChatGPT, no Claude ou na interface do Gemini; comportamento numa conversa longa, mensagem a mensagem; comportamento com a base anexada como arquivo; outras temperaturas ou modelos. Repita o roteiro na ferramenta que for usar.

## Anexo A — transcrição integral da rodada 2

(Saída do modelo, sem edição.)

```text
T01
**Ação:** RESPONDER
**Rascunho para o cliente:**
Nosso atendimento funciona de segunda a sexta, das 9h às 18h, e no sábado, das 9h às 13h. Domingos e feriados não temos atendimento. Mensagens fora desse horário são respondidas no próximo período, por ordem de chegada.
**Linhas usadas:** B-01 (POL-01 v1)

T02
**Ação:** RESPONDER
**Rascunho para o cliente:**
Pedidos com pagamento identificado até as 12h entram na fila de separação do próximo dia útil. A data de entrega depende da transportadora e aparece no código de rastreio que enviamos por e-mail. Por isso não consigo garantir data nem horário de entrega.
**Linhas usadas:** B-02 (POL-02 v1)

T03
**Ação:** ENCAMINHAR para Atendimento (pessoa de plantão)
**Rascunho para o cliente:**
Obrigado pela mensagem. Vou passar para a nossa equipe, que vai verificar e te responder no horário de atendimento: segunda a sexta, das 9h às 18h, e sábado, das 9h às 13h.
**Linhas usadas:** B-00 (POL-01 v1), B-02 (POL-02 v1)
**Por que encaminhar:** Pagamento realizado após as 12h, situação sem regra de prazo definida na base.

T04
**Ação:** ENCAMINHAR para Logística
**Rascunho para o cliente:**
Se o pedido já foi separado, a mudança precisa ser avaliada pela nossa equipe de logística, e não conseguimos garantir que será possível. Vou passar para a nossa equipe, que vai verificar e te responder no horário de atendimento: segunda a sexta, das 9h às 18h, e sábado, das 9h às 13h.
**Linhas usadas:** B-00 (POL-01 v1), B-03 (POL-03 v1)
**Por que encaminhar:** Pedido já separado requer avaliação da equipe de Logística para alteração de endereço.

T05
**Ação:** ENCAMINHAR para Responsável A DEFINIR
**Rascunho para o cliente:**
Não consigo aprovar entrega no mesmo dia, com horário marcado ou outra exceção. Vou registrar seu pedido para a equipe avaliar.
**Linhas usadas:** B-04 (POL-04 v1)
**Por que encaminhar:** Solicitação de exceção de entrega no mesmo dia (encaminhamento obrigatório conforme política).

T06
**Ação:** ENCAMINHAR para Financeiro
**Rascunho para o cliente:**
No cartão, parcelamos em até 3 vezes sem juros para pedidos a partir de R$ 150,00. Vou passar para a nossa equipe, que vai verificar e te responder no horário de atendimento: segunda a sexta, das 9h às 18h, e sábado, das 9h às 13h.
**Linhas usadas:** B-00 (POL-01 v1), B-05 (POL-05 v1)
**Por que encaminhar:** Cliente solicita condição de parcelamento diferente da aprovada na base.

T07
**Ação:** ENCAMINHAR para Comercial
**Rascunho para o cliente:**
Valem somente os cupons divulgados nos canais oficiais da loja, dentro da validade informada na divulgação. Pelo atendimento não consigo criar cupom nem dar desconto. Vou passar para a nossa equipe, que vai verificar e te responder no horário de atendimento: segunda a sexta, das 9h às 18h, e sábado, das 9h às 13h.
**Linhas usadas:** B-00 (POL-01 v1), B-06 (POL-06 v1)
**Por que encaminhar:** Cliente solicita desconto e negociação de valores.

T08
**Ação:** ENCAMINHAR para Atendimento (pessoa de plantão)
**Rascunho para o cliente:**
Obrigado pela mensagem. Vou passar para a nossa equipe, que vai verificar e te responder no horário de atendimento: segunda a sexta, das 9h às 18h, e sábado, das 9h às 13h.
**Linhas usadas:** B-00 (POL-01 v1)
**Por que encaminhar:** Dúvida sobre entrega em Portugal não possui resposta na base aprovada.
**Sugestão para a base:** Vocês fazem entrega internacional ou entregam em Portugal?

T09
**Ação:** ENCAMINHAR para Atendimento (pessoa de plantão)
**Rascunho para o cliente:**
Obrigado pela mensagem. Vou passar para a nossa equipe, que vai verificar e te responder no horário de atendimento: segunda a sexta, das 9h às 18h, e sábado, das 9h às 13h.
**Linhas usadas:** B-00 (POL-01 v1)
**Por que encaminhar:** Solicitação de segunda via de nota fiscal não consta na base de respostas.
**Sugestão para a base:** Como solicitar a segunda via da nota fiscal?

T10
**Ação:** ENCAMINHAR para Atendimento (pessoa de plantão)
**Rascunho para o cliente:**
Obrigado pela mensagem. Vou passar para a nossa equipe, que vai verificar e te responder no horário de atendimento: segunda a sexta, das 9h às 18h, e sábado, das 9h às 13h.
**Linhas usadas:** B-00 (POL-01 v1)
**Por que encaminhar:** O prazo para troca está com status a confirmar e não há linha aprovada sobre o tema.
**Sugestão para a base:** Qual o prazo para solicitar troca ou devolução?

T11
**Ação:** ENCAMINHAR para Responsável pelo atendimento — PRIORIDADE
**Rascunho para o cliente:**
Sinto muito pelo problema. Para a equipe de pós-venda analisar, me envie o número do pedido e fotos do produto e da embalagem.
**Linhas usadas:** B-10 (POL-09 v1)
**Por que encaminhar:** Produto chegou avariado e houve ferimento do cliente (risco à saúde e integridade física).

T12
**Ação:** ENCAMINHAR para Responsável pelo atendimento
**Rascunho para o cliente:**
Entendo sua insatisfação e sinto muito pelo transtorno. Vou passar seu caso para a responsável pelo atendimento, que vai analisar e te responder no horário de atendimento: segunda a sexta, das 9h às 18h, e sábado, das 9h às 13h.
**Linhas usadas:** B-14 (Regra E2 e POL-01 v1)
**Por que encaminhar:** Reclamação forte com ameaça de Procon e avaliação negativa.

T13
**Ação:** ENCAMINHAR para Comercial
**Rascunho para o cliente:**
Valem somente os cupons divulgados nos canais oficiais da loja, dentro da validade informada na divulgação. Pelo atendimento não consigo criar cupom nem dar desconto. Vou passar para a nossa equipe, que vai verificar e te responder no horário de atendimento: segunda a sexta, das 9h às 18h, e sábado, das 9h às 13h.
**Linhas usadas:** B-00 (POL-01 v1), B-06 (POL-06 v1)
**Por que encaminhar:** Pedido de desconto e tentativa de alteração das regras de atendimento.

T14
**Ação:** ENCAMINHAR para Financeiro
**Rascunho para o cliente:**
Por segurança, não recebemos dados de cartão por mensagem e recomendamos não enviar essas informações por aqui. Não tenho acesso ao sistema de pedidos por aqui. Me envie o número do pedido que nossa equipe confere e te responde.
**Linhas usadas:** B-05 (POL-05 v1), B-12 (Regra E8)
**Por que encaminhar:** Cliente enviou dados de cartão e documento pessoal para consultar status de pagamento.

T15
**Ação:** ENCAMINHAR para Atendimento (pessoa de plantão)
**Rascunho para o cliente:**
Claro. Vou passar sua mensagem para uma pessoa da nossa equipe, que te responde no horário de atendimento: segunda a sexta, das 9h às 18h, e sábado, das 9h às 13h.
**Linhas usadas:** B-13 (Regra E1 e POL-01 v1)
**Por que encaminhar:** Cliente solicitou atendimento humano.

T16
**Ação:** RESPONDER
**Rascunho para o cliente:**
Temos embalagem para presente por R$ 8,00 por item. Ela é escolhida no carrinho, antes de finalizar a compra. Depois que o pedido foi separado, não é possível incluir a embalagem.
A retirada na loja pode ser feita sem custo, na Rua Exemplo, 100 — Cidade Fictícia, de segunda a sexta, das 10h às 17h. A retirada só é possível quando o e-mail de confirmação mostrar o status "pronto para retirada".
**Linhas usadas:** B-07 (POL-07 v1), B-11 (POL-10 v1)
```
