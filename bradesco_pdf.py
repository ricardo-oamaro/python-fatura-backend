import re
import subprocess
import time

from PyPDF2 import PdfReader

import itau_pdf

pdf = PdfReader(itau_pdf.pdf_file)
page = pdf.pages[0]

text = ''

text_adjustment_pattern = r'(?<=,\d{2})'

for i in range(len(pdf.pages)):
    page = pdf.pages[i]
    text += page.extract_text()

keywords = ["MAR", "JUL", "AGO", "SET"]
months = ["03", "07", "08", "09"]
pattern = r'(\d{2}/\w{3})(.*?)\((.*?)\)'

list = []
handled_list = []
remove_items = ["Totaldafatura", "Saldoanterior", "SALDOANTERIOR",
                "Pagamentos/Créditos", "Despesaslocais", "Despesasnoexterior", "Pagamentomínimo",
                "PAGBOLETOBANCARIO"]


def handle_data(data):
    result = re.split(text_adjustment_pattern, data)
    result_list = '\n'.join(result)

    return result_list


def remove_lines(texto):
    lines = [item for item in texto if item[0] != '' and len(item) == 3]
    lines = [item for item in lines if not any(termo in item[1] for termo in remove_items)]
    return lines


def lines_up(data, keyword):
    lines = data.split('\n')
    i = 1
    while i < len(lines):
        if lines[i].startswith(keyword):
            lines[i - 1] += "/" + lines[i]
            lines.pop(i)  # Remove a linha juntada
        else:
            i += 1
    new_text = '\n'.join(lines)
    return new_text


def add_to_list(data):
    lines = data.split('\n')
    i = 0
    while i < len(lines):
        list.append(lines[i].strip())
        i += 1


def handle_list(lista):
    for l in lista:
        lista_separada = l.split('\xa0')
        sublista = [el.replace(' ', '') for el in lista_separada if el.strip()]
        handled_list.append(sublista)


def insert_date(handled_list):
    data = ''
    for i, list in enumerate(handled_list):
        if len(list) < 3:
            list.insert(0, data)
            i += 1
        else:
            data = handled_list[i][0]
            i += 1


# print(texto)
for p in keywords:
    text = lines_up(text, p)

result_list = handle_data(text)
# print(result_list)
add_to_list(result_list)
# print(lista)
handle_list(list)
insert_date(handled_list)
# for l in lista_tratada:
#     print(l)

handled_list = remove_lines(handled_list)

