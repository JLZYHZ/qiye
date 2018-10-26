from app.company_api.dao.companyDao import Company
from exts import db

#更新公司信息
class CompanyService:
#通过公司名字，获取公司对象
    def showCompanyinfo(companyname):

        company = Company.query.filter(Company.name_company == companyname).first()
        return company

#通过公司名字的关键字来进行模糊搜索
    def findCompanyBykeywords(keywords):
        companys = db.session.query(Company).filter(Company.name_company.like("%"+keywords+"%"))
        return companys.all()
#更新数据
    def updateCompanyinfo(code,num,scope,partner):

        db.session.query(Company).filter(Company.code_company == code).update(
            {Company.stuffnum_company: num, Company.scope_company: scope,
                Company.partner_company: partner})
        db.session.commit()
