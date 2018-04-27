#-*- coding:utf-8 -*-
#!usr/bin/python3

from handlers.base.base_handler import BaseHandler
from libs.main import main_lib
import tornado.web
class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        articles,categorys,tags = main_lib.get_article_lib(self)
        kw = {
            'articles':articles,
            'newarticles': articles[:3],
            'categorys':categorys,
            'tags':tags,
        }
        self.render('article/article_list.html',**kw)

