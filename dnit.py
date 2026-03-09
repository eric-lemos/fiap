import unicodedata
from datetime import datetime
import json
import requests

url = "https://www1.dnit.gov.br/editais/consulta/lista.asp"

resp = requests.get(url, timeout=20)
resp.raise_for_status()

dados = resp.json()
editais = dados.get("aaData", [])

# Aceita singular/plural em "projeto(s) basico(s)" e ignora acentos/caixa.
# triggers = [
#     "projeto basico",
#     "projeto basicos",
#     "projetos basico",
#     "projetos basicos",
# ]
# total_editais = 0
# ano_minimo = datetime.now().year - 2


# def normalizar_texto(texto: str) -> str:
#     texto = (texto or "").lower()
#     return "".join(
#         c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn"
#     )


# def extrair_data_abertura(data_abertura: str) -> datetime | None:
#     try:
#         return datetime.strptime(data_abertura, "%d/%m/%Y")
#     except (TypeError, ValueError):
#         return None

# for edital in editais:
#     objeto_normalizado = normalizar_texto(edital.get("objeto", ""))
#     data_abertura = extrair_data_abertura(edital.get("data_abertura"))

#     if (
#         any(trigger in objeto_normalizado for trigger in triggers)
#         and data_abertura is not None
#         and data_abertura.year >= ano_minimo
#     ):
#         # print(f"Encontrado edital com o objeto desejado: {edital['numero']}, id = {edital['detalhes']}")
#         total_editais += 1

# print("Filtro aplicado: projeto(s) basico(s), ignorando acentos")
# print(f"Filtro de data: ano de abertura >= {ano_minimo}")
# print(f"Total de editais encontrados: {total_editais}")

# print(editais[:1][0]['detalhes'])

# url2 = f"https://www1.dnit.gov.br/editais/consulta/resumo.asp?NUMIDEdital={str(editais[:1][0]['detalhes'])}"

# resp2 = requests.get(url2, timeout=20)
# resp2.raise_for_status()

# dados2 = resp2.json()

print(json.dumps(dados, indent=2, ensure_ascii=False))

# https://www1.dnit.gov.br/editais/consulta/resumo.asp?NUMIDEdital=10959
# print("Total:", len(editais))
# print("editais[:1])
# print(json.dumps(editais[:1], indent=2, ensure_ascii=False))

