import sys

import gspread
from bradesco_pdf import handled_list
import itau_pdf

sh_updated = False
#connect to the service account
gc = gspread.service_account(filename="cred.json")

sh = gc.open("Teste").sheet1

linhas = []

if itau_pdf.fatura_itau:
    linhas = itau_pdf.result_list2
else:
    linhas = handled_list
    print('executado essa linha')

sh.update('A1:C', linhas)
sys.exit(0)


