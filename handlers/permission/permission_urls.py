#coding=utf-8
from handlers.permission.permission_handler import AddMenuPemissionHandler,AddPermissionHandler,PermissionListHandler,\
        AddRoleHandler,DeleteRoleHandler,UserAddRoleHandler,RoleAddPermissionHandler,DeletePermissionHandler,DeleteMenuHandler
permission_url=[
        (r'/permission/add_permission', AddPermissionHandler),
        (r'/permission/add_menu_permission', AddMenuPemissionHandler),
        (r'/permission/permission_list', PermissionListHandler),
        (r'/permission/add_role', AddRoleHandler),
        (r'/permission/del_role', DeleteRoleHandler),
        (r'/permission/user_add_role', UserAddRoleHandler),
        (r'/permission/role_add_permission', RoleAddPermissionHandler),
        (r'/permission/del_permission', DeletePermissionHandler),
        (r'/permission/del_menu', DeleteMenuHandler),

        ]