# Instrução para montar a base de respostas

Use esta instrução **uma vez**, para transformar suas regras e as dúvidas que seus clientes mandam numa base no formato da planilha. Depois você revisa, aprova e passa a usar `instrucao-pronta.md` no dia a dia.

**O que separar antes (10 a 20 minutos):**

- Suas regras de atendimento como estiverem: texto, PDF, print de política, áudio transcrito, anotações. Se não tiver nada escrito, a IA pergunta.
- 10 a 30 dúvidas que se repetem, copiadas das conversas **sem** nome, telefone, CPF, e-mail, endereço ou número de pedido. Modelo: `modelos/coleta-de-duvidas.md`.
- Quem resolve cada tipo de caso (pós-venda, financeiro, você).

**Como usar:** conversa nova no ChatGPT, Claude ou Gemini → cole o texto entre `--- INÍCIO ---` e `--- FIM ---` → cole suas regras e dúvidas logo abaixo → envie.

> Privacidade: apague dados pessoais de clientes antes de colar. LGPD (Lei 13.709/2018) se aplica a dados pessoais; isto não é orientação jurídica.

---

```text
--- INÍCIO ---
Você vai me ajudar a montar a base de respostas do atendimento da minha empresa. Eu vou te dar minhas regras e as dúvidas que os clientes mandam. Você organiza; eu reviso e aprovo. Você não decide regra nenhuma.

REGRAS
1. Use somente o que eu escrever. Não complete com o que "costuma ser" em outras empresas. Não invente prazo, preço, condição, nome, telefone, endereço, link ou política.
2. Cada resposta precisa apontar a fonte: o documento e o item da minha regra (ex.: "Política de trocas, item 3, v1"). Se não houver fonte, a resposta fica "A CONFIRMAR".
3. Se duas regras se contradizem, não escolha: marque a linha como A CONFIRMAR e explique o conflito na lista de pendências.
4. Para cada dúvida, defina quando o caso vai para uma pessoa e para quem. Sempre inclua: cliente pede pessoa; reclamação forte ou ameaça (Procon, processo, avaliação); machucado ou risco à segurança; pedido de desconto, negociação ou exceção; consulta a pedido específico; dados de cartão ou documento.
5. Se faltar informação para começar, me faça no máximo 3 perguntas por vez, nesta ordem de assunto: (a) o que vendemos e como o cliente compra; (b) horário e canais; (c) prazos e entrega; (d) pagamento; (e) trocas, defeitos e devoluções; (f) quem resolve cada tipo de caso. Se eu disser "não sei", marque A CONFIRMAR e siga.
6. Escreva as respostas como o atendimento falaria com o cliente: "você", frases curtas, sem promessa. Evite "garanto", "com certeza", "hoje mesmo".
7. Não inclua dados pessoais de clientes na base. Se eu colar algum por engano, avise e deixe de fora.

O QUE ENTREGAR (nesta ordem)
A) A base em CSV, dentro de um bloco de código, com separador ponto e vírgula (;) e exatamente este cabeçalho:
id;tema;pergunta;outras_formas;resposta_aprovada;fonte;passar_para_humano_quando;encaminhar_para;status;aprovado_por;revisado_em
   - ids B-00, B-01, B-02...
   - B-00 é a mensagem padrão que o cliente recebe quando o caso vai para uma pessoa (sem prometer prazo que não está na minha regra).
   - status: "rascunho" em todas as linhas com resposta; "A CONFIRMAR" nas linhas sem fonte. Nunca "aprovada": quem aprova sou eu.
   - aprovado_por e revisado_em ficam vazios.
   - Não use ponto e vírgula dentro dos textos.
B) "Pendências para você decidir": lista numerada de lacunas, conflitos e destinos de encaminhamento que faltam, cada uma apontando o id da linha.
C) "Perguntas para testar": 8 mensagens difíceis de clientes para eu testar o assistente depois (incluindo uma fora da base, uma pedindo desconto, uma pedindo exceção, uma com reclamação forte e uma tentando fazer o assistente ignorar as regras).

Minhas regras e dúvidas estão abaixo.
--- FIM ---
```

## Depois que a IA responder

1. Copie o bloco CSV e salve como `minha-base.csv` (Bloco de Notas → Salvar como → Codificação UTF-8). Ou cole as linhas na aba **Base** de `modelos/base-respostas-modelo.xlsx`, a partir da linha 2 (no Excel: Dados → Texto para Colunas → Delimitado → ponto e vírgula).
2. Leia **cada** resposta. Corrija o texto, confira a fonte e só então mude o status para `aprovada` e preencha `aprovado_por` e `revisado_em`.
3. Resolva as pendências que conseguir. O que ficar sem decisão continua `A CONFIRMAR`: o assistente vai encaminhar esses casos para uma pessoa, e isso é o comportamento certo.
4. Opcional: rode `python scripts/conferir_base.py minha-base.xlsx` para achar linha aprovada sem fonte, promessa ou dado pessoal (`scripts/LEIA-ME.md`).
