#-*- coding:utf-8 -*-
#!usr/bin/python3


from account_handler import LoginHandler,RegisterHandler,CaptchaHandler,LogoutHandler
from auth_handler import AuthProfileHandler,EditDetailHandler,UploadAvatarHandler
account_url = [
    (r'/user_login',LoginHandler),
    (r'/user_register',RegisterHandler),
    (r'/auth/captcha',CaptchaHandler),
    (r'/logout',LogoutHandler),

    (r'/personal',AuthProfileHandler),
    (r'/edit_detail',EditDetailHandler),
    (r'/account/avatar',UploadAvatarHandler),

]