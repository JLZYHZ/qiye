# encoding: utf-8

# 模型文件，用来存放所有的模型

from exts import db


class UserDao(db.Model):
    __tablename__ = 'user'
    phone_user = db.Column(db.String(255), primary_key=True, nullable=False)
    username_user = db.Column(db.String(255),nullable=False)
    password_user = db.Column(db.String(255),nullable=False)
    company_user = db.Column(db.String(255), nullable=False)


