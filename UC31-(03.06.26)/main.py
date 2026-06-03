from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def cadastro():
    return render_template('index.html')

@app.route('/validacao', methods=['POST'])
def validacao():
    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email', '').strip().lower()
    cidade = request.form.get('cidade', '').strip().title()

    return f"""
    <h1>Dados cadastrados:</h1>
    <p>Nome: {nome}</p>
    <p>Email: {email}</p>
    <p>Cidade: {cidade}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)       
    