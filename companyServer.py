# encoding: utf-8
from flask import Flask, render_template, request, redirect, url_for, session
import config
from app.user_api.dao.models import UserDao
from app.company_api.controller.companyController import companydtail
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app) # 不能忘
app.register_blueprint(companydtail)

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


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        phone_user = request.form.get('phone_user')
        password_user = request.form.get('password_user')
        user = UserDao.query.filter(UserDao.phone_user == phone_user, UserDao.password_user == password_user).first()
        if user:
            session['phone_user'] = phone_user
            session['company_user'] = user.company_user
            # 如果想在31天内都不需要登录 加checkbox（记住我）
            session.permanent = True
            return redirect('/companyinfo.html')
        else:
            return u'手机号码或者密码错误，请确认后再登录!'


@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        phone_user = request.form.get('phone_user')
        username_user = request.form.get('username_user')
        password_user = request.form.get('password_user')
        password1 = request.form.get('password1')
        company_user = request.form.get('company_user')

        # 手机号码验证，如果被注册了就不能被注册了
        user = UserDao.query.filter(UserDao.phone_user == phone_user).first()
        if user:
            return u'该手机号码已被注册，请更换手机号码！'
        else:
            if password_user != password1:
                return u'两次密码不相等，请核对后再填写！'
            else:
                user = UserDao(phone_user=phone_user,username_user=username_user,password_user=password_user,company_user=company_user)
                db.session.add(user)
                db.session.commit()
                # 如果注册成功，就让页面跳转的登陆的页面
                return redirect(url_for('login'))


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
