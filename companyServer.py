# encoding: utf-8
from flask import Flask, render_template, request, redirect, url_for, session
import config
from app.user_api.dao.models import UserDao
from exts import db
from app.user_api.controller.usercontroller import usercontroller
from app.policy_api.controller.policyController import policycontroller
from app.company_api.controller.companyController import companydtail
from app.demand_api.controller.demandController import demand

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app) # 不能忘
app.register_blueprint(usercontroller)
app.register_blueprint(policycontroller)

app.register_blueprint(companydtail)
app.register_blueprint(demand)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index.html')
def index1():
    return render_template('index.html')



@app.errorhandler(404)
def miss(e):
    return render_template('404.html')


@app.errorhandler(500)
def err(e):

    return render_template('404.html')

@app.context_processor
def my_context_processor():
    phone_user = session.get('phone_user')
    if phone_user:
        user = UserDao.query.filter(UserDao.phone_user == phone_user).first()
        if user:
            return {'user': user}
    return {}


@app.route('/policy.html')
def policy():
    return render_template('policy.html')


if __name__ == '__main__':
    app.run(debug=True)
