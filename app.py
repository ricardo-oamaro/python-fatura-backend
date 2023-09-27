import gspread
from pdf import *
import re

texto = novo_texto

#connect to the service account
gc = gspread.service_account(filename="cred.json")

sh = gc.open("Teste").sheet1

linhas = texto.split('\n')


for i, linha in enumerate(linhas):
    sh.update_cell(i+1, 1, linha)
 #   colunas = linha.split()
 #   for j, coluna in enumerate(colunas):
  #      sh.update_cell(i + 1, j + 1, coluna)

#name = sh.acell("a2").value
#website = sh.acell("b2").value

#print(name)
#print(website)