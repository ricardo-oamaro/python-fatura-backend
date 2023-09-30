import re
import pdfplumber


with pdfplumber.open('/Users/ramaro/Desktop/pessoal_fatura/itaucard.pdf') as pdf:
    page = pdf.pages[1]
    data = page.extract_text()
    print(data)

# initial_data_pattern = re.compile(r'\d{2}/\d{2}(.*?\d+,\d{2})$') //possivel remoção
handled_data_pattern = re.compile(r'(\d{2}/\d{2})\s+(.*?)\s+(\d+,\d{2})')
result_list = []
result_list2 = []


for line in data.split('\n'):
    if handled_data_pattern.match(line):
        pattern = re.search(r'\d,\d{2}', line)
        if pattern:
            final_position = pattern.end()
            result = line[:final_position]
            result_list.append(result)
        else:
            print('Pattern no matches')

for line in result_list:
    text = line
    result = re.match(handled_data_pattern, text)
    if result:
        # print(result.group(3))
        date = result.group(1)
        desc = result.group(2)
        value = result.group(3)

        result_list2.append([date, desc, value])

for line in result_list2:
    print(line)



