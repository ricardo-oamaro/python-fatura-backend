from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_python_script')
def run_python_script():
    file = open(r'itau_pdf.py', 'r').read()
    return exec(file)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
