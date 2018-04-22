#-*- coding:utf-8 -*-
#!usr/bin/python3

import tornado.escape
import tornado.web
import tornado.websocket
from libs.pycket.session import SessionMixin
from libs.db.dbsession import dbSession
from libs.redis_conn.redis_connection import conn
from models.account.auth_user import User

class BaseHandler(tornado.web.RequestHandler,SessionMixin):
    def initialize(self):
        self.flashes = None
        self.db = dbSession
        self.conn = conn

    def get_current_user(self):
        username = self.session.get('user_name')
        user = None
        if username:
            user = User.by_name(username)
        return user if user else None

    def on_finish(self):
        self.db.close()