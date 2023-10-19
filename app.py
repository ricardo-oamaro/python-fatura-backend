import sys

import gspread

from bradesco_pdf import handled_list
from sms import result_list, sms_receiver
import itau_pdf

sh_updated = False
# connect to the service account
gc = gspread.service_account(filename="cred.json")

spreadsheet = gc.open("bradesco")

##### logica sms
sheet = spreadsheet.worksheet('meses')

get_month = sheet.cell(5, 1).value.capitalize()
print(get_month)

month_sheet = spreadsheet.worksheet(get_month)

get_data = month_sheet.get_values('A2:C')
print(get_data)

########################################

#TODO adicionar os itens uma nova lista e fazer o update nas linhas vazias

linhas = []


def update_invoice():
    month_sheet.update('A2:C', get_data)


def compare_lists(sheet_list, invoice_list):
    set_list = set(tuple(item) for item in sheet_list)

    for item in invoice_list:
        if tuple(item) not in set_list:
            get_data.append(item)


if sms_receiver == 'True':
    linhas = result_list
    empty_line = month_sheet.col_values(1)
    next_line = len(empty_line) + 1
    month_sheet.update_cell(next_line, 1, linhas[0][0])
    month_sheet.update_cell(next_line, 2, linhas[0][1])
    month_sheet.update_cell(next_line, 3, linhas[0][2])
elif itau_pdf.fatura_itau:
    linhas = itau_pdf.result_list2
    compare_lists(get_data, itau_pdf.result_list2)
    update_invoice()
else:
    linhas = handled_list
    print('executado essa linha')
    update_invoice()

for i in get_data:
    print(i)

sys.exit(0)
