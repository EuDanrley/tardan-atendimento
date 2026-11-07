# Deixar o assistente salvo: Projeto, skill ou conversa

Colar a instrução e a base toda vez funciona, mas cansa. Escolha **um** dos caminhos abaixo e a equipe passa a só colar a mensagem do cliente.

Limites e planos conferidos nas páginas oficiais em **02/11/2026**. Eles mudam; se a tela estiver diferente, vale o que a ferramenta mostra.

> Antes de subir a base: ela não deve ter dados pessoais de clientes. Confira também a configuração de privacidade da ferramenta (uso das conversas para treinar modelos) e a política da sua empresa. A LGPD (Lei 13.709/2018) se aplica a dados pessoais. Isto não é orientação jurídica.

## Caminho 1 — Projeto no ChatGPT (recomendado para quem já usa ChatGPT)

1. No ChatGPT, na barra lateral, crie um **novo projeto** com o nome "Atendimento — rascunhos".
2. Nas configurações do projeto, em **instruções**, cole o texto entre `--- INÍCIO ---` e `--- FIM ---` de `instrucao-pronta.md` (troque nome e tom).
3. Em **arquivos** do projeto, envie a sua base (`.csv` ou `.xlsx`).
4. Abra uma conversa dentro do projeto e mande: "Confira a base". A resposta deve contar as linhas aprovadas.
5. Pronto. Cada atendimento: conversa nova dentro do projeto → cole a mensagem do cliente (sem dados pessoais).

O que a Central de Ajuda da OpenAI informa (artigo "Projects in ChatGPT"; a página bloqueou leitura direta, conferimos pelo conteúdo indexado dela):
- Projetos estão disponíveis no plano gratuito, com até **5 arquivos por projeto** e **3 uploads por dia**. Go e Plus: até 25 arquivos; Edu, Pro, Business e Enterprise: até 40.
- As instruções do projeto valem só dentro dele e se sobrepõem às instruções personalizadas gerais.
- Em Free, Plus e Pro, o conteúdo dos projetos pode ser usado para treinar modelos se a opção "Improve the model for everyone" estiver ligada. Confira em Configurações → Controles de dados.

**Não use "GPT personalizado" para isto.** Segundo a Central de Ajuda da OpenAI (artigo "Custom GPT retirement and migration FAQ", conferido pelo conteúdo indexado), contas pessoais (Free, Go, Plus e Pro) não podem mais criar GPTs novos, e os GPTs personalizados têm aposentadoria prevista para **11/12/2026**, com migração para "plugins".

## Caminho 2 — Projeto no Claude

1. Em claude.ai, abra **Projects** → **New project** → nome "Atendimento — rascunhos".
2. Em **instruções do projeto**, cole a instrução pronta (com nome e tom trocados).
3. Em **conhecimento do projeto** (project knowledge), envie a base.
4. Conversa nova dentro do projeto → "Confira a base" → depois, mensagens dos clientes.

O que a Central de Ajuda da Anthropic informa (support.claude.com, artigo 9519177):
- Projetos estão disponíveis também no plano gratuito, com máximo de **5 projetos**.
- Quando o conhecimento do projeto chega perto do limite de contexto, os planos pagos ativam um modo de busca (RAG) que amplia a capacidade. A página não informa limite de tamanho ou de quantidade de arquivos.
- Privacidade: em Configurações → Privacidade há a opção de permitir o uso das conversas para melhorar os modelos (planos Free, Pro e Max). Chats anônimos (incognito) não são usados para treino (privacy.claude.com, artigo 12109829).

## Caminho 3 — Skill (Claude ou Gemini)

A pasta `claude-skill/atendimento-base-respostas/` serve para os dois.

**Antes de zipar:** coloque a sua base dentro da pasta com o nome `base-respostas.csv` (ou `base-respostas.xlsx`). Sem isso, a skill pede a base na conversa.

**Claude** (support.claude.com, artigos 12512180 e 12512198):
1. Ligue Configurações → Capabilities → "Code execution and file creation" (no layout novo: "Create and edit files"). A skill exige isso.
2. Compacte a **pasta** `atendimento-base-respostas` em ZIP (a pasta tem que estar na raiz do ZIP, não os arquivos soltos).
3. Customize → Skills → "+" → "+ Create skill" → "Upload a skill" → envie o ZIP.
4. Disponível nos planos Free, Pro, Max, Ultra, Team e Enterprise. O nome da pasta precisa ser igual ao `name` da skill (já está).

**Gemini** (support.google.com/gemini, artigo 17094296):
1. Em gemini.google.com → Customize → Skills → Create → Upload.
2. Selecione o `SKILL.md`, a pasta ou o ZIP com o `SKILL.md` na pasta principal → Open → revise → Create.
3. Requisitos informados: 18 anos ou mais, conta conectada, "Keep Activity" ligado. A página diz que skills funcionam sem assinatura Google AI. Total de arquivos até 100 MB.
4. Arquivos de referência só entram enviados junto com a skill; para atualizar a base, envie a skill inteira de novo.
5. A página lista tipos não aceitos (Office antigo .doc/.xls/.ppt, áudio, vídeo, arquivos compactados dentro da skill, alguns formatos de código). `.csv` e `.xlsx` não aparecem na lista de bloqueados; aceitação desses formatos **não confirmada** em teste.

**Não use Gem para isto.** Segundo a Ajuda do Gemini (artigo 18560919), em contas pessoais os Gems ficam somente leitura em **17/11/2026** e são removidos em **17/12/2026**, substituídos por skills.

## Caminho 4 — Sem salvar nada

Conversa nova → cole a instrução + a base → use. Serve para testar ou para quem atende pouco.

## Depois de configurar, em qualquer caminho

1. Rode o roteiro de testes (`modelos/roteiro-de-testes.md`) **na ferramenta escolhida**.
2. Combine com a equipe: a IA prepara o rascunho, a pessoa lê, ajusta se precisar e envia.
3. Mudou uma regra? Atualize a base, troque o arquivo no Projeto ou na skill e teste de novo.
