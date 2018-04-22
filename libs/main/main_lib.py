#-*- coding:utf-8 -*-
#!usr/bin/python3

from models.article.article_model import Article,ArticleToTag,Tag,Category,Comment,UserLikeArticle,SecondComment
def get_article_lib(self):
    articles = Article.all_createtime_desc()
    categorys = Category.all()
    tags = Tag.all()
    return articles,categorys,tags