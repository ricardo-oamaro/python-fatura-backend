import gspread
import bradesco_pdf
import itau_pdf


#connect to the service account
gc = gspread.service_account(filename="cred.json")

sh = gc.open("Teste").sheet1

linhas = itau_pdf.result_list2

# if itau_pdf.fatura_itau:
#     linhas = itau_pdf.result_list2
# else:
#     linhas = bradesco_pdf.handled_list
#     print('executado essa linha')

sh.update('A1:H', linhas)
