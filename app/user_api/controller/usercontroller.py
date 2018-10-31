# encoding: utf-8
from flask import Flask, render_template, Blueprint, current_app, request, session, redirect, url_for, make_response
import config
from app.user_api.dao.models import UserDao
from exts import db
import hashlib
from app.utils.captcha import Captcha
from io import BytesIO
from app.utils import xjson

usercontroller = Blueprint('usercontroller', __name__)


@usercontroller.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        phone_user = request.form.get('phone_user')
        pwd_temp = hashlib.md5(request.form.get('password_user').encode("utf8"))  # MD5加密
        password = pwd_temp.hexdigest()  # MD5加密
        user = UserDao.query.filter(UserDao.phone_user == phone_user, UserDao.password_user == password).first()
        if user:
            session['phone_user'] = phone_user
            session['company_user'] = user.company_user
            # 如果想在31天内都不需要登录 加checkbox（记住我）
            session.permanent = True
            return redirect('/companyinfo.html')
        else:
            return u'手机号码或者密码错误，请确认后再登录!'


@usercontroller.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        phone_user = request.form.get('phone_user')
        username_user = request.form.get('username_user')
        password1 = request.form.get('password_user')
        password2 = request.form.get('password1')
        company_user = request.form.get('company_user')

        # 手机号码验证，如果被注册了就不能被注册了
        user = UserDao.query.filter(UserDao.phone_user == phone_user).first()
        if user:
            return u'该手机号码已被注册，请更换手机号码！'
        else:
            if password1 != password2:
                return u'两次密码不相等，请核对后再填写！'
            else:
                pwd_temp = hashlib.md5(password1.encode("utf8"))  # MD5加密，中文字符在Python中是以unicode存在的，在hash前要求进行编码转换，是因为同一个字符串在不同的编码体系下有不同的值，为确保不发生歧义必须要进行一次显性转换
                password = pwd_temp.hexdigest()  # MD5加密

                user = UserDao(phone_user=phone_user,username_user=username_user,password_user=password, company_user=company_user)
                db.session.add(user)
                db.session.commit()
                # 如果注册成功，就让页面跳转的登陆的页面
                return redirect('/login.html')


# 保存session中用户信息的操作
@usercontroller.context_processor
def my_context_processor():
    phone_user = session.get('phone_user')
    if phone_user:
        user = UserDao.query.filter(UserDao.phone_user == phone_user).first()
        if user:
            return {'user': user}
    return {}


# 注销
@usercontroller.route('/logout')
def logout():
    session.clear()
    return redirect('/login.html')

# 生成图片验证码
@usercontroller.route('/graph_captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp


