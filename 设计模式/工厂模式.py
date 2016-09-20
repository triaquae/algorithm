#_*_coding:utf-8_*_
__author__ = 'Alex Li'


'''
课程类是通用的
学校类是通用的
分校区可以是独立的类,继承通用的学校类

每个学校的课程 有共同点,有不同点
学生在不同的分校,注册流程是一样的

'''
class Course(object):
    '''课程类'''

    def __init__(self,teacher,course_type):
        self.name = course_type
        self.time_range = ""
        self.teacher = teacher
        self.students = []

    def level_test(self):
        '''入学前测试水平 '''
        print("做1小时测试题...")


class School(object):
    '''通用的学校类'''


    def create_course(self,course_type):
        pass



class BJSchoolBranch(School):
    '''北京分校'''
    teacher_list = {
        'alex':{'name':"Alex Li"},
        'oldboy':{},
        'wusir':{},
    }
    def create_course(self,course_type):
        if course_type == 'py_ops':
            return Course(self.teacher_list['alex'],course_type)
        elif course_type == 'linux':
            return Course(self.teacher_list['oldboy'],course_type)
        else:
            return None


class SHSchoolBranch(School):
    '''上海分校'''


    teacher_list = {
        'jack':{'name':"Jack chen"},
        'rain':{},
    }
    def create_course(self,course_type):
        if course_type == 'py_ops':
            return Course(self.teacher_list['jack'],course_type)
        elif course_type == 'linux':
            return Course(self.teacher_list['rain'],course_type)
        else:
            return None


if __name__ == "__main__":
    bj_school = BJSchoolBranch()
    bj_pyops_course = bj_school.create_course("py_ops")
    sh_school = SHSchoolBranch()
    sh_py_ops_course = sh_school.create_course("py_ops")

    stu1 = bj_school.enroll_course(bj_pyops_course, '北京学员2')
    stu2 = sh_school.enroll_course(sh_py_ops_course,'上海学员1')

    print(stu1.name,stu1.teacher)
    print(stu2.name,stu2.teacher)