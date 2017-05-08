#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
这里是主要代码的地方，其实就算在这里调用其他代码，项目入口就是直接调用这里的
'''
class School(object):
    '定义学校类'
    def __init__(self,name,addr,**kwargs):
        '构造函数(名字，地址，学生列表，班级列表，课程，老师列表)'
        self.name = name
        self.addr = addr
        self.student = []
        self.teacher = []
        self.grade = []
        self.course = []

    #学校的功能（开设课程，班级,招聘学生）这里会先做两个定好地址的实例
    def recruit(self,name,age,six,salary,course):
        '招聘老师'
        self.teacher.append(name)
        print( self.teacher)
    def creat_course(self):
        pass
    def creat_grade(self):
        pass
s1 = School('北京分校','北京')
s2 = School('上海分校','上海')
s1.recruit('hy',22,'M',5000,'py')
s1.recruit('ll',22,'M',5000,'py')

class School_Member(object):
    '定义学校成员类'
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex


class Teacher(School_Member):
    '定义老师'
    def __init__(self,name,age,sex,salary,course):
        '继承学校成员类'
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course
    #老师的功能
    def theaing(self,):
        print('%s开始讲%s的课程了'%(self.name,self.course))



class Student(School_Member):
    '定义学生'
    def __init__(self,name,age,sex,course):
        '继承学校成员类'
        super(Student,self).__init__(name,age,sex)
        self.course = course
    #定义学生的功能
    def listen(self):
        print('%s在听%s'%(self.name,self.course))
    #试试看




t1 = Teacher('hy',22,'M',5000,'py')
s1 = Student('ll',10,'F','py')
t1.theaing()
s1.listen()



def rum():
    '定义入口'
    print('开始了')