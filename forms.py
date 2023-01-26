from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegistrationForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), Email(message=None,
                                                                        granular_message=False,
                                                                        check_deliverability=True,
                                                                        allow_smtputf8=True,
                                                                        allow_empty_local=False)])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=6, message=None)])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("SIGN ME UP!")


class LoginForm(FlaskForm):
    login_email = EmailField(label="Email", validators=[DataRequired()])
    login_password = PasswordField(label="Password", validators=[DataRequired()])
    login_submit = SubmitField("Let me in, betch!")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")