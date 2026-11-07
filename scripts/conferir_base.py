"""Confere a base de respostas antes de entregar para a IA.

Uso:
    python scripts/conferir_base.py BASE.csv|BASE.xlsx [--csv SAIDA.csv]

O que confere (não corrige nada sozinho):
- IDs repetidos e status fora da lista (aprovada, rascunho, A CONFIRMAR);
- linha aprovada sem resposta, sem fonte, com "A CONFIRMAR" ou com [colchetes] de modelo;
- linha aprovada com regra de passagem para pessoa, mas sem destino;
- palavras que costumam virar promessa ("garanto", "com certeza", "hoje mesmo"...);
- texto com cara de dado pessoal (CPF, telefone, e-mail);
- ausência da mensagem padrão de encaminhamento (B-00) aprovada.

--csv SAIDA.csv exporta a aba Base (ou o próprio CSV) em CSV com ";" e UTF-8 com BOM,
que abre com acentos no Excel e pode ser anexado à IA.

Código de saída: 0 sem erros, 1 com erros (avisos não contam como erro).
Não envia nada e não acessa a internet. Requer openpyxl para ler .xlsx.
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

COLUNAS = [
    "id", "tema", "pergunta", "outras_formas", "resposta_aprovada", "fonte",
    "passar_para_humano_quando", "encaminhar_para", "status", "aprovado_por",
    "revisado_em",
]
TITULOS = {
    "ID": "id", "Tema": "tema", "Pergunta do cliente": "pergunta",
    "Outras formas de perguntar": "outras_formas",
    "Resposta aprovada": "resposta_aprovada",
    "Fonte (documento, item, versão)": "fonte",
    "Passar para pessoa quando": "passar_para_humano_quando",
    "Encaminhar para": "encaminhar_para", "Status": "status",
    "Aprovado por": "aprovado_por", "Revisado em": "revisado_em",
}
STATUS_VALIDOS = {"aprovada", "rascunho", "A CONFIRMAR"}
VAZIOS = {"", "-", "—"}
PALAVRAS_PROMESSA = [
    "garanto", "garantimos", "com certeza", "sem falta", "prometo",
    "prometemos", "hoje mesmo", "100%",
]
PADROES_DADO_PESSOAL = {
    "CPF": re.compile(r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b"),
    "telefone": re.compile(r"\(?\b\d{2}\)?\s?9?\d{4}-?\d{4}\b"),
    "e-mail": re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"),
}


def ler(caminho: Path) -> list[dict]:
    if caminho.suffix.lower() == ".xlsx":
        from openpyxl import load_workbook

        wb = load_workbook(caminho, read_only=True, data_only=True)
        if "Base" not in wb.sheetnames:
            raise SystemExit("ERRO: a planilha não tem a aba 'Base'.")
        linhas = list(wb["Base"].iter_rows(values_only=True))
        if not linhas:
            return []
        cab = [TITULOS.get(str(c).strip(), str(c).strip()) if c else "" for c in linhas[0]]
        dados = []
        for valores in linhas[1:]:
            if all(v in (None, "") for v in valores):
                continue
            item = {cab[i]: ("" if v is None else str(v).strip()) for i, v in enumerate(valores) if i < len(cab)}
            dados.append({c: item.get(c, "") for c in COLUNAS})
        return dados
    with caminho.open(encoding="utf-8-sig", newline="") as f:
        leitor = csv.DictReader(f, delimiter=";")
        faltando = [c for c in COLUNAS if c not in (leitor.fieldnames or [])]
        if faltando:
            raise SystemExit(f"ERRO: colunas ausentes: {', '.join(faltando)}")
        return [{c: (l.get(c) or "").strip() for c in COLUNAS} for l in leitor]


def conferir(linhas: list[dict]) -> tuple[list[str], list[str]]:
    erros, avisos = [], []
    ids = Counter(l["id"] for l in linhas)
    for i, n in ids.items():
        if n > 1:
            erros.append(f"ID repetido: {i} aparece {n} vezes")

    for l in linhas:
        i = l["id"] or "(sem id)"
        st = l["status"]
        if st not in STATUS_VALIDOS:
            erros.append(f"{i}: status '{st}' inválido (use aprovada, rascunho ou A CONFIRMAR)")
        texto_todo = " ".join(l.values())
        for nome, padrao in PADROES_DADO_PESSOAL.items():
            if padrao.search(texto_todo):
                erros.append(f"{i}: possível dado pessoal ({nome}). Retire antes de usar com IA.")
        if st != "aprovada":
            continue
        resp = l["resposta_aprovada"]
        if resp in VAZIOS:
            erros.append(f"{i}: aprovada, mas sem resposta")
        if "A CONFIRMAR" in resp.upper():
            erros.append(f"{i}: aprovada, mas a resposta contém A CONFIRMAR")
        if "[" in resp and "]" in resp:
            erros.append(f"{i}: aprovada, mas a resposta ainda tem [texto de modelo]")
        if l["fonte"] in VAZIOS:
            erros.append(f"{i}: aprovada, mas sem fonte")
        if l["passar_para_humano_quando"] not in VAZIOS and l["encaminhar_para"] in VAZIOS:
            avisos.append(f"{i}: tem regra de passagem para pessoa, mas não diz para quem")
        if "A DEFINIR" in l["encaminhar_para"].upper():
            avisos.append(f"{i}: destino do encaminhamento ainda A DEFINIR")
        if l["aprovado_por"] in VAZIOS:
            avisos.append(f"{i}: aprovada, mas sem 'aprovado por'")
        baixo = resp.lower()
        for p in PALAVRAS_PROMESSA:
            if p in baixo:
                avisos.append(f"{i}: contém '{p}'. Confira se não é promessa sem regra.")

    if not any(l["id"] == "B-00" and l["status"] == "aprovada" for l in linhas):
        avisos.append("Sem B-00 aprovada (mensagem padrão de encaminhamento). A IA vai improvisar a mensagem.")
    return erros, avisos


def exportar_csv(linhas: list[dict], destino: Path) -> None:
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUNAS, delimiter=";")
        w.writeheader()
        w.writerows(linhas)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if not args or args[0] in {"-h", "--help"}:
        print(__doc__)
        return 2
    origem = Path(args[0])
    if not origem.exists():
        print(f"ERRO: arquivo não encontrado: {origem}")
        return 1
    linhas = ler(origem)
    erros, avisos = conferir(linhas)
    por_status = Counter(l["status"] for l in linhas)

    print(f"Base: {origem.name}")
    print(f"Linhas: {len(linhas)}")
    for st in ["aprovada", "rascunho", "A CONFIRMAR"]:
        print(f"  {st}: {por_status.get(st, 0)}")
    outros = sum(n for st, n in por_status.items() if st not in STATUS_VALIDOS)
    if outros:
        print(f"  status inválido: {outros}")
    print(f"Erros: {len(erros)}")
    for e in erros:
        print(f"  [ERRO] {e}")
    print(f"Avisos: {len(avisos)}")
    for a in avisos:
        print(f"  [AVISO] {a}")
    print("A IA só deve usar as linhas 'aprovada'." if not erros else "Corrija os erros antes de entregar a base para a IA.")

    if "--csv" in args:
        pos = args.index("--csv")
        if pos + 1 >= len(args):
            print("ERRO: informe o arquivo depois de --csv")
            return 1
        destino = Path(args[pos + 1])
        exportar_csv(linhas, destino)
        print(f"CSV exportado: {destino}")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
