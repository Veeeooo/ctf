#-*- coding:utf-8 -*-
#!usr/bin/python3

import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.escape
from tornado.options import define,options
from config import settings
from handlers.main.main_urls import handlers
from libs.db import create_tables
from libs.db.dbsession import dbSession
from models.account.auth_user import User
from models.article.article_model import *
from models.permission.permission_models import *
from models.flag.ctf_flag import *


define('port',default=8000,help='run port',type=int)
define('runserver',default=False,help='start server',type=bool)
define('t',default=False,help='create table',type=bool)
define('u',default=False,help='create user',type=bool)

if __name__ == '__main__':
    options.parse_command_line()

    if options.t:
        create_tables.run()

    # if options.u:
    #     user = User()
    #     user.name = 'vee'
    #     user.password = '123456'
    #     dbSession.add(user)
    #     dbSession.commit()

    if options.runserver:
        app = tornado.web.Application(handlers,**settings)
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(options.port)
        print 'start server'
        tornado.ioloop.IOLoop.instance().start()