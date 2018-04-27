#-*- coding:utf-8 -*-
#!usr/bin/python3
from handlers.base.base_handler import BaseHandler
from libs.account.account_lib import create_captcha_img,auth_captcha,login,register

class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('account/auth_login.html')
    def post(self, *args, **kwargs):
        name = self.get_argument('name', '')
        password = self.get_argument('password', '')
        code = self.get_argument('code', '')
        captcha = self.get_argument('captcha', '')
        print name, password, code, captcha
        result = auth_captcha(self, captcha, code)

        if result['status'] is False:
            return self.write({'status': 400, 'msg': result['msg']})

        result = login(self, name, password)

        if result['status'] is True:
            return self.write({'status': 200, 'msg': result['msg']})
        return self.write({'status': 400, 'msg': result['msg']})



class RegisterHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('account/auth_regist.html')

    def post(self, *args, **kwargs):
        name = self.get_argument('name','')
        password1 = self.get_argument('password1','')
        password2 = self.get_argument('password2','')
        captcha = self.get_argument('captcha','')
        code = self.get_argument('code','')
        agree = self.get_argument('agree','')
        print name,password1,password2,captcha,code,type(str(agree))

        result = auth_captcha(self, captcha, code)
        if result['status'] is False:
            return self.write({'status': 400, 'msg': result['msg']})


        ##用户注册
        result = register(self, name, password1, password2)
        if result['status'] is True:
            return self.write({'status': 200, 'msg': result['msg']})
            # return self.redirect('/auth/user_login')
        return self.write({'status': 400, 'msg': result['msg']})

class CaptchaHandler(BaseHandler):
    def get(self, *args, **kwargs):
        pre_code = self.get_argument('pre_code','')
        code = self.get_argument('code','')
        img = create_captcha_img(self,pre_code,code)  ##接受返回的验证码图片
        # img = create_captcha_img(pre_code,code)
        self.set_header('Content-Type','image/jpg')
        self.write(img)

class LogoutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        print self.session.get('user_name')
        self.clear_cookie("PYCKET_ID")
        self.redirect('/user_login')


