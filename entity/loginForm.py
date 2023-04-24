from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    category = SelectField('category', choices=[('', '- 地区 -'), ('1', '中国大陆'), ('2', '中国香港地区'), ('3', '中国台湾地区')],
                           validators=[DataRequired()])
    priority = RadioField('priority', choices=[('email', '邮箱登录'), ('phone', '电话登录')], validators=[DataRequired()])
    agreement = BooleanField('agreement', validators=[DataRequired()])