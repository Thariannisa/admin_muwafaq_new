# from email.message import EmailMessage
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    EmailField,
    # FloatField,
)
# from wtforms.fields.choices import SelectField
# from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email, InputRequired


class LoginForm(FlaskForm):
    email = EmailField(
        validators=[DataRequired(),  Email()],  render_kw={"placeholder": "Masukkan email"}
    )
    password = PasswordField(
        validators=[DataRequired(), Length(min=3, max=25)], render_kw={"placeholder": "Masukkan password"}
    )

    submit = SubmitField(label="MASUK")
