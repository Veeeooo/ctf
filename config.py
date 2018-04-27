#-*- coding:utf-8 -*-
#!usr/bin/python3
from libs.flash.flash_lib import get_flashed_messages
from libs.permission_auth.permission_interface_libs import menu_permission
from libs.add_num.add_num_libs import add_nums
from libs.get_time.get_times_libs import get_times
from libs.comfire.comfire_libs import match_c

settings = dict(
    template_path = 'templates',
    static_path = 'static',
    debug = True,
    cookie_secret = '123456',
    login_url = '/user_login',
    xsrf_cookies = True,
    ui_methods = {
        'menu_permission':menu_permission,
        'get_flashed_messages':get_flashed_messages,
        'get_total':add_nums,
        'get_time':get_times,
        'match_c':match_c
    },
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

