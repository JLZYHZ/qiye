# encoding: utf-8
from flask import Flask, render_template, request, redirect, url_for, session
import config
from app.user_api.dao.models import UserDao
from exts import db
from app.user_api.controller.usercontroller import usercontroller
from app.policy_api.controller.policyController import policycontroller


app = Flask(__name__)
app.config.from_object(config)

db.init_app(app) # 不能忘
app.register_blueprint(usercontroller)
app.register_blueprint(policycontroller)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index.html')
def index1():
    return render_template('index.html')


@app.route('/category.html')
def category():
    return render_template('category.html')


@app.route('/about-us.html')
def about():
    return render_template('about-us.html')


@app.route('/blog-home.html')
def blogHome():
    return render_template('blog-home.html')


@app.route('/blog-single.html')
def blogSingle():
    return render_template('blog-single.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/elements.html')
def elements():
    return render_template('elements.html')


@app.route('/price.html')
def price():
    return render_template('price.html')


@app.route('/search.html')
def search():
    return render_template('search.html')


@app.route('/single.html')
def single():
    return render_template('single.html')


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
