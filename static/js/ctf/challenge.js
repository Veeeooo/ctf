function get_cookie(name) {
                var xsrf_cookies = document.cookie.match("\\b" + name + "=([^;]*)\\b");
                return xsrf_cookies[1]
            }
            function DoAjax(val) {
    // alert(val)
                $.ajax({
                    url: "/ctf/index",//调用的是这个url对应的那个Handler
                    type: "GET",//Post方法
                    data: {dat: val},//要往服务器传递的数据
                    'headers': {
                        "X-XSRFTOKEN": get_cookie("_xsrf")
                    },
                    success: function (arg) {//成功从服务端获取到值，参数arg表示从服务端的Handler获取的数据
                        var obj = jQuery.parseJSON(arg);//获取的数据一般为json格式，用这个方法来解析数据
                        console.log(obj.status);
                        console.log(obj.message);
                        console.log(obj.data);
                    },
                    error: function () {//获取失败
                        console.log("failed");
                    }
                });
            }