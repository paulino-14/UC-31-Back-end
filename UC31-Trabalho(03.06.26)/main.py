from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  
def cadastro():
    mensagem = ""
    dados = {}

    if request.method == 'POST':
        
        nome = request.form.get('nome', '').strip().title()
        email = request.form.get('email', '').strip().lower()
        telefone = request.form.get('telefone', '').strip().replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
        cpf = request.form.get('cpf', '').strip().replace('.', '').replace('-', '')
        cidade = request.form.get('cidade', '').strip().title()
        estado = request.form.get('estado', '').strip().upper()
        curso = request.form.get('curso', '').strip().title()
        idade = request.form.get('idade', '').strip()
        senha = request.form.get('senha', '').strip()

        
        if not all([nome, email, telefone, cpf, cidade, estado, curso, idade, senha]):
            mensagem = "Preencha todos os campos obrigatórios."
        elif len(nome) < 8:
            mensagem = "Nome inválido."
        elif '@' not in email or '.com' not in email:
            mensagem = "E-mail inválido."
        elif len(telefone) != 11 or not telefone.isdigit():
            mensagem = "Telefone inválido."
        elif len(cpf) != 11 or not cpf.isdigit():
            mensagem = "CPF inválido."
        elif len(cidade) < 3:
            mensagem = "Cidade inválida."
        elif len(estado) != 2:
            mensagem = "Estado inválido."
        elif not idade.isdigit() or int(idade) < 16:
            mensagem = "Idade inválida."
        elif len(senha) < 8 or not any(char.isdigit() for char in senha):
            mensagem = "Senha muito fraca."
        else:
            mensagem = "Cadastro realizado com sucesso!"
            dados = {
                "Nome": nome,
                "E-mail": email,
                "Telefone": telefone,
                "CPF": cpf,
                "Cidade": cidade,
                "Estado": estado,
                "Curso": curso,
                "Idade": idade
            }

    return render_template('cadastro.html', mensagem=mensagem, dados=dados)

if __name__ == '__main__':
        app.run(debug=True)
