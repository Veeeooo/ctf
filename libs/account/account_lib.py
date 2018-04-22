#-*- coding:utf-8 -*-
#!usr/bin/python3
import re

from utils.captcha.captcha import create_captcha  ##生产验证码图片
from models.account.auth_user import User
from datetime import datetime
import re
from models.article.article_model import Article


def create_captcha_img(self,pre_code,code):   ### self参数是LoginHandler的，LoginHandler继承BaseHandler，获取redis的连接变量
    if pre_code:
        self.conn.delete("captcha:%s"%pre_code)
    text, img = create_captcha()   ##获取验证码文本内容和图片
    self.conn.setex('captcha:%s'%code,text.lower(),60)
    return img

def auth_captcha(self,captcha,code):
    print self.conn.get('captcha:%s' % code),'hahah',captcha
    if captcha == '':
        return {'status':False,'msg':'请输入验证码'}

    elif self.conn.get('captcha:%s'%code) != captcha:
        return {'status':False,'msg':'验证码错误'}

    return {'status':True,'msg':'正确'}


def login(self,name,password):
    if name == '' or password == '':
        return {'status':False,'msg':'请输入用户名或密码'}
    user = User.by_name(name)
    if user and user.auth_password(password):
        user.last_login = datetime.now()
        user.loginnum += 1
        self.db.add(user)
        self.db.commit()
        self.session.set('user_name',user.name)
        return {'status':True,'msg':'登录成功'}
    return {'status':False,'msg':'用户名或密码错误'}

def register(self,name,password1,password2):
    demo = re.findall(r'[A-Za-z0-9]', name)
    if demo == []:
        return {'status': False, 'msg': '请输入包含大写、小写、数字的用户名'}
    if name == '':
        return {'status': False, 'msg': '用户名不能为空'}

    if password1 == '':
        return {'status': False, 'msg': '密码不能为空'}

    if password2 == '':
        return {'status': False, 'msg': '重复密码处不能为空'}

    if password1 != password2:
        return {'status':False,'msg':'两次密码不一致'}


    user = User.by_name(name)
    if user is not None:
        return {'status':False,'msg':'该用户名已存在啦'}

    user = User()
    user.name = name
    user.password = password1
    self.db.add(user)
    self.db.commit()
    return {'status':True,'msg':'注册成功'}

def get_article(self):
    article = Article.by_userid(self.current_user.id)
    return article

def get_user_detail(self):
    data = User.by_name(self.current_user.name)
    return data

def edit_detail(self,name,qq,email,mobile,aboutme):
    if name == '':
        return {'status':False,'msg':'用户名不能为空'}
    if qq != '':
        demo = re.findall(r'[1-9][0-9]{4,14}',qq)
        if not demo:
            return {'status':False,'msg':'请输入正确的QQ号'}
    if email != '':
        demo = re.findall(r'^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$',email)
        if not demo:
            return {'status':False,'msg':'请输入正确的邮箱地址'}
    if mobile != '':
        demo = re.findall(r'^1[3|4|5|8][0-9]\d{4,8}$',mobile)
        if not demo:
            return {'status':False,'msg':'请输入正确的手机号码'}
    user = self.current_user
    user.name = name
    user.qq = qq
    user.email = email
    user.mobile = mobile
    user.signature = aboutme
    user.update_time = datetime.now()
    self.db.add(user)
    self.db.commit()
    self.session.set('user_name',user.name)
    return {'status':True,'msg':'信息修改成功'}

def account_avatar_lib(self,data):
    try:
        user = self.current_user
        user.avatar = data
        user.update_time = datetime.now()
        self.db.add(user)
        self.db.commit()
        return {'status':True}
    except Exception as e:
        return {'status':False}


