from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, BooleanField
from wtforms.validators import DataRequired, Email


class languageForm(FlaskForm):
    file_path = StringField('file_path', validators=[DataRequired(), Email()])
    language_select = SelectField('language_select', choices=[(None, ), ('java', 'java'), ('python', 'python'), ('c++', 'c++')],
                           validators=[DataRequired()])
