import os
import subprocess
from os.path import exists

from flask import Flask, render_template, request, redirect
from twilio import twiml

sms = False
owner_sheet = ''

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_python_script')
def run_python_script():
    file = open(r'itau_pdf.py', 'r').read()
    return exec(file)


@app.route('/processar_pdf', methods=['POST'])
def processar_pdf():
    file = request.files['pdf_file']
    file.save('arquivo.pdf')  # Salva o arquivo enviado
    subprocess.run(['python3', 'itau_pdf.py', 'arquivo.pdf'])
    return 'Arquivo processado com sucesso!<br><br><button><a href="/" style="text-decoration: none; color: ' \
           '333">Voltar para a Página Inicial</a></button>'


@app.route('/salvar_pdf', methods=['POST'])
def salvar_pdf():
    global sms
    global owner_sheet
    sms = False
    texto = request.form['texto']
    owner_sheet = request.form['opcao']
    card_sheet = request.form['cartao']
    file = request.files['pdf_file']
    print(file)
    if texto:
        sms = True
        if exists('arquivo.pdf'):
            os.remove('arquivo.pdf')
        with open('sms.txt', 'w') as file:
            file.write(texto)
        subprocess.run(['python3', 'sms.py', str(sms), str(owner_sheet), str(card_sheet)])
    else:
        sms = False
        file.save('arquivo.pdf')  # Salva o arquivo enviado
        subprocess.run(['python3', 'itau_pdf.py', str(sms), str(owner_sheet)])
    return 'Conteúdo salvo em arquivo.pdf com sucesso!<br><br><button><a href="/" style="text-decoration: none; color: ' \
           '333">Voltar para a Página Inicial</a></button>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
