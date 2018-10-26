from flask import session, render_template,Blueprint,redirect,request,json
from app.company_api.service.companyService import CompanyService

companydtail = Blueprint('companydetail',__name__)

#点击企业信息时，没有登录的情况，调到登录界面。如果用户已经登录，直接显示公司信息
@companydtail.route('/companyinfo.html')
def companyinfo():
    phone_user = session.get('phone_user')
    if phone_user:
        company_user = session.get('company_user')
        company = CompanyService.showCompanyinfo(company_user)
        return render_template('companyinfo.html', company=company)
    else:
        return redirect('/login.html')


@companydtail.route('/edit',methods=['post',])
def editCompanyinfo():
    ajax={}
    stuffnum_company = request.form.get('companynum')
    scope_company = request.form.get('companyscope')
    partner_company = request.form.get('companypartner')
    company = CompanyService.showCompanyinfo(session.get('company_user'))
    code_company=company.code_company
    #更新语句
    try:
        CompanyService.updateCompanyinfo(code_company,stuffnum_company,scope_company,partner_company)
        ajax['success']=True
        ajax['msg'] = '更新成功'
    except:
        ajax['success'] = False
        ajax['msg'] = '服务器错误'
    return json.jsonify(ajax)

@companydtail.route('/searchcompany',methods=['post'])
def searchcompany():

    session['search'] = request.form.get('search')
    return '搜索'


@companydtail.route('/result.html')
def result():

    key_words = session.get('search')
    companys=CompanyService.findCompanyBykeywords(key_words)

    if companys:
        return render_template('/result.html',company=companys)
    else:
        return "没有相关公司的信息"

