from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route("/")
@app.route("/index")
def index():
    return render_template("login.html")


# Página de resultado
@app.route("/resultado", methods=["GET"])
def resultado():

    nome = request.args.get("nome")
    curso = request.args.get("curso")
    cidade = request.args.get("cidade")
    email = request.args.get("email")

    return render_template(
        "resultado.html",
        nome=nome,
        curso=curso,
        cidade=cidade,
        email=email
    )


if __name__ == "__main__":
    app.run(debug=True)