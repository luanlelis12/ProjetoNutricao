from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from formulario import CadastroForm, LoginForm, FazerDieta
from datetime import datetime

now = datetime.now()

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
    senha = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    aniversario = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '%r' % self.nome

class Dieta(db.Model):
    __tablename__ = 'dieta'
    codDieta = db.Column(db.Integer, primary_key=True)
    peso = db.Column(db.Float, nullable=False)
    altura = db.Column(db.Integer, nullable=False)
    objetivo = db.Column(db.String(7), nullable=False)
    TMB = db.Column(db.Float, nullable=False)
    Proteinas = db.Column(db.Float, nullable=False)
    Carboidratos =  db.Column(db.Float, nullable=False)
    Gordura = db.Column(db.Float, nullable=False)
    id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.context_processor
def user_logado_context():
    return dict(user_logado=user_logado)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():

    form = CadastroForm()

    if form.validate_on_submit():
        novo_user = User(nome = form.nome.data, email = form.email.data, sexo = form.sexo.data, aniversario = form.aniversario.data, senha = form.senha.data)
        db.session.add(novo_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('cadastro.html', form=form)

@app.route('/dieta', methods=['POST', 'GET'])
def dieta():

    form = FazerDieta()

    if form.validate_on_submit():
        user = User.query.filter_by(nome=user_logado).first()
        peso = form.peso.data
        altura = form.altura.data
        dNiver = user.aniversario
        yNiver = dNiver.year
        yNow = now.year
        idade = yNow-yNiver
        print(idade)
        Proteinas = 2.5*peso
        Gordura = 1*peso
        Carboidratos = 0
        if user.sexo is 'F':
            TMB = (655+(9.6*peso)+(1.8*altura)-(4.7*idade))
        if user.sexo is 'M':
            TMB = (66+(13.8*peso)+(5*altura)-(6.8*idade))
        nova_dieta = Dieta(peso = form.peso.data, altura = form.altura.data, objetivo = form.objetivo.data, TMB = TMB, Proteinas = Proteinas, Carboidratos = Carboidratos, Gordura = Gordura, id = user.id)
        db.session.add(nova_dieta)
        db.session.commit()

    return render_template('dieta.html', form=form)

@app.route('/fale conosco')
def fala():
    return render_template('fala.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    
    form = LoginForm()

    if form.validate_on_submit():
           
        user = User.query.filter_by(nome=form.nome.data).first()

        if user:
            if user.senha == form.senha.data and user.email == form.email.data:
                global user_logado
                user_logado = form.nome.data
                return redirect(url_for('index'))
            else:
                return 'osdjajdksa'

    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)