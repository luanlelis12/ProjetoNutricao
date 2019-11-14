from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class CadastroForm(FlaskForm):
    nome = StringField('Nome completo', validators=[DataRequired(), Length(min=3,max=60)])
    sexo = SelectField('Sexo', choices=[('M', 'Masculino'), ('F', 'Feminino')], validators=[DataRequired()])
    aniversario = DateField('Data de nascimento', format='%Y-%m-%d')
    email = StringField('E-mail', validators=[DataRequired(), Email(), Length(min=6,max=60)])
    senha = PasswordField('Senha (6 dígitos numéricos)*', validators=[DataRequired(), Length(min=6,max=20)])
    confirmar = PasswordField('Verificar senha*', validators=[DataRequired(), EqualTo('senha', message='Senhas diferentes')])
    botao = SubmitField('FINALIZAR')

class LoginForm(FlaskForm):
    nome = StringField('Nome completo', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    senha = PasswordField('Senha (6 dígitos numéricos)', validators=[DataRequired()])
    botao = SubmitField('LOGAR')