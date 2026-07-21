from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

ARQUIVO = "livros.json"


def carregar_livros():
    """Lê o arquivo JSON e retorna a lista de livros."""

    # se o arquivo ainda não existe, cria como uma lista vazia
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_livros(lista_livros):
    """Salva a lista de livros no arquivo JSON."""

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            lista_livros,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


@app.route("/", methods=["GET", "POST"])
def cadastro():
    erro = None

    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        autor = request.form["autor"].strip()
        ano = request.form["ano"].strip()
        categoria = request.form["categoria"].strip()
        quantidade = request.form["quantidade"].strip()

        # validação: nenhum campo pode ficar vazio
        if not titulo or not autor or not ano or not categoria or not quantidade:
            erro = "Todos os campos são obrigatórios."
            return render_template("cadastro.html", erro=erro)

        # validação: ano precisa ser número
        if not ano.isdigit():
            erro = "O ano deve conter apenas números."
            return render_template("cadastro.html", erro=erro)

        # validação: quantidade precisa ser número inteiro maior que zero
        if not quantidade.isdigit() or int(quantidade) <= 0:
            erro = "A quantidade deve ser um número inteiro maior que zero."
            return render_template("cadastro.html", erro=erro)

        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": int(ano),
            "categoria": categoria,
            "quantidade": int(quantidade)
        }

        livros = carregar_livros()
        livros.append(livro)
        salvar_livros(livros)

        return redirect(url_for("listar"))

    return render_template("cadastro.html", erro=erro)


@app.route("/livros")
def listar():
    livros = carregar_livros()
    return render_template("livros.html", livros=livros)


@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    resultado = None
    encontrado = False
    pesquisado = False

    if request.method == "POST":
        pesquisado = True
        titulo_buscado = request.form["titulo"].strip().lower()

        livros = carregar_livros()

        for livro in livros:
            if livro["titulo"].lower() == titulo_buscado:
                resultado = livro
                encontrado = True
                break

    return render_template(
        "buscar.html",
        resultado=resultado,
        encontrado=encontrado,
        pesquisado=pesquisado
    )


@app.route("/editar/<int:indice>", methods=["GET", "POST"])
def editar(indice):
    livros = carregar_livros()

    # se o índice não existir, volta pra listagem
    if indice < 0 or indice >= len(livros):
        return redirect(url_for("listar"))

    erro = None

    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        autor = request.form["autor"].strip()
        ano = request.form["ano"].strip()
        categoria = request.form["categoria"].strip()
        quantidade = request.form["quantidade"].strip()

        if not titulo or not autor or not ano or not categoria or not quantidade:
            erro = "Todos os campos são obrigatórios."
            return render_template("editar.html", livro=livros[indice], indice=indice, erro=erro)

        if not ano.isdigit():
            erro = "O ano deve conter apenas números."
            return render_template("editar.html", livro=livros[indice], indice=indice, erro=erro)

        if not quantidade.isdigit() or int(quantidade) <= 0:
            erro = "A quantidade deve ser um número inteiro maior que zero."
            return render_template("editar.html", livro=livros[indice], indice=indice, erro=erro)

        livros[indice] = {
            "titulo": titulo,
            "autor": autor,
            "ano": int(ano),
            "categoria": categoria,
            "quantidade": int(quantidade)
        }

        salvar_livros(livros)

        return redirect(url_for("listar"))

    return render_template("editar.html", livro=livros[indice], indice=indice, erro=erro)


@app.route("/excluir/<int:indice>")
def excluir(indice):
    livros = carregar_livros()

    if 0 <= indice < len(livros):
        livros.pop(indice)
        salvar_livros(livros)

    return redirect(url_for("listar"))


if __name__ == "__main__":
    app.run(debug=True)