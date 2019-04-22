#encoding:utf-8
# 单表的操作

from sa_1 import (Base, drop_all_table, engine, User, Address)
from sqlalchemy.orm import sessionmaker # 这个是会话工厂


#增加单条
def addUser(account, pwd):
    db_session = sessionmaker(bind=engine)
    session = db_session()

    user = User(account=account, pwd=pwd)
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()
    return user


#增加多条
def add_many_user(users=[]):
    db_session = sessionmaker(bind=engine)
    session = db_session()

    us = []
    import datetime
    for ac, pwd, sc in users:
        us.append(User(account=ac, pwd=pwd, score=sc, birth=datetime.datetime.today()))
    session.add_all(us)
    session.commit()
    [session.refresh(u) for u in us]
    session.close()
    return us


#同时插入不同的数据对象
def add_diff_obj(*args):
    db_session = sessionmaker(engine)
    session = db_session()

    session.add_all(args)
    session.commit()
    [session.refresh(a) for a in args]
    session.close()
    return args

add_diff_obj(User('zhangsan', '5', '33'), Address(aname='上海市'))


# addUser("shen", 123)
# add_many_user([('xing', '2', '99'), ('bo', '3', '100')])


