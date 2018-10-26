# encoding: utf-8

# 模型文件，用来存放所有的模型

from exts import db
import time

class demandDao(db.Model):
    __tablename__ = 'demand'

    id_demand = db.Column(db.Integer, primary_key=True)
    company_demand = db.Column(db.VARCHAR(255), nullable=False)
    filler_demand = db.Column(db.VARCHAR(255), nullable=False)
    content_demand = db.Column(db.Text, nullable=False)
    detail_demand = db.Column(db.Text)
    domain_demand = db.Column(db.Text)
    type_demand = db.Column(db.Integer)
    delete_demand = db.Column(db.Integer)
    time_demand = db.Column(db.DateTime)

    def __init__(self,company_demand,filler_demand,content_demand,
                 detail_demand,domain_demand,type_demand,delete_demand):
        self.company_demand = company_demand
        self.filler_demand = filler_demand
        self.content_demand = content_demand
        self.detail_demand = detail_demand
        self.domain_demand = domain_demand
        self.type_demand = type_demand
        self.delete_demand = delete_demand
        self.time_demand = time.strftime('%Y-%m-%d %H:%M:%S')


