#-*- coding:utf-8 -*-
#!usr/bin/python3

from handlers.base.base_handler import BaseHandler
from libs.network import network_libs
class NetWorkHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = network_libs.get_categoryid_lib(self)
        articles = network_libs.get_article_lib(self,id)
        kw={
            'articles': articles,
        }
        self.render('network/network.html', **kw)