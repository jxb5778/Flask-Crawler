from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class QueryFileForm(FlaskForm):
    filename = StringField('Filename', validators=[DataRequired()])
    value = StringField('Value', validators=[DataRequired()])
    submit = SubmitField('Search')


class SearchDirectoryForm(FlaskForm):
    directory = StringField('Directory', validators=[DataRequired()])
    pandas_query = StringField('Pandas Query', validators=[DataRequired()])
    submit = SubmitField('Display')


class FileDisplayForm(FlaskForm):
    filename = StringField('Filename', validators=[DataRequired()])
    submit = SubmitField('Display')
