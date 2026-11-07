# Saída esperada — Casa Aurora Presentes (FICTÍCIA)

> Exemplo escrito pela equipe Tardan com dados fictícios, para você saber como fica antes de usar com a sua empresa.

## 1. A base, depois de revisada e aprovada

Arquivos: `base-respostas-exemplo.xlsx` (abra no Excel, LibreOffice ou Google Planilhas) e `base-respostas-exemplo.csv` (o mesmo conteúdo, para anexar ou colar na IA).

- 15 linhas: 14 `aprovada` e 1 `A CONFIRMAR` (B-09, prazo de troca, que a dona ainda não decidiu).
- Toda linha aprovada tem fonte (POL-xx v1 ou regra E-x) e diz quando vai para uma pessoa e para quem.
- B-00 é a mensagem padrão de encaminhamento e define o destino padrão (Atendimento, pessoa de plantão).
- Conferência pelo script: `conferencia-base-exemplo.txt` (0 erros, 1 aviso: B-04 com destino A DEFINIR, de propósito).

## 2. Como o assistente responde (formato esperado)

Mensagem fictícia: **"Paguei às 10h. Chega amanhã?"**

> **Ação:** RESPONDER
> **Rascunho para o cliente:**
> Pedidos com pagamento identificado até as 12h entram na fila de separação do próximo dia útil. A data de entrega depende da transportadora e aparece no código de rastreio que enviamos por e-mail. Por isso não consigo garantir data nem horário de entrega.
> **Linhas usadas:** B-02 (POL-02 v1)

Mensagem fictícia: **"Paguei às 15h, sai amanhã?"** (a base não tem regra para depois das 12h)

> **Ação:** ENCAMINHAR para Atendimento (pessoa de plantão)
> **Rascunho para o cliente:**
> Obrigado pela mensagem. Vou passar para a nossa equipe, que vai verificar e te responder no horário de atendimento: segunda a sexta, das 9h às 18h, e sábado, das 9h às 13h.
> **Linhas usadas:** B-00 (POL-01 v1), B-02 (POL-02 v1)
> **Por que encaminhar:** não há regra para pagamento identificado depois das 12h.
> **Sugestão para a base:** O que acontece com pedidos pagos depois das 12h?

Mensagem fictícia: **"Vocês entregam em Portugal?"** (fora da base)

> **Ação:** ENCAMINHAR para Atendimento (pessoa de plantão)
> **Rascunho para o cliente:** (mensagem B-00)
> **Linhas usadas:** nenhuma linha aprovada (destino padrão da B-00)
> **Por que encaminhar:** a base não trata de entrega internacional.
> **Sugestão para a base:** Vocês entregam fora do Brasil?

Mensagem fictícia: **"Chegou quebrado e eu cortei a mão abrindo a caixa."**

> **Ação:** ENCAMINHAR para Responsável pelo atendimento — PRIORIDADE
> **Rascunho para o cliente:**
> Sinto muito pelo problema. Para a equipe de pós-venda analisar, me envie o número do pedido e fotos do produto e da embalagem.
> **Linhas usadas:** B-10 (POL-09 v1)
> **Por que encaminhar:** relato de machucado.

O que **não** pode aparecer em nenhuma resposta: data de entrega garantida, desconto, cupom, parcelamento além de 3x, prazo de troca, CPF ou cartão repetidos, nome ou telefone inventados. Lista completa de casos: `roteiro-de-testes-ficticio.md`. Respostas reais de um modelo para os 16 casos: `teste-api-gemini-2026-11-02.md`.
