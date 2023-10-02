import re
import subprocess
import bradesco_pdf

import pdfplumber

pdf_file = '/Users/ramaro/Desktop/pessoal_fatura/Bradesco_out.pdf'
string_alvo = 'Banco Itaú'
fatura_itau = False
fatura_bradesco = False
texto = ''
lista = []
lista2 = []

with pdfplumber.open(pdf_file) as pdf:
    data = ''
    for i in range(len(pdf.pages)):
        page = pdf.pages[i]
        data += page.extract_text()
    if data and string_alvo in data:
        fatura_itau = True
    else:
        fatura_bradesco = True

# initial_data_pattern = re.compile(r'\d{2}/\d{2}(.*?\d+,\d{2})$') //possivel remoção
handled_data_pattern = re.compile(r'(\d{2}/\d{2})\s+(.*?)\s+(\d+,\d{2})')
result_list = []
result_list2 = []

if fatura_itau:
    for line in data.split('\n'):
        if handled_data_pattern.match(line):
            pattern = re.search(r'\d,\d{2}', line)
            if pattern:
                final_position = pattern.end()
                result = line[:final_position]
                result_list.append(result)
            else:
                print('Pattern no matches')

    for line in result_list:
        text = line
        result = re.match(handled_data_pattern, text)
        if result:
            # print(result.group(3))
            date = result.group(1)
            desc = result.group(2)
            value = result.group(3)

            result_list2.append([date, desc, value])

    for line in result_list2:
        print(line)

if fatura_bradesco:
    subprocess.run(['python3', 'bradesco_pdf.py', pdf_file])
    # data = ''
    # pdf = PdfReader(pdf_file)
    #
    # for i in range(len(pdf.pages)):
    #     page = pdf.pages[i]
    #     data += page.extract_text()
    # # print(data)
    #
    # for p in palavras_chave:
    #     texto = bradesco_pdf.mover_linha_para_cima(data, p)
    #
    # bradesco_pdf.adiciona_a_lista(texto)
    # print(texto)
    # bradesco_pdf.trata_lista(bradesco_pdf.lista)
    # bradesco_pdf.adiciona_data(bradesco_pdf.lista_tratada)
    # # bradesco_pdf.lista_tratada = bradesco_pdf.remover_linhas(bradesco_pdf.lista_tratada)
    #
    # for l in bradesco_pdf.lista_tratada:
    #     print(l)
