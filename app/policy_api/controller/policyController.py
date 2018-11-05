# encoding: utf-8
from flask import Flask, render_template, Blueprint, current_app, request, session, redirect, url_for, abort
import config
from app.policy_api.dao.policyDao import PolicyDao
from exts import db
import hashlib

policycontroller = Blueprint('policycontroller', __name__)


@policycontroller.route('/policy.html')
def policy():
    if not session.get('phone_user'):
        return redirect('/login.html')
    else:
        policy = PolicyDao.query.all()  # filter()是查询的条件
        # if not policy:
        #     abort(404)
        return render_template('policy.html', policy=policy)    # 后面参数不能忘


@policycontroller.route('/policy-single/<id_policy>')
def policy_single(id_policy):
    if not session.get('phone_user'):
        return redirect('/login.html')
    else:
        policy_single = PolicyDao.query.filter(PolicyDao.id_policy ==id_policy).first()
        print(policy_single.content_policy.encode('unicode_escape'))
        # if not policy:
        #     abort(404)
        return render_template('policy-single.html', policy_single=policy_single)




# @policycontrollercontroller.context_processor
# def my_context_processor():
#     phone_user = session.get('phone_user')
#     if phone_user:
#         user = UserDao.query.filter(UserDao.phone_user == phone_user).first()
#         if user:
#             return {'user': user}
#     return {}
