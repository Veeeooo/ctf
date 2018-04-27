#coding=utf-8

from libs.perimission import permission_libs
from handlers.base.base_handler import BaseHandler

class AddPermissionHandler(BaseHandler):
    def get(self, *args, **kwargs):
        permission = permission_libs.get_permission_lib(self)
        kw = {
            'permissions':permission
        }
        self.render('permission/permissions_add.html',**kw)

    def post(self, *args, **kwargs):
        name = self.get_argument('name','')
        code = self.get_argument('strcode','')
        if name == '' or code == '':
            return self.redirect('/permission/add_permission')
        permission_libs.add_permission_lib(self,name,code)
        return self.redirect('/permission/add_permission')


class AddMenuPemissionHandler(BaseHandler):
    def get(self, *args, **kwargs):
        menu = permission_libs.get_menu_lib(self)
        permissions = permission_libs.get_permission_lib(self)
        kw = {
            'menus':menu,
            'permissions':permissions
        }
        self.render('permission/menu_permission_add.html',**kw)
    def post(self, *args, **kwargs):
        name = self.get_argument('name','')
        permissionid = self.get_argument('permissionid','')
        if name == '' or permissionid == '':
            return
        permission_libs.add_menu_permission(self,name,permissionid)
        return self.redirect('/permission/add_menu_permission')

class PermissionListHandler(BaseHandler):
    def get(self, *args, **kwargs):
        users = permission_libs.get_user_lib(self)
        kw = {
            'users':users,

        }
        self.render('permission/permission_list.html',**kw)

class AddRoleHandler(BaseHandler):
    def get(self, *args, **kwargs):
        role = permission_libs.get_role_lib(self)
        kw = {
            'roles':role
        }
        self.render('permission/add_role.html',**kw)
    def post(self, *args, **kwargs):
        name = self.get_argument('name','')
        if name == '':
            return self.redirect('/permission/add_role')
        permission_libs.add_role_lib(self,name)
        self.redirect('/permission/add_role')

class DeleteRoleHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id','')
        if id == '':
            return self.redirect('/permission/add_role')
        permission_libs.delete_role_lib(self,id)
        self.redirect('/permission/add_role')

class UserAddRoleHandler(BaseHandler):
    def get(self, *args, **kwargs):
        role = permission_libs.get_role_lib(self)
        user = permission_libs.get_user_lib(self)
        kw = {
            'users':user,
            'roles':role,
            'permissions':[]
        }
        self.render('permission/user_add_role.html',**kw)
    def post(self, *args, **kwargs):
        u_id = self.get_argument('userid','')
        r_id = self.get_argument('roleid','')
        if u_id == '' or r_id == '':
            print('x')
            return
        permission_libs.user_add_role_lib(self,u_id,r_id)
        return  self.redirect('/permission/user_add_role')

class RoleAddPermissionHandler(BaseHandler):
    def get(self, *args, **kwargs):
        roles = permission_libs.get_role_lib(self)
        permissions = permission_libs.get_permission_lib(self)
        users = permission_libs.get_user_lib(self)
        kw = {
            'roles':roles,
            'permissions':permissions,
            'users':users
        }
        self.render('permission/role_add_permission.html',**kw)

    def post(self, *args, **kwargs):
        rid = self.get_argument('roleid','')
        pid = self.get_argument('permissionid','')
        if rid == '' or pid == '':
            return
        permission_libs.role_add_permission_lib(self,rid,pid)
        return self.redirect('/permission/role_add_permission')

class DeletePermissionHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id','')
        if id == '':
            return
        permission_libs.delete_permission_lib(self,id)
        return self.redirect('/permission/add_permission')

class DeleteMenuHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id','')
        if id == '':
            return
        permission_libs.delete_menu_lib(self,id)
        return self.redirect('/permission/add_menu_permission')