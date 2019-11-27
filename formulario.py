from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, SelectField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class CadastroForm(FlaskForm):
    nome = StringField('Nome completo', validators=[DataRequired(), Length(min=3,max=60)])
    sexo = SelectField('Sexo', choices=[('M', 'Masculino'), ('F', 'Feminino')], validators=[DataRequired()])
    aniversario = DateField('Data de nascimento', format='%Y-%m-%d')
    email = StringField('E-mail', validators=[DataRequired(), Email(), Length(min=6,max=60)])
    senha = PasswordField('Senha (6 dígitos numéricos)*', validators=[DataRequired(), Length(min=6,max=20), EqualTo('confirmar', message='Senhas diferentes')])
    confirmar = PasswordField('Verificar senha*', validators=[DataRequired(), Length(min=6,max=20)])
    botao = SubmitField('FINALIZAR')

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    senha = PasswordField('Senha (6 dígitos numéricos)', validators=[DataRequired()])
    botao = SubmitField('LOGAR')

class FazerDieta(FlaskForm):
    peso = FloatField('Massa Corporal (em Kg)', validators=[DataRequired()])
    altura = IntegerField('Estatura (em cm)', validators=[DataRequired()])
    objetivo = SelectField('Objetivo', choices=[('bulking', 'Ganhar massa magra'), ('cutting', 'Perder gordura')], validators=[DataRequired()])
    botao = SubmitField('CRIAR DIETA')