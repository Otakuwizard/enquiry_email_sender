from . import mail
from flask_mail import Message
from flask import cuttent_app, render_template
from threading import Thread

def async_send_mail(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(to, subject, template, **kw):
    app = current_app._get_current_object()
    msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + ' ' + subject,\
        sender=app.config['MAIL_SENDER'], recipients=[to])
    mag.html = render_template(template + '.html', **kw)
    thr = Thread(target=async_send_mail, args=[app, msg])
    thr.start()

    return thr
