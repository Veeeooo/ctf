#coding=utf-8

from libs.db.dbsession import dbSession
from libs.db.dbsession import Base
from sqlalchemy.orm import relationship
from uuid import uuid4
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine, Column, Integer, String,
                        Text, Boolean, Date, DateTime, ForeignKey)
from datetime import datetime
class UserToChallenge(Base):
    """用户题目多对多关系表"""
    __tablename__='user_to_challenge'
    u_id = Column(Integer,ForeignKey("user.id"), primary_key=True)
    c_id = Column(Integer,ForeignKey("title.id"), primary_key=True)
    time = Column(DateTime, default=datetime.now)

    @classmethod
    def by_uid(cls,id):
        return dbSession.query(cls).filter_by(u_id=id).first()

    @classmethod
    def by_cid(cls,id):
        return dbSession.query(cls).filter_by(c_id=id).first()

    @classmethod
    def by_uid_tid(cls,tid,uid):
        return dbSession.query(cls).filter(cls.c_id == tid,cls.u_id == uid).first()

class Challenge(Base):
    __tablename__ = 'title'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()))
    name = Column(String(100),nullable=False)
    title = Column(Text,nullable=False)
    c_id = Column(Integer, ForeignKey('category.id'))
    source = Column(Integer,nullable=False)
    flag = relationship("Flag", uselist=False)
    user = relationship("User", secondary=UserToChallenge.__table__)

    @classmethod
    def by_title(cls,title):
        return dbSession.query(cls).filter_by(title=title).first()

    @classmethod
    def all(cls):
        return dbSession.query(cls).all()

    @classmethod
    def by_id(cls,id):
        return dbSession.query(cls).filter_by(id=id).first()

    @classmethod
    def by_uuid(cls,uuid):
        return dbSession.query(cls).filter_by(uuid=uuid).first()

    @classmethod
    def by_name(cls,name):
        return dbSession.query(cls).filter_by(name=name).first()


class Flag(Base):
    __tablename__ = 'flag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    flag = Column(String(50),nullable=False)
    c_id = Column(Integer, ForeignKey("title.id"))
    @classmethod
    def all(cls):
        return dbSession.query(cls).all()

    @classmethod
    def by_id(cls, id):
        return dbSession.query(cls).filter_by(id=id).first()

    @classmethod
    def by_flag(cls,flag):
        return dbSession.query(cls).filter_by(flag=flag).first()

    @classmethod
    def by_cid(cls,cid):
        return dbSession.query(cls).filter_by(c_id=cid).first()
class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50),nullable=False)
    category = relationship('Challenge', backref='category')

    @classmethod
    def all(cls):
        return dbSession.query(cls).all()

    @classmethod
    def by_id(cls,id):
        return dbSession.query(cls).filter_by(id=id).first()

    @classmethod
    def by_name(cls,name):
        return dbSession.query(cls).filter_by(name=name).first()

