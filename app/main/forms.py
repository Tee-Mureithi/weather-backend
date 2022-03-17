from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField, DateField, SelectField,BooleanField,PasswordField
from ..models import User
from wtforms import ValidationError

# user subscription

class SubscriberForm(FlaskForm):
    email = StringField('Add email',validators=[DataRequired(),Email()])
    submit = SubmitField('Subscribe')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('This email is in use')