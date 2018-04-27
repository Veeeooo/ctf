#coding=utf-8
from models.flag.ctf_flag import Flag,Challenge,Category,UserToChallenge
from models.account.auth_user import User
from libs.flash.flash_lib import flash
def add_challenge(self,title,flag,scoure,category,name,id):
    t = Challenge.by_title(title)
    n = Challenge.by_name(name)
    if id != '':
        t = Challenge.by_id(id)
    else:
        if t is not None or n is not None:
            return {'status': False}
        t = Challenge()
    t.title = title
    t.name = name
    t.source = scoure
    t.c_id = category
    self.db.add(t)
    self.db.commit()
    if add_flag(self,flag,title,id) is True:
        return {'status':True}
    else:
        return {'status':False}


def get_categorys(self):
    return Category.all()

def add_flag(self,flag,title,id):
    f = Flag.by_flag(flag)
    # print(id,123)
    print(f)
    if id != '':
        ch = Flag.by_cid(id)
        print(123)
        if ch:
            ch.flag = flag
            self.db.add(ch)
            self.db.commit()
            return True
        return False
    else:
        t = Challenge.by_title(title)
        if t:
            if f:
                return {'status': False}
            f = Flag()
            f.flag = flag
            f.c_id = t.id
            self.db.add(f)
            self.db.commit()
            return True
        return False


def get_title_source_lib(self):
    c = Challenge.all()
    return c

def get_title_lib(self,id):
    t = Challenge.by_id(id)
    return t

def get_flag_lib(self,answer,id,uid):
    try:
        if answer == '':
            print('bad')
            flash(self, '回答错误', 'error')
            return
        if id == '':
            flash(self, '回答错误', 'error')
            return
        print(id,'***')
        f = Flag.by_cid(id)
        print(f)
        if answer == f.flag:
            u = User.by_id(uid)
            if u:
                cu = UserToChallenge()
                cu.c_id = id
                cu.u_id = uid
                self.db.add(cu)
                self.db.commit()
                flash(self, '回答正确', 'success')
                return
        else:
            flash(self, '回答错误', 'error')
            return
    except:
        flash(self, '回答正确', 'success')
        return

def get_all_title_lib(self):
    return Challenge.all()

def get_user_time_lib(self,id):
    time = UserToChallenge.by_cid(id)
    # print(time.time)
    c = Challenge.by_id(id)
    return c.user,time

def get_user_lib(self):
    user = User.all()
    li = []
    for u in user:
        source = get_source_lib(self,u.id)
        li.append(source)
    return user,li

def get_source_lib(self,id):
    u = User.by_id(id)
    return u.challenge

def get_self_data_lib(self):
    print(self.current_user.id)
    u = User.by_id(self.current_user.id)
    print(u.challenge)   ###当前用户的所回答的题目
    t = UserToChallenge.by_uid(self.current_user.id)
    return u.challenge,t

def get_title_data_lib(self,id):
    # print(Challenge.by_id(id).title)   ###题目
    # print(Challenge.by_id(id).name)   ###标题
    # print(Challenge.by_id(id).source)   ###分数
    # print(Challenge.by_id(id).c_id)
    # print(Challenge.by_id(id).flag)
    return Challenge.by_id(id)

def delete_title_libs(self,id):
    ch = Challenge.by_id(id)
    f = Flag.by_cid(id)
    print(f,'**',ch)
    if ch:
        self.db.delete(ch)
        self.db.delete(f)
        self.db.commit()
        return
    else:
        return

def get_cid(self):
    id = Challenge.all()
    print(id)