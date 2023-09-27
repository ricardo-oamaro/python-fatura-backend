tabela = PrettyTable()

tabela.field_names = ["Data", "Descrição", "Preço"]

for linha in texto:
    tabela.add_row(linha)

print(tabela)