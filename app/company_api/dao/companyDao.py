# encoding: utf-8

# 模型文件，用来存放所有的模型

from exts import db
from datetime import date

class Company(db.Model):
    __tablename__ = 'company'
    code_company = db.Column(db.String(255), primary_key=True)
    name_company = db.Column(db.String(255),nullable=False)
    scope_company = db.Column(db.String,nullable=True)
    industry_company = db.Column(db.String(255),nullable=True)
    stuffnum_company = db.Column(db.String(255), nullable=True)
    registeredcaptial_company = db.Column(db.String(255), nullable=True)
    createdtime_company = db.Column(db.Date, nullable=True)
    contactname_company = db.Column(db.String(255), nullable=True)
    contactphone_company = db.Column(db.String(255), nullable=True)
    address_company = db.Column(db.String(255), nullable=True)
    partner_company = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return '<Company %r>' % self.name_company
