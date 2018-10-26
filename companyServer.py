# encoding: utf-8
from flask import Flask, render_template
import config
from exts import db

from app.company_api.controller.companyController import companydtail
from app.user_api.controller.usercontroller import usercontroller
from app.demand_api.controller.demandController import demand

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app) # 不能忘
app.register_blueprint(usercontroller)
app.register_blueprint(companydtail)
app.register_blueprint(demand)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index1():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
