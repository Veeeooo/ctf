#-*- coding:utf-8 -*-
#!usr/bin/python3
# from libs.flash.flash_lib import get_flashed_messages
# from libs.permission.permission_auth.permission_interface_libs import menu_permission


settings = dict(
    template_path = 'templates',
    static_path = 'static',
    debug = True,
    cookie_secret = '123456',
    login_url = '/user_login',
    xsrf_cookies = True,
    # ui_methods = {
    #     'menu_permission':menu_permission,
    #     'get_flashed_messages':get_flashed_messages
    # },
    pycket = {
        'engine':'redis',
        'storage':{
            'host':'127.0.0.1',
            'port':6379,
            'db_sessions':6,
            'db_notifications':11,
            'max_connections':2**31,
        },
        'cookies':{
            'expires_days':30,
        },
    },
)

