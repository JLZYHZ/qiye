from app.company_api.dao.companyDao import Company

from exts import db

#更新公司信息

#通过公司名字，获取公司对象
def showCompanyinfo(companyname):
    company = Company.query.filter(Company.name_company == companyname).first()
    return company

