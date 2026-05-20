from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
@app.route ('/index')
def index():
    return render_template('index.html', usuario=None , nome=None, title='Nome')

@app.route('/contato')
def contato ():
    nome = 'JP'
    return render_template('index.html', title= 'Página inicial ', nome=nome , usuario=None )   

@app.route('/usuario ')
def usuario ():
    usuario = {' nome ': 'JP ', 'email ': 'joaopedropaulino122@gmail.com'}
    return render_template('index.html ', title = ' Página Inicial', usuario=usuario, nome=None  ) 


if __name__ == '__main__':
    app.run(debug=True)