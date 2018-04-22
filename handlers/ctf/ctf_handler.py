#-*- coding:utf-8 -*-
#!usr/bin/python3

from handlers.base.base_handler import BaseHandler
class EnterHandler(BaseHandler):
    def get(self, *args, **kwargs):
        if self.session.get('user_name'):
            return self.render('ctf/ctf_game.html')
        return self.render('ctf/ctf_register.html')

