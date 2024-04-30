from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, DateField
from wtforms.validators import DataRequired
from datetime import date


class RegisterForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField(
        'Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    birthday = DateField(
        'Дата рождения', validators=[DataRequired()])
    about = TextAreaField("О себе")
    submit = SubmitField('Зарегистрироваться')
