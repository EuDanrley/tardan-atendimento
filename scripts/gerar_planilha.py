"""Gera a planilha .xlsx da base de respostas a partir de um .csv.

Uso:
    python scripts/gerar_planilha.py ENTRADA.csv SAIDA.xlsx

O .csv usa ponto e vírgula (;) como separador e UTF-8 (com ou sem BOM).
Colunas esperadas: id;tema;pergunta;outras_formas;resposta_aprovada;fonte;
passar_para_humano_quando;encaminhar_para;status;aprovado_por;revisado_em

Não envia nada, não acessa a internet e não altera o .csv de entrada.
Requer: openpyxl (veja scripts/requirements.txt).
"""
import csv
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

COLUNAS = [
    "id", "tema", "pergunta", "outras_formas", "resposta_aprovada", "fonte",
    "passar_para_humano_quando", "encaminhar_para", "status", "aprovado_por",
    "revisado_em",
]
TITULOS = {
    "id": "ID",
    "tema": "Tema",
    "pergunta": "Pergunta do cliente",
    "outras_formas": "Outras formas de perguntar",
    "resposta_aprovada": "Resposta aprovada",
    "fonte": "Fonte (documento, item, versão)",
    "passar_para_humano_quando": "Passar para pessoa quando",
    "encaminhar_para": "Encaminhar para",
    "status": "Status",
    "aprovado_por": "Aprovado por",
    "revisado_em": "Revisado em",
}
LARGURAS = {
    "id": 8, "tema": 16, "pergunta": 34, "outras_formas": 34,
    "resposta_aprovada": 60, "fonte": 22, "passar_para_humano_quando": 40,
    "encaminhar_para": 24, "status": 14, "aprovado_por": 18, "revisado_em": 13,
}
STATUS_VALIDOS = ["aprovada", "rascunho", "A CONFIRMAR"]

COMO_USAR = [
    "BASE DE RESPOSTAS DE ATENDIMENTO — Comunidade Tardan",
    "",
    "1. Cada linha da aba Base é uma dúvida de cliente com a resposta que a empresa aprovou.",
    "2. Só a IA usa linhas com Status = aprovada. Rascunho e A CONFIRMAR são ignorados.",
    "3. Toda resposta aprovada precisa de Fonte: o documento e o item da regra, com versão.",
    "4. 'Passar para pessoa quando' diz em que situações a IA não responde e encaminha.",
    "5. Não escreva na base dados de clientes (nome, telefone, CPF, endereço, número de pedido real).",
    "6. Mudou uma regra? Atualize a linha, a versão da fonte e a data em 'Revisado em'.",
    "7. Para usar com a IA: anexe este arquivo (ou o .csv) ao Projeto, ou cole o conteúdo na conversa.",
    "",
    "Confira a base antes de usar: python scripts/conferir_base.py ARQUIVO",
]


def ler_csv(caminho: Path) -> list[dict]:
    with caminho.open(encoding="utf-8-sig", newline="") as f:
        leitor = csv.DictReader(f, delimiter=";")
        faltando = [c for c in COLUNAS if c not in (leitor.fieldnames or [])]
        if faltando:
            raise SystemExit(f"ERRO: colunas ausentes no CSV: {', '.join(faltando)}")
        return [{c: (linha.get(c) or "").strip() for c in COLUNAS} for linha in leitor]


def gerar(linhas: list[dict], saida: Path) -> None:
    wb = Workbook()

    guia = wb.active
    guia.title = "Como usar"
    for i, texto in enumerate(COMO_USAR, start=1):
        celula = guia.cell(row=i, column=1, value=texto)
        if i == 1:
            celula.font = Font(bold=True, size=13)
    guia.column_dimensions["A"].width = 110

    base = wb.create_sheet("Base")
    cabecalho_fill = PatternFill("solid", fgColor="1F3A5F")
    for col, nome in enumerate(COLUNAS, start=1):
        c = base.cell(row=1, column=col, value=TITULOS[nome])
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = cabecalho_fill
        c.alignment = Alignment(wrap_text=True, vertical="center")
        letra = c.column_letter
        base.column_dimensions[letra].width = LARGURAS[nome]

    for r, linha in enumerate(linhas, start=2):
        for col, nome in enumerate(COLUNAS, start=1):
            c = base.cell(row=r, column=col, value=linha[nome])
            c.alignment = Alignment(wrap_text=True, vertical="top")

    ultima = max(len(linhas) + 1, 2)
    limite_validacao = ultima + 200  # espaço para novas linhas
    base.freeze_panes = "C2"
    base.auto_filter.ref = f"A1:K{ultima}"

    listas = wb.create_sheet("Listas")
    listas["A1"] = "Status válidos"
    listas["A1"].font = Font(bold=True)
    for i, s in enumerate(STATUS_VALIDOS, start=2):
        listas.cell(row=i, column=1, value=s)
    listas.column_dimensions["A"].width = 20

    col_status = COLUNAS.index("status") + 1
    letra_status = base.cell(row=1, column=col_status).column_letter
    dv = DataValidation(
        type="list",
        formula1=f"=Listas!$A$2:$A${len(STATUS_VALIDOS) + 1}",
        allow_blank=True,
        showErrorMessage=True,
        errorTitle="Status inválido",
        error="Use: aprovada, rascunho ou A CONFIRMAR.",
    )
    base.add_data_validation(dv)
    dv.add(f"{letra_status}2:{letra_status}{limite_validacao}")

    faixa = f"A2:K{limite_validacao}"
    cores = {
        "aprovada": "E2F0D9",
        "rascunho": "FFF2CC",
        "A CONFIRMAR": "F8CBAD",
    }
    for status, cor in cores.items():
        base.conditional_formatting.add(
            faixa,
            FormulaRule(
                formula=[f'${letra_status}2="{status}"'],
                fill=PatternFill("solid", fgColor=cor),
            ),
        )

    wb.active = 1  # abre na aba Base
    saida.parent.mkdir(parents=True, exist_ok=True)
    wb.save(saida)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    entrada, saida = Path(sys.argv[1]), Path(sys.argv[2])
    if not entrada.exists():
        print(f"ERRO: arquivo não encontrado: {entrada}")
        return 1
    linhas = ler_csv(entrada)
    gerar(linhas, saida)
    print(f"OK: {len(linhas)} linhas de {entrada.name} -> {saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
