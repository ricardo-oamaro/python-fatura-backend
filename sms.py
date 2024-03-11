import re
import sys
import app
import server

sms_file = './sms.txt'
sms_receiver = sys.argv[1]
owner_sheet = sys.argv[2]
card_sheet = sys.argv[3]
data = ''
result_list = []
handled_data_pattern = r'(\d{2}/\d{2})(\d+,\d{2})\s(.*?)'

with open(sms_file, 'r') as arquivo:
    for linha in arquivo:
        data = linha

# Encontrar a data no formato dd/MM
padrao_data = r'\d+/\d{2}'
date = re.search(padrao_data, data).group()

# Encontrar o valor
padrao_valor = r'\d+,\d{2}'
valor = re.search(padrao_valor, data).group()

# Encontrar o texto restante
# padrao_bradesco = r'VALOR DE R\$\s+(\d+,\d{2})\s+((?:\S+\s+){0,2}\S+)'
padrao_bradesco = r'VALOR DE R\$\s\d+\,\d{2}\s(.*?)(?=\s{3,})'
padrao_latampass = r' - (.*?) valor'
padrao_caixa = r'aprovada(.*?)R\$'
texto_restante = re.search(padrao_bradesco, data).group(1) if 'BRADESCO' in data else re.search(padrao_caixa, data).group(1)
print(texto_restante)


result_list.append([date, texto_restante, valor, ])
print(result_list)