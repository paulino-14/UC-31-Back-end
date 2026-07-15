from flask import Flask, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# variaveis globais so pra guardar o usuario temporariamente (nao pode usar banco de dados)
nome_usuario = ""
senha_hash = ""


# rota da pagina de cadastro
@app.route("/", methods=["GET", "POST"])
def cadastro():
    global nome_usuario, senha_hash

    if request.method == "POST":
        # pega os dados que vieram do formulario
        nome = request.form["nome"]
        senha = request.form["senha"]

        # gera o hash da senha e guarda nas variaveis globais
        nome_usuario = nome
        senha_hash = generate_password_hash(senha)

        # depois de cadastrar manda pro login
        return redirect(url_for("login"))

    return render_template("cadastro.html")


# rota da pagina de login
@app.route("/login", methods=["GET", "POST"])
def login():
    erro = ""

    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]

        # primeiro confere se o nome bate com o que foi cadastrado
        if nome != nome_usuario:
            erro = "Usuário não encontrado."
        else:
            # se o nome tiver certo, confere a senha usando o check_password_hash
            if check_password_hash(senha_hash, senha):
                return redirect(url_for("inicio"))
            else:
                erro = "Senha inválida."

    return render_template("login.html", erro=erro)


# rota da pagina inicial (só entra aqui se o login der certo)
@app.route("/inicio")
def inicio():
    return render_template("inicio.html", nome=nome_usuario)


if __name__ == "__main__":
    app.run(debug=True)
