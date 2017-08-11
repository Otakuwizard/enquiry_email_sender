from . import main
from flask import request, render_template, redirect, url_for, current_app, flash
from ..email import send_mail
from forms import EnquiryEmail
from ..models import Enquiry, Quote

@main('/', methods=['GET', 'POST'])
def index():
    form = EnquiryEmail()
    if form.validate_on_submit():
        new_enquiry = Enquiry(
            enquiry_number=form.enquiry_number.datta,
            brand=form.brand.data,
            typ_number=form.typ_number.data,
            amount=form.amount.data,
            recipient=form.to.data,
            asker=form.asker.data,
            )

        if form.language.data == 1:
            template = 'mail/DE.html'
        elif form.language.data == 2:
            template = 'mail/EN.html'
        
          

