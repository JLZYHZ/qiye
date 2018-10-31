// -------   Mail Send ajax
var demandType = 0;

function isReadOnly(index, domain) {
    var input = document.getElementById("others");
    if (index === 5) {
        input.value = "";
        input.readOnly = false;
    }
    else {
        input.readOnly = true;
        input.value = domain;
    }
}

function submittedClicked() {
    $.ajax({
        url: 'submittedController', // form action url
        type: 'GET', // form submit method get/post

        success: function (data) {
            isTrue = data['success'];
            if (!isTrue) {
                if (data['msg'] === 'not login') {
                    window.alert('账户未登陆');
                    window.location = '/login.html';
                } else if (data['msg'] === 'server false') {
                    window.alert('服务器断开连接');
                } else {
                    window.alert('未知错误');
                }
            }
            else {
                window.location = '/demandShow.html';
            }

        },
        error: function (e) {
            console.log(e)
        }
    });
}

$(document).ready(function () {
    var form = $('#myForm'); // contact form
    var submit = $("button[name='submit']");
    var alert = $('.alert-msg'); // alert div for show alert message

    form.on('submit', function (e) {
        e.preventDefault();
        $.ajax({
            url: 'demandAddController', // form action url
            type: 'POST', // form submit method get/post
            data: form.serialize(), // serialize form data
            beforeSend: function () {
                alert.fadeOut();
                submit.html('SUBMITing...'); // change submit button text
            },
            success: function (data) {
                if (data === 'server false') {
                    window.alert('服务器断开连接')
                } else if (data === 'not login') {
                    window.alert('账户未登陆');
                    window.location = '/login.html';
                } else if (data === 'domain is null') {
                    window.alert('请选择相关领域');
                } else if (data === 'content is null') {
                    window.alert('需求标题和详细信息,至少填写其中一个');
                } else if (data === 'true') {
                    window.alert('提交成功!');
                    form.trigger('reset');
                } else {
                    window.alert('未知错误')
                }
                submit.html('SUBMIT')
            },
            error: function (e) {
                console.log(e)
            }
        });
    });
});

var idTypeDemand = "null";
document.onclick = function () {

    var obj = event.srcElement;
    if (obj.type === "button") {
        if (idTypeDemand !== "null") {
        var btn0 = document.getElementById(idTypeDemand);
        btn0.style.color = "#fff";
        btn0.style.fontStyle = "";
        btn0.style.fontWeight = "";
    }
        var id = obj.id;
        var btn = document.getElementById(id);
        if (id !== "btn1") {
            var btn1 = document.getElementById("btn1");
            btn1.style.color = "#fff";
            btn1.style.fontStyle = "";
            btn1.style.fontWeight = "";
        }
            btn.style.color = "#174363";
            btn.style.fontStyle = "italic";
            btn.style.fontWeight = "bold";

        // 设置隐藏的type_demand的值为点击值
        document.getElementById('type_demand').value = obj.value;
        idTypeDemand = id;
    }
};