#-*- coding:utf-8 -*-
#!usr/bin/python3

from dbsession import dbSession,Base
def run():
    print '-----start-----'
    Base.metadata.create_all()
    # Base.metadata.drop_all()
    print '-----end-----'
