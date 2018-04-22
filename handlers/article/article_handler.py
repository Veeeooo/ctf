#-*- coding:utf-8 -*-
#!usr/bin/python3

from handlers.base.base_handler import BaseHandler
from libs.article import article_lib
import json

class ArticleHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id','')
        article = article_lib.article_info_libs(self,id)
        kw = {
            'article':article
        }
        self.render('article/articles_detail.html',**kw)


class AddArticleHandler(BaseHandler):
    def get(self, *args, **kwargs):
        categorys,tags = article_lib.get_tags_categorys(self)
        kw = {
            'categorys':categorys,
            'tags':tags
        }
        self.render('article/add_article.html',**kw)

    def post(self, *args, **kwargs):
        title = self.get_argument('title', '')
        article = self.get_argument('article', '')
        desc = self.get_argument('desc', '')
        category = self.get_argument('category', '')
        thumbnail = self.get_argument('thumbnail', '')
        tags = json.loads(self.get_argument('tags', ''))
        article_id = self.get_argument('article_id', '')
        result = article_lib.add_article_lib(self, title, article, desc, category, thumbnail, tags, article_id)

        if result['status'] is True:
            return self.write({'status': 200, 'msg': result['msg']})
        return self.write({'status': 400, 'msg': result['msg']})

class ArticleModifyManageHandler(BaseHandler):
    def get(self, *args, **kwargs):
        articles = article_lib.get_all_article_lib(self)
        kw = {
            'articles':articles
        }
        self.render('article/article_modify_manage.html',**kw)

class DeleteArticleHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id','')
        articles = article_lib.delete_article_lib(self, id)
        kw = {
            'articles': articles
        }
        self.render('article/article_modify_manage.html', **kw)

class ArticleModifyHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id', '')
        article, categorys, tags = article_lib.article_modify_lib(self, id)
        kw = {
            'article': article,
            'categorys': categorys,
            'tags': tags
        }
        self.render('article/article_modify.html', **kw)

class AddCategoryTagHandler(BaseHandler):
    def get(self, *args, **kwargs):
        categorys,tags = article_lib.get_tags_categorys(self)
        kw = {
            'tags':tags,
            'categorys':categorys
        }
        self.render('article/add_category_tag.html',**kw)

    def post(self, *args, **kwargs):
        category_name = self.get_argument('category_name','')
        tag_name = self.get_argument('tag_name','')
        # print tag_name+'handlername'
        if category_name == '' and tag_name == '':
            return self.write({'status':400,'msg':'此处不能为空'})
        if tag_name == '' and category_name != '':
            result = article_lib.add_category_lib(self,category_name)
            if result['status'] is True:
                return self.write({'status': 200, 'msg': result['msg']})
            return self.write({'status': 400, 'msg': result['msg']})
        if category_name == '' and tag_name != '':
            result = article_lib.add_tag_lib(self,tag_name)
            if result['status'] is True:
                return self.write({'status': 200, 'msg': result['msg']})
            return self.write({'status': 400, 'msg': result['msg']})

class DeleteTagHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id', '')
        categorys, tags = article_lib.delete_tag_lib(self, id)

        kw = {
            'categorys': categorys,
            'tags': tags
        }
        self.render('article/add_category_tag.html', **kw)

class DeleteCategoryHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id', '')
        categorys, tags = article_lib.delete_category_lib(self, id)

        kw = {
            'categorys': categorys,
            'tags': tags
        }
        self.render('article/add_category_tag.html', **kw)


class SearchHandler(BaseHandler):
    def get(self, *args, **kwargs):
        tag_id = self.get_argument('tag_id','')
        category_id = self.get_argument('category_id','')

        articles, tags, categorys = article_lib.article_search_lib(self,tag_id,category_id)
        kw = {
            'articles': articles,
            'newarticles': articles[:3],
            'categorys': categorys,
            'tags': tags,
        }
        self.render('article/article_list.html', **kw)
