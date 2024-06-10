# pip install flask-wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from Comunidade_fantastica.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(),Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado.Cadastre-se com outro e-mail ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('senha', validators=[DataRequired(),Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar a foto do perfil', validators=[FileAllowed(['jpg', 'png'])])
    cursos_seres_magicos = BooleanField('Seres Mágicos')
    cursos_ervas_natureza = BooleanField('Ervas e Natureza')
    cursos_ocultismo = BooleanField('Ocultismo')
    cursos_vida_alternativa = BooleanField('Vida Alternativa')
    cursos_sobrevivencialismo = BooleanField('Sobrevivencialismo')
    cursos_criacoes = BooleanField('Criações')
    cursos_comidas = BooleanField('Comidas')
    cursos_lendas = BooleanField('Lendas')
    cursos_gnomos = BooleanField('Gnomos')
    cursos_duendes = BooleanField('Duendes')
    cursos_fadas = BooleanField('Fadas')
    cursos_bruxas = BooleanField('Bruxas')
    cursos_terror = BooleanField('Terror')
    cursos_colecionaveis = BooleanField('Colecionaveis')
    cursos_moda = BooleanField('Moda')
    cursos_curiosidades = BooleanField('Curiosidades')
    cursos_comunidade = BooleanField('Comunidade')
    cursos_anuncios = BooleanField('Anúncios')
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse e-mail. Cadastre outro e-mail')


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu Post Aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')