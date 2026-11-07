# Scripts (opcionais)

Você **não precisa** destes scripts para usar a solução: a planilha modelo já está pronta em `modelos/`. Eles servem para quem prefere editar a base em CSV ou quer uma conferência automática antes de entregar a base para a IA.

Testados em 02/11/2026 com Python 3.11.9 e openpyxl 3.1.5, no Windows. Saída guardada em `exemplos/conferencia-base-exemplo.txt`.

## Preparar (uma vez)

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
pip install -r scripts/requirements.txt
```

Crie o `.venv` fora da pasta do repositório se for versionar seus arquivos.

## gerar_planilha.py — CSV para planilha formatada

```bash
python scripts/gerar_planilha.py minha-base.csv minha-base.xlsx
```

Gera abas "Como usar", "Base" (cabeçalho fixo, filtro, lista de status e cor por status) e "Listas". O CSV precisa usar `;` como separador e as 11 colunas do modelo.

## conferir_base.py — conferência antes de usar

```bash
python scripts/conferir_base.py minha-base.xlsx
python scripts/conferir_base.py minha-base.xlsx --csv minha-base.csv
```

Aponta: ID repetido, status inválido, linha aprovada sem resposta ou sem fonte, "A CONFIRMAR" ou [texto de modelo] em linha aprovada, regra de passagem sem destino, palavras que viram promessa ("garanto", "com certeza", "hoje mesmo"...), texto com cara de CPF, telefone ou e-mail e falta da mensagem B-00. Com `--csv`, exporta a aba Base em CSV (UTF-8 com BOM, abre com acentos no Excel).

Não corrige nada sozinho, não envia nada e não acessa a internet. A detecção de dado pessoal é por padrão de texto: pode deixar passar casos e pode marcar números que não são dados pessoais. Não substitui a sua leitura.
