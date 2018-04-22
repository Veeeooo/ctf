
//获取cookie
function get_cookie(name) {
    var xsrf_cookies = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return xsrf_cookies[1];
}

$(function () {
   var obtn = $('#submit_register');
   $('#agree').change(function () {
       var that = $(this);
       that.prop("checked",that.prop("checked"));
       if(that.prop("checked")){
            obtn.prop("disabled",false)
        }else{
            obtn.prop("disabled",true)
        }
   })
});
//注册用户函数
$(document).ready(function(){
    get_image_code();

    //点击获取图形验证码
    $('#a_code').click(function () {
        get_image_code();
    });

});
$("#submit_register").click(function (event) {
    event.preventDefault();
    $.ajax({
        'url':'/user_register',
        'type':"post",
        'data':{
            'name':$('#name').val(),
            'password1':$('#password1').val(),
            'password2':$('#password2').val(),
            'captcha':$('#captcha').val(),
            'code':$('#code').val(),
            'agree':$('#agree').val()
        },
        'headers':{
                 "X-XSRFTOKEN":get_cookie("_xsrf")
            },
        'success': function (data) {
            if (data['status'] == 200) {
                swal({
                    'title': '正确',
                    'text': data['msg'],
                    'type': 'success',
                    'showCancelButton': false,
                    'showConfirmButton': false,
                    'timer': 1500,
                    'closeOnConfirm': false
                }, function () {
                    window.location = '/user_login';
                });
            } else {
                swal({
                    'title': '错误',
                    'text': data['msg'],
                    'type': 'error',
                    'showCancelButton': false,
                    'showConfirmButton': false,
                    'timer': 1500
                });
                get_image_code();
            }
        }
    })
});


