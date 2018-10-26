# encoding: utf-8
from flask import Blueprint

login = Blueprint('login', __name__)


@login.route('/gggg')
def index():
    return 'HHHHHHHHHHHHH'


