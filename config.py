# encoding: utf-8

# 存储配置

import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'web'
USERNAME = 'root'
PASSWORD = ''
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False    #  不跟踪修改