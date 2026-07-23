@app.route('/cantinho')
@login_necessario          # protege a rota - só entra quem tá logado
def cantinho():
    nome = session.get('usuario_nome')

    # contador de visitas (bônus)
    visitas = session.get('visitas_cantinho', 0)
    visitas += 1
    session['visitas_cantinho'] = visitas

    return render_template('cantinho.html',
        nome        = nome,
        cor         = 'Azul',              # <- coloque a SUA cor
        linguagem   = 'Python',            # <- coloque a SUA linguagem
        frase       = 'Feito é melhor que perfeito.',  # <- coloque a SUA frase
        visitas     = visitas
    )