function isLogined(){
     $.ajax({
        url: 'isLogined', // form action url
        type: 'GET', // form submit method get/post

        success: function (data) {
            if(data === 'not login'){
                window.alert('账户未登陆, 这个提示要不要');
                window.location = '/login.html';
            }
        },
        error: function (e) {
            console.log(e)
        }
    });
}