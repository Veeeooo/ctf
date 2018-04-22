#-*- coding:utf-8 -*-
#!usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'ctf'
USERNAME = 'viman'
PASSWORD = '456852li'
# DB_URI的格式：dialect（mysql/sqlite）+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,
                                                              PASSWORD,
                                                              HOSTNAME,
                                                              PORT,
                                                              DATABASE
                                                              )
engine = create_engine(DB_URI,echo=False)
Session = sessionmaker(bind=engine)
dbSession = Session()
Base = declarative_base(engine)

# connection = engine.connect()
# result = connection.execute('select 1')
# print result.fetchone()