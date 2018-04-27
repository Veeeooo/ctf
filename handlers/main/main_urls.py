#-*- coding:utf-8 -*-
#!usr/bin/python3


from main_handler import MainHandler
from handlers.ctf.ctf_urls import ctf_url
from handlers.account.account_urls import account_url
from handlers.article.article_urls import article_url
from handlers.exploit.exploit_urls import exploit_url
from handlers.network.network_urls import network_url
from handlers.permission.permission_urls import permission_url
handlers = [
    (r'/',MainHandler),

]
handlers += ctf_url  ##列表相加
handlers += account_url  ##列表相加
handlers += article_url  ##列表相加
handlers += exploit_url  ##列表相加
handlers += network_url  ##列表相加
handlers += permission_url  ##列表相加