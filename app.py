import sys

import gspread

from bradesco_pdf import handled_list
from sms import result_list, sms_receiver, owner_sheet, card_sheet
import itau_pdf

sh_updated = False
# connect to the service account
gc = gspread.service_account(filename="cred.json")
spreadsheet = ''
sheet = ''

if owner_sheet == 'Ricardo' or itau_pdf.owner_sheet == 'Ricardo':
    if card_sheet == 'Caixa':
        spreadsheet = gc.open("caixa")
    else:
        spreadsheet = gc.open("bradesco")
    sheet = spreadsheet.worksheet('meses')
else:
    spreadsheet = gc.open("itau")
    sheet = spreadsheet.worksheet('meses')

get_month = sheet.cell(5, 1).value.capitalize()

month_sheet = spreadsheet.worksheet(get_month)

get_data = month_sheet.get_values('A2:C')

empty_line = month_sheet.col_values(1)

next_line = len(empty_line) + 1

linhas = []
updated_lines = []

invoice = [
    ['25/05', 'RAYOBYTE 521177', '79,20'],
    ['25/01', 'PAG*Box46 -CT 05/05', '87,00'],
]


def update_invoice():
    for i in linhas:
        for j, value in enumerate(i, start=1):
            month_sheet.update_cell(next_line, j, value)
        update_nextline()


def update_nextline():
    global next_line
    global empty_line
    empty_line = month_sheet.col_values(1)
    next_line = len(empty_line) + 1


def compare_lists(sheet_list, invoice_list):
    set_list = set(tuple(item) for item in sheet_list)

    for item in invoice_list:
        if tuple(item) not in set_list:
            updated_lines.append(item)


if sms_receiver == 'True':
    linhas = result_list
    month_sheet.update_cell(next_line, 1, linhas[0][0])
    month_sheet.update_cell(next_line, 2, linhas[0][1])
    month_sheet.update_cell(next_line, 3, linhas[0][2])
elif itau_pdf.fatura_itau:
    print('entrei no if do itau')
    linhas = itau_pdf.result_list2
    compare_lists(get_data, linhas)
    update_invoice()
    print(updated_lines)
else:
    linhas = handled_list
    print('executado essa linha')
    compare_lists(get_data, linhas)
    update_invoice()
    print(updated_lines)

sys.exit(0)
