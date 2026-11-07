# Checklist — antes de usar o assistente com clientes

## A base

- [ ] Cada linha `aprovada` foi lida por quem responde pela regra (não só pela IA).
- [ ] Toda linha aprovada tem **fonte**: documento, item e versão ou data.
- [ ] Nenhuma resposta aprovada promete o que a regra não garante (data de entrega, desconto, aprovação de troca, reembolso).
- [ ] Lacunas e conflitos ficaram `A CONFIRMAR`, não "resolvidos" no chute.
- [ ] Existe a linha **B-00** aprovada: mensagem de encaminhamento + destino padrão.
- [ ] Cada linha diz quando vai para uma pessoa e **para quem** (sem destino = Responsável A DEFINIR = decidir antes de usar).
- [ ] Regra em revisão, mas com destino conhecido? Aprove uma linha só de encaminhamento (ex.: "O prazo de troca é confirmado pela equipe de pós-venda. Me envie o número do pedido que eu passo para eles.").
- [ ] A base não tem nome, telefone, CPF, e-mail, endereço ou número de pedido de cliente.
- [ ] Opcional: `python scripts/conferir_base.py sua-base.xlsx` terminou com 0 erros.

## O assistente

- [ ] A primeira resposta contou o número certo de linhas aprovadas e achou a B-00.
- [ ] O roteiro de testes foi escrito **antes** de testar e rodado na ferramenta que você vai usar.
- [ ] Nenhum teste mostrou informação fora da base. (Se mostrou: ajuste a base ou a instrução e repita.)
- [ ] Pergunta fora da base, desconto, exceção, Procon, machucado e "quero falar com uma pessoa" foram encaminhados.
- [ ] Mensagem com CPF ou cartão: o rascunho não repetiu os dados.

## A rotina da equipe

- [ ] Todos sabem: a IA prepara, a pessoa confere e envia.
- [ ] Mensagens de clientes são coladas **sem dados pessoais**.
- [ ] A configuração de privacidade da ferramenta foi conferida (uso das conversas para treinar modelos).
- [ ] Há um dono da base, que atualiza quando uma regra muda e registra a data em "Revisado em".
- [ ] As "Sugestões para a base" que a IA devolve são revisadas de tempos em tempos e viram linhas novas quando aprovadas.
