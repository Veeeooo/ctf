#coding=utf-8

from models.permission.permission_models import (Handler,
                                                 Permission,
                                                 PermissionToRole,
                                                 Role,
                                                 UserToRole,
                                                 Menu,
                                                 )
from models.account.auth_user import User


def get_role_lib(self):
    result = Role.all()
    return result

def add_role_lib(self,name):
    try:
        ch = Role.by_name(name)
        if ch:
            return
        role = Role()
        role.name = name
        self.db.add(role)
        self.db.commit()
        return
    except:
        return


def delete_role_lib(self,id):
    try:
        ch = Role.by_id(id)
        if ch:
            self.db.delete(ch)
            self.db.commit()
            return
        return
    except:
        return


def get_user_lib(self):
    result = User.all()
    return result


def get_permission_lib(self):
    result = Permission.all()
    return result


def add_permission_lib(self,name,code):
    try:
        ch = Permission.by_name(name)
        code_ch = Permission.by_strcode(code)
        print(1)
        if ch:
            return
        if code_ch:
            return
        print(4)
        permission = Permission()
        permission.name = name
        permission.strcode = code
        self.db.add(permission)
        self.db.commit()
        return
    except:
        return

def get_menu_lib(self):
    result = Menu.all()
    return result

def add_menu_permission(self,name,id):
    ch = Menu.by_name(name)
    id = Permission.by_id(id)
    if ch:
        return
    menu = Menu()
    menu.name = name
    menu.permission = id
    self.db.add(menu)
    self.db.commit()
    return

def user_add_role_lib(self,uid,rid):
    uch = User.by_id(uid)
    rch = Role.by_id(rid)
    if uch is None:
        print(1)
        return
    if rch is None:
        print(2)
        return

    uch.roles.append(rch)
    self.db.add(uch)
    self.db.commit()
    return

def role_add_permission_lib(self,rid,pid):
    rch = Role.by_id(rid)
    pch = Permission.by_id(pid)
    if rch is None:
        return
    if pch is None:
        return
    rch.permissions.append(pch)
    self.db.add(rch)
    self.db.commit()
    return

def delete_permission_lib(self,id):
    ch = Permission.by_id(id)
    if ch is None:
        return
    self.db.delete(ch)
    self.db.commit()
    return

def delete_menu_lib(self,id):
    ch = Menu.by_id(id)
    if ch is None:
        return
    self.db.delete(ch)
    self.db.commit()
    return

