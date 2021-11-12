# configure forms here


from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from VinylShop.models import User


class registrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=5, max=15)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign UP')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()  # WE ARE GETTING FIRST VALUE FORM THE DATABASE
        # IF THERE IS A VALUE WE GET THE FIRST ONE THERE IF WE DONT IT IS SIMPLY GOING TO RETURN NONE
        if user:  # IF THE USER EXIST ALREADY
            raise ValidationError('Username is already taken')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already Registered')


class loginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember = BooleanField('Remember Me')


    submit = SubmitField('Login')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


if __name__ == '__main__':
    print("forms.py")