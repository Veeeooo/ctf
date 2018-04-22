function get_cookie(name) {
    var xsrf_cookies = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return xsrf_cookies[1];
}


    $(document).ready(function (){
        $('#submit_tag').click(function () {
            event.preventDefault();
            // alert(category_name);
            // alert($('#tag_name').val());
            $.ajax({
                'url': '/article/add_category_tag',
                'type': 'POST',
                'data': {
                    'tag_name': $('#tag_name').val()
                },
                'headers': {
                    "X-XSRFTOKEN": get_cookie("_xsrf")
                },
                'success': function (data) {
                    if (data['status'] == 200) {
                        // alert('tag1');
                        swal({
                                'title': '正确',
                                'text': data['msg'],
                                'type': 'success',
                                'showCancelButton': false,
                                'showConfirmButton': false,
                                'timer': 1000
                            }, function () {
                                window.location = '/article/add_category_tag';
                            }
                        );
                    } else {
                        // alert('tag2');
                        swal({
                                'title': '错误',
                                'text': data['msg'],
                                'type': 'error',
                                'showCancelButton': false,
                                'showConfirmButton': false,
                                'timer': 1000
                            }
                        )
                    }
                }
            })
        })
     });

    $(document).ready(function (){
        $('#submit_category').click(function () {
            event.preventDefault();
            // alert(category_name);
            // alert($('#content').val());
            $.ajax({
                'url': '/article/add_category_tag',
                'type': 'POST',
                'data': {
                    'category_name': $('#content').val()
                },
                'headers': {
                    "X-XSRFTOKEN": get_cookie("_xsrf")
                },
                'success': function (data) {
                    if (data['status'] == 200) {
                        // alert('ok');
                        swal({
                                'title': '正确',
                                'text': data['msg'],
                                'type': 'success',
                                'showCancelButton': false,
                                'showConfirmButton': false,
                                'timer': 1000
                            }, function () {
                                window.location = '/article/add_category_tag';
                            }
                        );
                    } else {
                        // alert('bad');
                        swal({
                                'title': '错误',
                                'text': data['msg'],
                                'type': 'error',
                                'showCancelButton': false,
                                'showConfirmButton': false,
                                'timer': 1000
                            }
                        )
                    }
                }
            })
        })
     });

