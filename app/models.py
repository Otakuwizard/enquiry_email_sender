from . import db
from flask import current_app
import uuid, time, hashlib
from datetime import datetime

def generate_id():
    return '%015d%s000' % (int(time.time()*1000), uuid.uuid4().hex)

class Enquiry(db.Model):
    __tablename__ = 'enquiries'
    id = db.Column(db.String(64), primary_key=True, default=generate_id)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    enquiry_number = db.Column(db.String(64), index=True, unique=True)
    brand = db.Column(db.String(32), index=True)
    typ_number = db.Column(db.String(64))
    amount = db.Column(db.Integer)
    recipient = db.Column(db.String(64))
    asker = db.Column(db.String(64))
    quotes = db.relationship('Quote', backref='enquiry', lazy='dynamic')

class Quote(db.Model):
    __tablename__ = 'quotes'
    id = db.Column(db.String(64), primary_key=True, defualt=generate_id)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    quote_number = db.Column(db.String(64), index=True)
    enquiry_id = db.Column(db.String(64), db.ForeignKey('enquiries.number'))
    series_number = db.Column(db.String(64), index=True)
    discount = db.Column(db.Float)
    unit_price = db.Column(db.Float)
    total_price = db.Column(db.Float)
    hs_code = db.Column(db.String(32))
    freight = db.Column(db.Float)
    delivery_time = db.Column(db.String(32))
    weight = db.Column(db.Float)


