from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from formulario import CadastroForm, LoginForm, FazerDieta

global user_logado
user_logado = 'Fazer login'

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BancoDeDados.db'
app.config['SECRET_KEY'] = 'akjdshsagdgajdgmnxmch'


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    senha = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    aniversario = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '%r' % self.nome

@app.context_processor
def user_logado_context():
    return dict(user_logado=user_logado)

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():

    form = CadastroForm()

    if form.validate_on_submit():    
        NewUser = User(nome = form.nome.data, email = form.email.data, sexo = form.sexo.data, aniversario = form.aniversario.data, senha = form.senha.data)
        db.session.add(NewUser)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('cadastro.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    
    form = LoginForm()

    if form.validate_on_submit():
           
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            if user.email == form.email.data and user.senha == form.senha.data:
                global user_logado
                user_logado = user.nome
                return redirect(url_for('index'))
            else:
                return '<h1>ERRO - Conta não encontrada</h1>'

    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)