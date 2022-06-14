from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    FileField,
    BooleanField,
    FloatField,
    TextAreaField,
    URLField,
    SelectField,
    EmailField,

)
from flask_ckeditor import CKEditorField
from wtforms.fields import TextAreaField

from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Regexp, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.widgets import TextArea


class KontenTulisanForm(FlaskForm):
    judul = StringField(
        label="Judul", validators=[DataRequired(), Length(min=3, max=25)], render_kw={"placeholder": "masukkan judul tulisan"}
    )
    # tulisan = CKEditorField(
    #     label="Tulisan", validators=[DataRequired(), Length(min=3, max=800)], render_kw={"placeholder": "masukkan pembahasan"}
    # )
    tulisan = TextAreaField('tulisan', widget=TextArea(), validators=[DataRequired(), Length(
        min=3, max=1300)],  render_kw={"placeholder": "masukkan pembahasan"})
    # tulisan = StringField(
    #     label="Tulisan", validators=[DataRequired(), Length(min=3, max=25)], render_kw={"placeholder": "masukkan tulisan"}
    # )


class KontenVideoForm(FlaskForm):
    judul = StringField(
        label="Judul", validators=[DataRequired(), Length(min=3, max=25)], render_kw={"placeholder": "masukkan judul video"}
    )
    author = StringField(
        label="Author", validators=[DataRequired(), Length(min=3, max=25)], render_kw={"placeholder": "masukkan nama author"}
    )

    video = FileField('Upload Video', validators=[
        FileRequired(),
        FileAllowed(['mp4'], 'Images only!')
    ])


class KontenVideo2Form(FlaskForm):
    judul = StringField(
        label="Judul", validators=[DataRequired(), Length(min=3, max=25)], render_kw={"placeholder": "masukkan judul video"}
    )
    author = StringField(
        label="Author", validators=[Length(min=3, max=25)], render_kw={"placeholder": "masukkan nama author"}
    )
    tulisan = TextAreaField('tulisan', widget=TextArea(), validators=[Length(
        min=3, max=1300)],  render_kw={"placeholder": "masukkan pembahasan"})

    video = FileField('Upload Video', validators=[
        FileAllowed(['mp4'], 'Images only!')
    ])


class AddTemaForm(FlaskForm):
    tema = StringField(
        label="Tema", validators=[DataRequired("Judul is Required"), Length(min=3, max=25)], render_kw={"placeholder": "Masukkan tema"}
    )

    submit = SubmitField(label="Submit")


class AddDiskusiForm(FlaskForm):
    platform = StringField(
        label="Platform", validators=[DataRequired("Platform is Required"), Length(min=3, max=25)], render_kw={"placeholder": "Masukkan Platform"}
    )
    link = URLField(
        label="Link", validators=[DataRequired("link is Required"), Length(min=3, max=70), Regexp('^(http|https):\/\/[\w.\-]+(\.[\w.\-]+)+.*$', 0,
                                                                                                  'URL must be a valid link')], render_kw={"placeholder": "Masukkan Link Diskusi"}
    )

    keterangan = StringField(
        label="Keterangan", validators=[DataRequired("Keterangan is Required"), Length(min=3, max=200)], render_kw={"placeholder": "Masukkan Keterangan"}
    )
    submit = SubmitField(label="Submit")


class AddModulForm(FlaskForm):
    judul = StringField(
        label="Judul", validators=[DataRequired("Judul is Required"), Length(min=3, max=28)], render_kw={"placeholder": "Masukkan Judul"}
    )
    PDF = FileField(
        label="Modul (Modul berupa PDF)", validators=[DataRequired("Modul is Required"), ],
    )

    submit = SubmitField(label="Submit")


class AddLatihanForm(FlaskForm):
    pertanyaan = StringField(
        label="Pertanyaan", validators=[DataRequired("Pertanyaan is Required"), Length(min=3, max=170)], render_kw={"placeholder": "Masukkan Pertanyaan"}
    )
    pilihan1 = StringField(
        label="Pilihan1", validators=[DataRequired("Pilihan1 is Required"), Length(min=3, max=70)], render_kw={"placeholder": "Masukkan Pilihan1"}
    )
    pilihan2 = StringField(
        label="Pilihan2", validators=[DataRequired("Pilihan2 is Required"), Length(min=3, max=70)], render_kw={"placeholder": "Masukkan Pilihan2"}
    )
    pilihan3 = StringField(
        label="Pilihan3", validators=[DataRequired("Pilihan3 is Required"), Length(min=3, max=70)], render_kw={"placeholder": "Masukkan Pilihan3"}
    )
    pilihan4 = StringField(
        label="Pilihan4", validators=[DataRequired("Pilihan4 is Required"), Length(min=3, max=70)], render_kw={"placeholder": "Masukkan Pilihan4"}
    )
    submit = SubmitField(label="Submit")


class LoginForm(FlaskForm):
    email = EmailField(
        validators=[DataRequired(),  Email()],  render_kw={"placeholder": "Masukkan email"}
    )
    password = PasswordField(
        validators=[DataRequired(), Length(min=3, max=25)], render_kw={"placeholder": "Masukkan password"}
    )
    nama = StringField(
        label="Nama", validators=[DataRequired(), Length(min=3, max=25)], render_kw={"placeholder": "masukkan nama"}
    )

    submit = SubmitField(label="MASUK")


class EditTulisanForm(FlaskForm):
    judul = StringField(
        label="Judul", validators=[DataRequired(), Length(min=3, max=25)], render_kw={"placeholder": "masukkan judul tulisan"}
    )
    # tulisan = CKEditorField(
    #     label="Tulisan", validators=[DataRequired(), Length(min=3, max=800)], render_kw={"placeholder": "masukkan pembahasan"}
    # )
    tulisan = StringField(
        label="Tulisan",  validators=[DataRequired(), Length(min=3, max=1300)], render_kw={"placeholder": "masukkan judul tulisan"}
    )
    # tulisan = StringField(
    #     label="Tulisan", validators=[DataRequired(), Length(min=3, max=25)], render_kw={"placeholder": "masukkan tulisan"}
    # )
