from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, ValidationError, TextAreaField, IntegerField, SelectField
from wtforms.validatiors import Email, Length, Required, Regexp, EqualTo
from ..models import Enquiry

class EnquiryEmail(FlaskForm):
    language = SelectField('Sprache', ocerce=int)
    to = StringField('An', validatiors=[Required(), Email(), Length(1, 64)])
    salutation = StringField('Anrede')
    enquiry_number = StringField('Anfrage-Nummer', validators=[Required(), Length(1,64)])
    brand = StringField('Marke', validators=[Required(), Length(1,64)])
    typ_number = StringField('Artikelnummer', validators=[Required(), Length(1,64)])
    amount = IntegerField('Menge', validators=[Required()])
    asker = StringField('Von', validators=[Required(), Length(1, 64)])
    submit = SubmitField('Senden')

    def __init__(self, *args, **kw):
        super(EnquiryEmail, self).__init__(*args, **kw)
        self.to.choices = [(1, 'Deutsch'), (2, 'English')]
    