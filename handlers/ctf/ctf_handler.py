#-*- coding:utf-8 -*-
#!usr/bin/python3

from handlers.base.base_handler import BaseHandler
from libs.ctf import ctf_libs
from libs.flash.flash_lib import flash
class EnterHandler(BaseHandler):
    def get(self, *args, **kwargs):
        if self.session.get('user_name'):
            challenge = ctf_libs.get_title_source_lib(self)
            kw = {
                'uid':self.current_user.id,
                'challenges':challenge,
            }
            return self.render('ctf/ctf_game.html',**kw)
        return self.render('ctf/ctf_register.html')


class ScoreBoardHandler(BaseHandler):
    def get(self):
        solver,li = ctf_libs.get_user_lib(self)
        kw = {
            'solvers':solver,
            'source':li,
            'default':0,
        }
        return self.render('ctf/scoreboard.html',**kw)


class MyTeamHandler(BaseHandler):
    def get(self):
        title,time = ctf_libs.get_self_data_lib(self)
        ctf_libs.get_self_data_lib(self)
        kw = {
            'current_user':self.current_user,
            'title': title,
        }
        return self.render('ctf/ctf_myteam.html',**kw)


class NoticeHandler(BaseHandler):
    def get(self):
        return self.render('ctf/ctf_notice.html')


class ManageHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id','')
        print(id)
        if id != '':
            title = ctf_libs.get_title_data_lib(self,id)
            category = ctf_libs.get_categorys(self)
            kw = {
                'title':title,
                'categorys': category,
                'id':id
            }
            return self.render('ctf/ctf_edit.html',**kw)
        category = ctf_libs.get_categorys(self)
        kw = {
            'categorys':category,
        }
        return self.render('ctf/ctf_manage.html',**kw)

    def post(self, *args, **kwargs):
        id = self.get_argument('id','')
        title = self.get_argument('title','')
        flag = self.get_argument('flag','')
        scoure = self.get_argument('scoure','')
        category = self.get_argument('categoryid','')
        name = self.get_argument('name','')
        print(title,'*',flag,'*',scoure,'*',category,'*',id)
        if title == '' or flag == '' or scoure == '' or category == '':
            return self.redirect('/ctf/manage')
        result = ctf_libs.add_challenge(self,title,flag,scoure,category,name,id)
        if result['status'] is True:
            return self.redirect('/ctf/index')
        return self.redirect('/ctf/manage')

import re
class ChallengeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id', '')
        title = ctf_libs.get_title_lib(self,id)
        solver, time = ctf_libs.get_user_time_lib(self,id)
        kw = {
            'solver':solver,
            'time':time,
            'title':title,
            'demo':title.title
        }
        return self.render('ctf/input_answer.html',**kw)
    def post(self, *args, **kwargs):
        answer = self.get_argument('answer',None)
        print(answer)
        id = self.get_argument('id',None)
        uid = self.current_user.id
        print(answer,"*",id,"*",uid)
        ctf_libs.get_flag_lib(self,answer,id,uid)
        self.redirect('/ctf/challenge?id=%s'%id)

class TitleListHandler(BaseHandler):
    def get(self):
        title = ctf_libs.get_all_title_lib(self)
        kw = {
            'titles':title
        }
        return self.render('ctf/ctf_title_list.html',**kw)

class DeleteHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id','')
        ctf_libs.delete_title_libs(self,id)
        return self.redirect('/ctf/list')