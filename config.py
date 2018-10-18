# encoding: utf-8

# 存储配置

import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOSTNAME = '10.6.11.61'
PORT = '3306'
DATABASE = 'web'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False    #  不跟踪修改