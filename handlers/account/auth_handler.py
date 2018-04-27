#coding=utf-8

from handlers.base.base_handler import BaseHandler
from libs.account import account_lib
import tornado.web
class AuthProfileHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        article = account_lib.get_article(self)
        user = account_lib.get_user_detail(self)
        kw = {
            'article':article,
            'current_user':self.current_user,
            'user':user,
        }
        self.render('auth/auth_profile.html',**kw)

class EditDetailHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):

        kw = {
            'current':self.current_user,
        }
        self.render('auth/Personal.html',**kw)

    def post(self, *args, **kwargs):
        kw = {
            'current': self.current_user,
        }
        name = self.get_argument('nickname','')
        qq = self.get_argument('qq','')
        email = self.get_argument('email','')
        mobile = self.get_argument('mobile','')
        aboutme = self.get_argument('aboutme','')
        result = account_lib.edit_detail(self,name,qq,email,mobile,aboutme)
        if result['status'] is True:
            self.render('auth/Personal.html',**kw)
        self.render('auth/Personal.html',**kw)



class UploadAvatarHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        kw = {
            'current': self.current_user,
        }
        data = self.request.files.get('avatar','')
        if data == '':
            return self.render('auth/Personal.html',**kw)
        result = account_lib.account_avatar_lib(self,data[0]['body'])
        if result['status'] is True:
            self.redirect('/edit_detail')
        return self.render('auth/Personal.html', **kw)