# Atendimento com base de respostas

Uma **base de respostas aprovadas** (planilha) e um **assistente de IA** que prepara o rascunho de resposta ao cliente usando só essa base, diz de onde tirou e passa para uma pessoa o que não está nela.

## Use em 5 minutos

1. **Baixe:** botão verde **Code → Download ZIP** e descompacte a pasta.
2. Abra `modelos/base-respostas-modelo.xlsx` e preencha suas perguntas e respostas (ou use `instrucoes/montar-base.md` para a IA montar o rascunho da base a partir das suas regras). Marque como `aprovada` só o que você conferiu.
3. Abra `instrucoes/instrucao-pronta.md`, copie o texto entre `--- INÍCIO ---` e `--- FIM ---`, cole no ChatGPT, no Claude ou no Gemini e anexe (ou cole) a sua base.
4. Cole a mensagem do cliente, **sem nome, telefone, CPF ou endereço**. Você recebe: responder ou encaminhar, o rascunho pronto e a linha da base usada.
5. Antes de usar com clientes, rode as perguntas difíceis de `modelos/roteiro-de-testes.md` e passe pelo `CHECKLIST.md`.

Quer ver funcionando antes? Use `exemplos/base-respostas-exemplo.xlsx` (empresa fictícia) com a instrução pronta e as mensagens de `exemplos/roteiro-de-testes-ficticio.md`.

## O que você precisa

- Conta no ChatGPT, no Claude ou no Gemini. O plano gratuito serve para a instrução pronta; para deixar salvo, veja `instrucoes/projeto-ia.md` (limites conferidos em 02/11/2026: Projetos do ChatGPT no plano gratuito aceitam até 5 arquivos; Projetos do Claude no gratuito, até 5 projetos).
- Excel, LibreOffice ou Google Planilhas para editar a base.
- Suas regras de atendimento e as dúvidas que se repetem (modelo: `modelos/coleta-de-duvidas.md`).
- Opcional: Python 3.11 para os scripts de conferência (`scripts/LEIA-ME.md`).

Nenhuma integração com WhatsApp, Instagram ou site está incluída. A IA prepara o rascunho; uma pessoa confere e envia.

## Arquivos do repositório

| Arquivo | Para que serve |
|---|---|
| `instrucoes/instrucao-pronta.md` | Assistente de atendimento: colar na IA junto com a base. |
| `instrucoes/montar-base.md` | Instrução para a IA transformar suas regras e dúvidas no rascunho da base. |
| `instrucoes/projeto-ia.md` | Como deixar salvo em Projeto (ChatGPT/Claude) ou skill (Claude/Gemini). |
| `instrucoes/claude-skill/atendimento-base-respostas/SKILL.md` | A mesma instrução em formato de skill (serve no Claude e no Gemini). |
| `modelos/base-respostas-modelo.xlsx` e `.csv` | Base em branco: pergunta, resposta aprovada, fonte, quando passar para pessoa, para quem, status. |
| `modelos/coleta-de-duvidas.md` | Roteiro para juntar dúvidas, regras e responsáveis antes de montar a base. |
| `modelos/roteiro-de-testes.md` | Perguntas difíceis para testar antes de usar. |
| `exemplos/entrada-ficticia-politicas.md` e `entrada-ficticia-perguntas.md` | Regras e dúvidas de uma empresa fictícia. |
| `exemplos/base-respostas-exemplo.xlsx` e `.csv` | A base dessa empresa fictícia, revisada. |
| `exemplos/saida-esperada.md` | Como o assistente deve responder. |
| `exemplos/roteiro-de-testes-ficticio.md` | 16 mensagens difíceis com o resultado esperado. |
| `exemplos/teste-api-gemini-2026-11-02.md` e `teste-montar-base-api-gemini-2026-11-02.md` | Registros dos testes feitos pela equipe. |
| `exemplos/conferencia-base-exemplo.txt` | Saída dos scripts de conferência. |
| `scripts/` | Opcional: gerar a planilha a partir de CSV e conferir a base. |
| `CHECKLIST.md` | Conferência antes de usar. |

## Quer entender ou adaptar?

As aulas do módulo 04 do Pro mostram o assistente funcionando (aula 1), como adaptar a base ao seu negócio e tratar casos difíceis (aula 2) e como funciona por dentro, privacidade e o caminho para levar ao WhatsApp (aula 3). Você não precisa assistir para usar.

## Limites

- O assistente só é tão bom quanto a base. Regra que não está na base vira encaminhamento, e isso é o comportamento certo.
- Ele prepara rascunhos. Não envia mensagens, não consulta pedidos, pagamentos ou estoque e não se conecta ao WhatsApp. Levar para o WhatsApp exige integração (módulo 10, com n8n) ou o serviço adicional "Quero que façam para mim", combinado pelo WhatsApp da Comunidade, com escopo e proposta próprios.
- Testamos a instrução via API do Gemini com dados fictícios (registros em `exemplos/`). Não testamos nas telas do ChatGPT, do Claude ou do Gemini: rode o roteiro de testes na ferramenta que você usar.
- Não cole dados pessoais de clientes. O tratamento de dados pessoais está sujeito à LGPD (Lei 13.709/2018). Confira a política da sua empresa e a configuração de privacidade da ferramenta. Isto não é orientação jurídica.

## Licença

Veja `LICENCA.md`. Material da Comunidade Tardan para uso de membros ativos em seus próprios negócios.
