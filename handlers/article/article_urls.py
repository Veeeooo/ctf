#-*- coding:utf-8 -*-
#!usr/bin/python3


from handlers.article.article_handler import (ArticleHandler,AddArticleHandler,
                                              ArticleModifyManageHandler,
                                              DeleteArticleHandler,
                                              ArticleModifyHandler,
                                              AddCategoryTagHandler,
                                              DeleteTagHandler,
                                            DeleteCategoryHandler,SearchHandler
                                              )

article_url = [
    (r'/article/article',ArticleHandler),
    (r'/article/add_article', AddArticleHandler),
    (r'/article/article_modify_manage', ArticleModifyManageHandler),
    (r'/article/article_delete', DeleteArticleHandler),
    (r'/article/article_modify', ArticleModifyHandler),
    (r'/article/add_category_tag', AddCategoryTagHandler),
    (r'/article/delete_tag', DeleteTagHandler),
    (r'/article/delete_category', DeleteCategoryHandler),
    (r'/article/search', SearchHandler),
]