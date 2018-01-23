#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2018/1/23

#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from sqlalchemy import ForeignKey,create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:admin123@localhost/test_db?charset=utf8")
Base = declarative_base()  # 生成orm基类

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例


#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from sqlalchemy import Table, Column, Integer,String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:admin123@localhost/test_db?charset=utf8")
Base = declarative_base()

SessionCls = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = SessionCls()

grade_m2m_student = Table('grade_student', Base.metadata,
                                 Column('grade_id', Integer, ForeignKey('grade.id')),
                                 Column('student_id', Integer, ForeignKey('student.id')),
                                 )

class Grade(Base):            # 定义班级表
    """班级表"""
    __tablename__ = 'grade'    # 表名
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(32))

    def __repr__(self):
        return "<Grade->id:%s name:%s>" % (self.id,self.name)

class Student(Base):
    """学生表"""
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(32))
    qq = Column(String(32))
    grades = relationship("Grade",secondary=grade_m2m_student,backref="students")

    def __repr__(self):
        return "<Student-->id:%s name:%s qq:%s>" % (self.id,self.name,self.qq)

def init_db():
    Base.metadata.create_all(engine)  # 创建表结构

def drop_db():
    Base.metadata.drop_all(engine)  # 删除

def create_grade(name):
    obj = Grade(name=name)
    return obj

def create_student(name,qq):
    obj = Student(name=name,qq=qq)
    return obj


# drop_db()  # 删除表结构
# init_db()   # 创建表结构
#
# # 创建三个班级
# grade_obj = []
# grades = ["Python","Linux","Go"]
# for grade in grades:
#     obj = create_grade(grade)
#     grade_obj.append(obj)
# session.add_all(grade_obj)
# session.commit()
#
# # 添加多个学生
# stu_obj = []
# students = [("杨幂","10001"),("赵丽颖","10002"),("刘亦菲","10003"),("胡歌","10004"),("勒布朗","10005"),("科比","10006"),("布兰妮","10007"),("林志玲","10008"),
#              ("汤唯", "10009"),("张馨予","10010"),("赵伟彤","10011"),("李四","10012"),("王宝强","10013"),
#              ("陈意涵", "10014"),("周冬雨","10015"),("林心如","10016"),("范冰冰","10017"),("梁静茹","10018"),("武藤兰","10019"),("小苍","10020"),]
# for i in range(0,14):
#     obj = create_student(students[i][0],students[i][1])
#     obj.grades = [grade_obj[0],grade_obj[1]]  # 为学生关联班级
#     stu_obj.append(obj)
# for j in range(14,20):
#     obj = create_student(students[j][0], students[j][1])
#     obj.grades = grade_obj   # 为学生关联班级
#     stu_obj.append(obj)
# session.add_all(stu_obj)
# session.commit()
# print("ok...")

# 从grade表中通过.students查询Python班 所有的学生
grade_obj = session.query(Grade).filter_by(name="Python").first()
for stu in grade_obj.students:
    print(stu)
print("----------------------------------------------------------")

# 从stu 表中 通过.grades查询 id为4的学生所在的 所有班级
student_obj = session.query(Student).filter_by(id=4).first()
print(student_obj.grades)


# 运行结果：
# <Student-->id:10 name:张馨予 qq:10010>
# <Student-->id:17 name:范冰冰 qq:10017>
# <Student-->id:15 name:周冬雨 qq:10015>
# <Student-->id:4 name:胡歌 qq:10004>
# <Student-->id:8 name:林志玲 qq:10008>
# <Student-->id:9 name:汤唯 qq:10009>
# <Student-->id:12 name:李四 qq:10012>
# <Student-->id:19 name:武藤兰 qq:10019>
# <Student-->id:20 name:小苍 qq:10020>
# <Student-->id:5 name:勒布朗 qq:10005>
# <Student-->id:14 name:陈意涵 qq:10014>
# <Student-->id:18 name:梁静茹 qq:10018>
# <Student-->id:2 name:赵丽颖 qq:10002>
# <Student-->id:11 name:赵伟彤 qq:10011>
# <Student-->id:1 name:杨幂 qq:10001>
# <Student-->id:3 name:刘亦菲 qq:10003>
# <Student-->id:13 name:王宝强 qq:10013>
# <Student-->id:7 name:布兰妮 qq:10007>
# <Student-->id:6 name:科比 qq:10006>
# <Student-->id:16 name:林心如 qq:10016>
# ----------------------------------------------------------
# [<Grade->id:1 name:Python>, <Grade->id:2 name:Linux>]
