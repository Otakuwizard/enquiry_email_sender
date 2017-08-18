from . import db
from flask import current_app
import uuid, time, hashlib
from datetime import datetime

def generate_id():
    return '%015d%s000' % (int(time.time()*1000), uuid.uuid4().hex)

class Enquiry(db.Model):
    __tablename__ = 'enquiries'
    id = db.Column(db.String(64), primary_key=True, default=generate_id)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    asker = db.Column(db.String(32), nullable=False)
    enquiry_number = db.Column(db.String(64), index=True, nullable=False)
    brand = db.Column(db.String(32), index=True)
    recipient = db.Column(db.Text())
    quotes = db.relationship('Quote', backref='enquiry', lazy='dynamic')
    enquiry_tables = db.relationship('EnquiryTable', backref='enquiry', lazy='dynamic')

    def __repr__(self):
        return '<Quiry %r-%r-%r>' % (self.asker, self.brand, self.enquiry_number)

class EnquiryTable(db.Model):
    __tablename__ = 'enquiry_tables'
    id = db.Column(db.String(64), primary_key=True, default=generate_id)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    typ_number = db.Column(db.String(64))
    amount = db.Column(db.Integer)
    enquiry_number = db.Column(db.String(64), db.ForeignKey('enquiries.enquiry_number'))

class Quote(db.Model):
    __tablename__ = 'quotes'
    id = db.Column(db.String(64), primary_key=True, defualt=generate_id)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    quote_number = db.Column(db.String(64), index=True, nullable=False)
    quoter = db.Column(db.String(32), nullable=False)
    enquiry_number = db.Column(db.String(64), db.ForeignKey('enquiries.enquiry_number'))
    quote_tables = db.relationship('QuoteTable', backref='quote', lazy='dynamic')
    
class QuoteTable(db.Model):
    __tablename__ =  'quote_tables'
    id = db.Column(db.String(64), primary_key=True, default=generate_id)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    serial_number = db.Column(db.String(64), index=True)
    discount = db.Column(db.Float)
    unit_price = db.Column(db.Float)
    total_price = db.Column(db.Float)
    hs_code = db.Column(db.String(32))
    freight = db.Column(db.Float)
    delivery_time = db.Column(db.String(32))
    weight = db.Column(db.Float)
    quote_number = db.Column(db.String(64), db.ForeignKey('quotes.quote_number'))


