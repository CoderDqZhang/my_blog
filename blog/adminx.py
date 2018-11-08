# -*- coding: utf-8 -*-
# encoding=utf8
import sys
import importlib
importlib.reload(sys)  

import xadmin
import xadmin.views as xviews
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _
from blog.blog_model.account import Account
from blog.blog_model.blog import Blog,Category,Comment,Tag
from django.forms import widgets
from my_blog import settings
from xadmin.views.base import ModelAdminView, filter_hook, csrf_protect_m
from mdeditor.widgets import MDEditorWidget

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    enable_themes = True
    site_title = "个人博客后台管理"
    site_footer = "个人博客后台管理"
    # menu_style = 'accordion'

    # 菜单设置

    def get_site_menu(self):
        return (

            {'title': '数据类型', 'perm': self.get_model_perm(Account, 'change'), 'menus': (
                {'title': '用户管理', 'icon': 'fa fa-user'
                    , 'url': self.get_model_url(Account, 'changelist')},
                {'title': '博客管理', 'icon': 'fa fa-vimeo-square'
                    , 'url': self.get_model_url(Blog, 'changelist')},
                {'title': '分类管理', 'icon': 'fa fa-vimeo-square'
                    , 'url': self.get_model_url(Category, 'changelist')},
                {'title': '标签管理', 'icon': 'fa fa-vimeo-square'
                    , 'url': self.get_model_url(Tag, 'changelist')},
                {'title': '评论管理', 'icon': 'fa fa-vimeo-square'
                    , 'url': self.get_model_url(Comment, 'changelist')},
            )},

        )

class AccountAdmin(object):
    list_display = ('user','nickname','openid','avatar','createTime'
                    ,'gender','phone',)

    relfield_style = 'fk_ajax'

class BlogAdmin(object):
    list_display = ('title','content','category','tag',)

class CategoryAdmin(object):
    list_display = ('name',)


class TagAdmin(object):
    list_display = ('name',)

class CommentAdmin(object):
    list_display = ()

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(Account, AccountAdmin)

xadmin.site.register(xviews.BaseAdminView, BaseSetting)
xadmin.site.register(xviews.CommAdminView, GlobalSettings)



