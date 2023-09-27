import gspread
from pdf import *
import re

texto = lista_tratada

#connect to the service account
gc = gspread.service_account(filename="cred.json")

sh = gc.open("Teste").sheet1

linhas = texto

sh.update('A1:C', linhas)
