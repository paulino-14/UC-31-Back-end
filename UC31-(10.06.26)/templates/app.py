from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def inicio():
    nome = request.cookies.get('nome')
    tema = request.cookies.get('tema', 'claro')
    return render_template('inicio.html', nome=nome, tema=tema)

@app.route('/salvar_nome', methods=['POST'])
def salvar_nome():
    nome = request.form['nome']
    resp = make_response(redirect(url_for('inicio')))
    resp.set_cookie('nome', nome)
    return resp

@app.route('/trocar_tema/<escolha>')
def trocar_tema(escolha):
    resp = make_response(redirect(url_for('inicio')))
    resp.set_cookie('tema', escolha)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
