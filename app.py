from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from formulario import CadastroForm, LoginForm

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BancoDeDados.db'
app.config['SECRET_KEY'] = 'akjdshsagdgajdgmnxmch'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    senha = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    aniversario = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '%r' % self.nome

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():

    form = CadastroForm()

    if form.validate_on_submit():
        
        user = User()
        
        user.nome = form.nome.data
        user.email = form.email.data
        user.sexo = form.sexo.data
        user.aniversario = form.aniversario.data
        user.senha = form.senha.data
        
        db.session.add(user)
        db.session.commit()

    return render_template('cadastro.html', form=form)

@app.route('/dieta')
def dieta():
    return render_template('dieta.html')

@app.route('/fale conosco')
def fala():
    return render_template('fala.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    
    form = LoginForm()

    if form.validate_on_submit():
           
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data
        
        senhadata = db.execute("SELECT senha FROM user WHERE senha=:senha",{"senha":senha}).fetchone()

        if senha == senhadata:
            return render_template('index.html') 

            
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)