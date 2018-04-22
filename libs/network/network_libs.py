#-*- coding:utf-8 -*-
#!usr/bin/python3

from models.article.article_model import Article,ArticleToTag,Tag,Category,Comment,UserLikeArticle,SecondComment

def get_article_lib(self,category_id):
    try:
        articles = Article.by_category(category_id)
        return articles
    except Exception as e:
        return
def get_categoryid_lib(self):
    try:
        data = Category.by_name('计算机网络')
        return data.id
    except Exception as e:
        return