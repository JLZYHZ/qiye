# encoding: utf-8
from flask import Flask, render_template, request, redirect, url_for, session
import config
from app.user_api.dao.models import UserDao

from exts import db

from app.user_api.controller.login import login
from app.demand_api.controller.demandController import demand
from app.demand_api.service.demandService import demandService
app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)  # 不能忘
app.register_blueprint(login)
app.register_blueprint(demand)

@app.route('/')
def index():
    return render_template('demandAdd.html')


@app.route('/demandAdd.html')
def demand():
    return render_template('demandAdd.html')



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
            session['password_user'] = user.password_user
            session['username_user'] = user.username_user
            # 如果想在31天内都不需要登录 加checkbox（记住我）
            session.permanent = True
            return redirect('/')
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
                user = UserDao(phone_user=phone_user, username_user=username_user, password_user=password_user,
                               company_user=company_user)
                # db.delete(user)
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


if __name__ == '__main__':
    app.run(debug=True)
