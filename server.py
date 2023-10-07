import subprocess

from flask import Flask, render_template, request

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
    return 'Arquivo processado com sucesso!<br><br><button><a href="/" style="text-decoration: none; color: 333">Voltar para a Página Inicial</a></button>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
