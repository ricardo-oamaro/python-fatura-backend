from PyPDF2 import PdfReader
import re
from prettytable import PrettyTable

pdf = PdfReader('Bradesco.pdf')
page = pdf.pages[0]

text = page.extract_text()
texto = text

# TODO multiple pages
#for i in range(len(pdf.pages)):
 #   page = pdf.pages[i]
  #  texto += page.extract_text()

palavras_chave = ["MAR", "JUL", "AGO", "SET"]
meses = ["03", "07", "08", "09"]
padrao = r'(\d{2}/\w{3})(.*?)\((.*?)\)'

lista = []
lista_tratada = []


def remover_linhas(texto, inicio, fim):
    linhas = texto.split('\n')
    linhas = linhas[:inicio - 1] + linhas[fim:]
    novo_texto = '\n'.join(linhas)
    return novo_texto


def mover_linha_para_cima(texto, palavra_chave):
    linhas = texto.split('\n')
    i = 1
    while i < len(linhas):
        if linhas[i].startswith(palavra_chave):
            linhas[i - 1] += "/" + linhas[i]
            linhas.pop(i)  # Remove a linha juntada
        else:
            i += 1
    novo_texto = '\n'.join(linhas)
    return novo_texto


def separar_texto(texto):
    linhas = texto.split('\n')
    padrao = r'(\d{2}/\w{3})\s(.*?)\((.*?)\)\s(.*)'
    match = re.match(padrao, linhas)
    if match:
        partes = match.groups()
        return partes
    else:
        return "erro"


def adiciona_a_lista(texto):
    linhas = texto.split('\n')
    i = 0
    while i < len(linhas):
        lista.append(linhas[i].strip())
        i += 1


texto = remover_linhas(texto, 1, 13)
for p in palavras_chave:
    texto = mover_linha_para_cima(texto, p)

adiciona_a_lista(texto)

for l in lista:
     lista_separada = l.split('\xa0')
     sublista = [el.replace(' ', '') for el in lista_separada if el.strip()]
     lista_tratada.append(sublista)

data = ''
for i, lista in enumerate(lista_tratada):
    if len(lista) < 3:
        lista.insert(0, data)
        i+=1
    else:
        data = lista_tratada[i][0]
        i+=1

print(lista_tratada)