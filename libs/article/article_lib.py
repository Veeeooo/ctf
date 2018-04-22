#-*- coding:utf-8 -*-
#!usr/bin/python3

from models.article.article_model import Article,ArticleToTag,Tag,Category,Comment,UserLikeArticle,SecondComment

def article_info_libs(self,id):
    article = Article.by_id(id)
    return article

def get_tags_categorys(self):
    categorys = Category.all()
    tags = Tag.all()
    return categorys,tags

def get_article_lib(self):
    articles = Article.all_createtime_desc()
    categorys,tags = get_tags_categorys(self)
    return articles,categorys,tags

def add_article_lib(self,title,content,desc,category_id,thumbnail,tags,article_id):
    if category_id == '' or tags == []:
        return {'status':False,'msg':'请选择分类或标签'}

    if title == '' or content == '' or desc == '':
        return {'status':False,'msg':'请输入标题、内容、摘要'}

    if article_id != '':
        article = Article.by_id(article_id)
        article.tags = []
    else:
        article = Article()
    article.title = title
    article.content = content
    article.desc = desc
    article.category_id = category_id
    article.thumbnail = thumbnail
    for tags_id in tags:
        tag = Tag.by_id(tags_id)
        article.tags.append(tag)
    article.user_id = self.current_user.id
    self.db.add(article)
    self.db.commit()
    if article_id != '':
        return {'status': True, 'msg': '文档修改成功！'}
    return {'status':True,'msg':'文档提交成功！'}

def get_all_article_lib(self):
    articles = Article.all()
    return articles
def delete_article_lib(self,id):
    article = Article.by_id(id)
    if article is None:
        return Article.all()

    self.db.delete(article)
    self.db.commit()
    return Article.all()

def article_modify_lib(self,id):
    article = Article.by_id(id)
    category, tags = get_tags_categorys(self)
    return article, category, tags


def add_category_lib(self,name):
    category = Category.by_name(name)
    if category is not None:
        return {'status':False,'msg':'该分类名已存在'}

    category = Category()
    category.name = name
    self.db.add(category)
    self.db.commit()
    return {'status':True,'msg':'分类添加成功'}


def add_tag_lib(self,name):
    tag = Tag.by_name(name)
    if tag is not None:
        return {'status':False,'msg':'该标签名已存在'}

    tag = Tag()
    tag.name = name
    self.db.add(tag)
    self.db.commit()
    return {'status':True,'msg':'标签添加成功'}

def delete_tag_lib(self,id):
    tags = Tag.by_id(id)
    categorys = Category.all()
    if tags is None:
        return categorys, Tag.all()

    self.db.delete(tags)
    self.db.commit()
    return categorys, Tag.all()

def delete_category_lib(self,id):
    categorys = Category.by_id(id)
    tags = Tag.all()
    if categorys is None:
        return Category.all(), tags

    self.db.delete(categorys)
    self.db.commit()
    return Category.all(), tags

def article_search_lib(self,tag_id,category_id):
    if tag_id == '':
        articles = Article.by_category(category_id)
        tags, categorys = get_tags_categorys(self)
        return articles, categorys, tags

    articles = Article.by_tag(tag_id)
    tags, categorys = get_tags_categorys(self)
    return articles, categorys, tags



