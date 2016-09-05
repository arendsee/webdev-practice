# modified from Miguel Grinberg's tutorial

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    # DataRequired just checks if the input is empty
    openid = StringField('openid', validators=[DataRequired()])
    assyria = StringField('assyria', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
