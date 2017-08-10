from . import main
from flask import request, render_template, redirect, url_for, current_app, flash
from ..email import send_mail

@main('/', methods=['GET', 'POST'])
def index():

