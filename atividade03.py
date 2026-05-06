from flask import Flask, render_template

app = Flask(__name__)

# Questão 03
@app.route('/arearestrita/<int:id>')
def arearestrita(id):
    if id == 1:
        msg = "Cadeado Fechado"
    elif id == 2:
        msg = "Cadeado Aberto"
    else:
        msg = "Valor inválido"

    return render_template("resultado.html", resultado=msg)


# Questão 04
@app.route('/operacao/<tipo>/<float:op1>/<float:op2>')
def operacao(tipo, op1, op2):

    if tipo == "sum":
        res = op1 + op2
    elif tipo == "sub":
        res = op1 - op2
    elif tipo == "mult":
        res = op1 * op2
    elif tipo == "div":
        if op2 == 0:
            res = "Não dá pra dividir por zero"
        else:
            res = op1 / op2
    else:
        res = "Operação não existe"

    return render_template("resultado.html", resultado=res)


if __name__ == "__main__":
    app.run(debug=True)