# encoding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for, session, Response, make_response,json,jsonify
from app.demand_api.service.demandService import demandService
from app.utils import utilszjl
demand = Blueprint('demand', __name__)



@demand.route('/submittedController', methods=['GET'])
def submittedController():
    ajax={}
    if not session.get('phone_user'):
        ajax['success'] = False
        ajax['msg'] = 'not login'
    else:
        # 获取公司和填写人
        company_demand = session.get('company_user')
        filler_demand = session.get('phone_user')
        demands = demandService.selectDemand(company_demand, filler_demand)
        if demands==False:
            ajax['success'] = False
            ajax['msg'] = 'server false'
        else:

            ajax['success'] = True
            ajax['msg'] = 'true'
    return json.jsonify(ajax)

@demand.route('/demandAdd.html')
def demandAdd():
    if not session.get('phone_user'):
        return redirect('/login.html')
    else:
        return render_template('demandAdd.html')

@demand.route('/demandShow.html')
def demandShow():
    if not session.get('phone_user'):
        return redirect('/login.html')
    else:
        return render_template('demandShow.html')

@demand.route('/demandSelController', methods=['GET', 'POST'])
def demandSelController():
    if request.method == 'GET':
        company_demand = session.get('company_user')
        filler_demand = session.get('phone_user')
        lstDemands = []
        demands = demandService.selectDemand(company_demand, filler_demand)
        for demand in demands:
            d = {}
            d['id_demand'] = demand.id_demand
            d['company_demand'] = demand.company_demand
            d['filler_demand'] = demand.filler_demand
            d['content_demand'] = demand.content_demand
            d['detail_demand'] = demand.detail_demand
            d['domain_demand'] = demand.domain_demand
            d['type_demand'] = utilszjl.transformNum2Word(demand.type_demand)
            d['time_demand'] = str(demand.time_demand)
            lstDemands.append(d)
        result = json.dumps(lstDemands)

        return result
    else:
        print('demandController第28行')

@demand.route('/demandAddController', methods=['GET', 'POST'])
def demandAddController():
    if not session.get('phone_user'):
        return 'not login'
    else:
        company_demand = session.get('company_user')
        filler_demand = session.get('phone_user')
        type_demand = request.form.get('type_demand')
        content_demand = request.form.get('content_demand')
        detail_demand = request.form.get('detail_demand')
        domain_demand = request.form.get('others')
        if content_demand.strip()=='' and detail_demand.strip() == '':
            return 'content is null'
        if domain_demand.strip() == '':
            return 'domain is null'
        if request.method == 'POST':
            isOk = demandService.addDemand(company_demand,filler_demand,content_demand,
                                           detail_demand,domain_demand,type_demand)
            if isOk:
                return 'true'
            else:
                return 'server false'

@demand.route('/demandDelController')
def demandDelController():
    ajax = {}
    if not session.get('phone_user'):
        ajax['success'] = False
        ajax['msg'] = 'not login'
    else:
        id_demand = request.args.get('id_demand')
        isDelete = demandService.deleteDemand(id_demand)
        if isDelete == False:
            ajax['success'] = False
            ajax['msg'] = 'server false'
        else:
            ajax['success'] = True
            ajax['msg'] = 'true'

    return json.jsonify(ajax)