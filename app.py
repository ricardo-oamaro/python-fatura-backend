import sys

import gspread
from bradesco_pdf import handled_list
from sms import result_list, sms_receiver
import itau_pdf

sh_updated = False
# connect to the service account
gc = gspread.service_account(filename="cred.json")

spreadsheet = gc.open("bradesco")

sheet = spreadsheet.worksheet('meses')

get_month = sheet.cell(1, 1).value

month_sheet = spreadsheet.worksheet(get_month)

empty_line = month_sheet.col_values(1)

next_line = len(empty_line) + 1

print(month_sheet)

linhas = []

if sms_receiver == 'True':
    linhas = result_list
    print(linhas)
elif itau_pdf.fatura_itau:
    linhas = itau_pdf.result_list2
else:
    linhas = handled_list
    print('executado essa linha')

month_sheet.update_cell(next_line, 1, linhas[0][0])
month_sheet.update_cell(next_line, 2, linhas[0][1])
month_sheet.update_cell(next_line, 3, linhas[0][2])
sys.exit(0)
