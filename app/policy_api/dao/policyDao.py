# encoding: utf-8

# 模型文件，用来存放所有的模型
import shortuuid

from exts import db


class PolicyDao(db.Model):
    __tablename__ = 'policy'
    id_policy = db.Column(db.Integer, nullable=False, default=shortuuid.uuid)
    name_policy = db.Column(db.String(255), primary_key=True, nullable=False)
    content_policy = db.Column(db.String(20000), nullable=False)
    time_policy = db.Column(db.String(255), nullable=False)
    department_policy = db.Column(db.String(255), nullable=False)
    overview_policy = db.Column(db.String(10000), nullable=False)
