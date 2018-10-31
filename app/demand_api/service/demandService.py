from app.demand_api.dao.demandDao import demandDao
from exts import db
import time
# import config

# db.create_engine(config.DB_URI)
class demandService():
    # 对demand的增删改查
    @classmethod
    def addDemand(self, company_demand,filler_demand,content_demand,
                 detail_demand,domain_demand,type_demand=1,delete_demand=0):
        demand = demandDao(company_demand,filler_demand,content_demand,
                           detail_demand,domain_demand,type_demand, delete_demand)
        try:
            db.session.add(demand)
            db.session.commit()
            return True
        except:
            return False

    @classmethod
    def deleteDemand(self, id_demand):
        try:
            db.session.query(demandDao).filter(demandDao.id_demand==id_demand).update({demandDao.delete_demand:1,
                                                                                       demandDao.time_demand:time.strftime('%Y-%m-%d %H:%M:%S')})
            db.session.commit()
            return True
        except:
            return False
    def updateDemand(self):
        pass

    @classmethod
    def selectDemand(self, company_demand,filler_demand):
        try:
            # demandDao.delete_demand==0 只查找为删除的
            demands = db.session.query(demandDao).filter(demandDao.filler_demand==filler_demand,
                                                       demandDao.company_demand==company_demand,
                                                         demandDao.delete_demand==0).all()

            return demands
        except:
            return False