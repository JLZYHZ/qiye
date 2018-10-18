from flask import session, render_template,Blueprint,redirect,request
from app.company_api.dao.companyDao import Company
from exts import db
from app.company_api.service.companyService import showCompanyinfo
companydtail = Blueprint('companydetail',__name__)

#点击企业信息时，没有登录的情况，调到登录界面。如果用户已经登录，直接显示公司信息
@companydtail.route('/companyinfo.html')
def companyinfo():
    phone_user = session.get('phone_user')
    if phone_user:
        company_user = session.get('company_user')
        company = showCompanyinfo(company_user)

        return render_template('companyinfo.html',company=company)


    else:
        return redirect('/login.html')


@companydtail.route('/edit',methods=['post',])
def editCompanyinfo():
    stuffnum_company = request.form.get('companynum')
    scope_company = request.form.get('companyscope')
    partner_company = request.form.get('companypartner')
    company = showCompanyinfo(session.get('company_user'))
    code_company=company.code_company
    name_company=company.name_company
    #更新语句
    db.session.query(Company).filter(code_company==code_company).update({Company.stuffnum_company:stuffnum_company,Company.scope_company:scope_company,
                                                                 Company.partner_company:partner_company})
    #这是新增语句，不对
    # company = Company(code_company=code_company,stuffnum_company=stuffnum_company,scope_company=scope_company,partner_company=partner_company)
    # db.session.add(company)
    db.session.commit()
    return "succeed"
# @companydtail.route('/succeed')
# def succeed():
#     return render_template('succeed.html')