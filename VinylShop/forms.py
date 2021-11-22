# configure forms here


from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,IntegerField,SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError,NumberRange
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


class Card(FlaskForm):
    card_number = IntegerField('Card Number',validators= [DataRequired(),NumberRange(min=16,
                                                                                     max=16,message="Error! The card number must be of 16 digits.")])

    MONTH_CHOICES = [('Jan','January'),('Feb','February'),('Mar','March'),('Apr','April'),
                     ('May','May'),('Jun','June'),('Jul','July'),('Aug','August'),
                     ('Sep','September'),('Oct','October'),('Nov','November'),('Dec','December')]
    month = SelectField('Month',validators=DataRequired(),choices=MONTH_CHOICES)

    YEAR_CHOICES = [('0', '2021'), ('1', '2022'), ('2', '2023'), ('3', '2024'), ('4', '2025'), ('5', '2026'),
                    ('6', '2027'), ('7', '2028'), ('8', '2029'), ('9', '2030'), ('10', '2031'), ('11', '2032')]
    year = SelectField('Year',validators=DataRequired(),choices=YEAR_CHOICES)

    cvv = IntegerField('CVV', validators=[DataRequired(), NumberRange(min=3, max=3,
                                                                      message="Error! The CVV number must be of 3 digits.")])

    submit = SubmitField('Pay')


class ShippingDetails(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])
    submit = SubmitField('Continue')




if __name__ == '__main__':
    print("forms.py")
