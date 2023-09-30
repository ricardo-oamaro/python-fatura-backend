import gspread
from pdf import *
import itau_pdf

texto = lista_tratada

#connect to the service account
gc = gspread.service_account(filename="cred.json")

sh = gc.open("Teste").sheet1

linhas = itau_pdf.result_list2

sh.update('A1:H', linhas)
