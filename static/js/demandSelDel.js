$(function () {
    $('#demandsTable').bootstrapTable({
        url: 'demandSelController',  // 请求数据源的路由
        method: 'GET',
        pagination: true, //前端处理分页
        search: true, //显示搜索框，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
        striped: true, //是否显示行间隔色
        strictSearch: false, //设置为 true启用 全匹配搜索，false为模糊搜索
        showColumns: true, //选择只看哪几列
        minimumCountColumns: 1, //最少要看的列数
        // height: 500,  //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
        showToggle: true, //是否显示详细视图和列表视图的切换按钮
        toolbar: '#toolbar', //工具按钮用哪个容器
        editable:true,
        columns: [
            {
                field: 'id_demand',
                title: '序号',
                align: 'center'//对齐方式，居中
            },
            {
                field: 'company_demand',
                title: '公司名',
                align: 'center'//对齐方式，居中,
            },
            {
                field: 'filler_demand',
                title: '手机号',
                align: 'center'//对齐方式，居中

            },
            {
                field: 'content_demand',
                title: '需求标题',
                align: 'center'

            },
            {
                field: 'detail_demand',
                title: '详细内容',
                align: 'center'//对齐方式，居中


            },
            {
                field: 'domain_demand',
                title: '需求领域',
                align: 'center'
            },
            {
                field: 'type_demand',
                title: '需求方向',
                align: 'center'//对齐方式，居中
            },
            {
                field: 'time_demand',
                title: '填写时间',
                align: 'center'
            },
            {
                field: 'id_demand',
                title: '操作',
                align: 'center',
                formatter: function (value, row, index) {
                    return [
                        // '<a class="edit" href="#" onclick="editDB(\'' + row.id_demand + '\')" title="编辑">',
                        // '<span class="fa fa-edit" style="font-size: 25px"></span>编辑',
                        // '</a>&nbsp;&nbsp;&nbsp;&nbsp;',
                        '<a class="remove" href="javascript:void(0)" onclick="deleteDB(\'' + row.id_demand + '\')" title="删除">',
                        '<i class="fa fa-remove" style="font-size: 25px"></i>删除',
                        '</a>'
                    ].join('');
                }
            }
        ]
    });

});

function deleteDB(id_demand){
    $.ajax({
        url:'demandDelController',
        type:'get',
        data: {id_demand:id_demand},

        success: function (data) {
            isTrue = data['success'];
            if (!isTrue) {
                if (data['msg'] === 'not login') {
                    window.alert('账户未登陆');
                    window.location = '/login.html';
                }else if(data['msg'] === 'server false'){
                    window.alert('服务器断开连接');
                }else{
                    window.alert('未知错误');
                }
            }
            else {
                $("#demandsTable").bootstrapTable('refresh');
            }

        },
        error: function (e) {
            console.log(e)
        }
    })
}

function editDB(id_demand){
    window.alert('editDB');
}
